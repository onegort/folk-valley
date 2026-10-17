import asyncio
import fcntl
import json
import os
import pty
import signal
import struct
import tempfile
import termios
import tty
import uuid
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
app = FastAPI(title="Folk Valley Terminal")
app.mount("/static", StaticFiles(directory=WEB), name="static")

# This is intentionally a fixed program, not a general-purpose shell.
# Each browser connection gets a separate working directory and save files.
MAX_SESSIONS = 30
active_sessions = set()

@app.get("/")
async def index():
    return FileResponse(WEB / "index.html")

async def read_pty(master_fd: int):
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    def ready():
        if not future.done():
            try:
                future.set_result(os.read(master_fd, 4096))
            except OSError:
                future.set_result(b"")
    loop.add_reader(master_fd, ready)
    try:
        return await future
    finally:
        loop.remove_reader(master_fd)

@app.websocket("/terminal")
async def terminal(websocket: WebSocket):
    await websocket.accept()
    if len(active_sessions) >= MAX_SESSIONS:
        await websocket.send_text("\r\nServer is busy. Please try again later.\r\n")
        await websocket.close(code=1013)
        return

    session_id = str(uuid.uuid4())
    active_sessions.add(session_id)
    workdir = Path(tempfile.mkdtemp(prefix="folk-valley-"))
    master_fd = slave_fd = None
    process = None
    try:
        # Set a useful initial terminal size so ANSI screen clearing behaves normally.
        master_fd, slave_fd = pty.openpty()
        fcntl.ioctl(slave_fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
        env = os.environ.copy()
        env.update({"TERM": "xterm-256color", "PYTHONUNBUFFERED": "1", "COLUMNS": "100", "LINES": "30"})
        process = await asyncio.create_subprocess_exec(
            "python", "-u", str(ROOT / "main.py"),
            cwd=str(workdir), stdin=slave_fd, stdout=slave_fd, stderr=slave_fd,
            env=env, start_new_session=True,
        )
        os.close(slave_fd)
        slave_fd = None
        await websocket.send_text("\x1b[?2004h")  # enable bracketed paste support where available

        async def send_output():
            while True:
                data = await read_pty(master_fd)
                if not data:
                    break
                await websocket.send_text(data.decode("utf-8", errors="replace"))

        async def receive_input():
            while True:
                message = await websocket.receive_text()
                try:
                    payload = json.loads(message)
                except json.JSONDecodeError:
                    payload = {"type": "input", "data": message}
                if payload.get("type") == "resize":
                    cols = max(40, min(200, int(payload.get("cols", 100))))
                    rows = max(12, min(60, int(payload.get("rows", 30))))
                    fcntl.ioctl(master_fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))
                    continue
                if payload.get("type") == "input":
                    data = payload.get("data", "")
                    if isinstance(data, str) and len(data) <= 4096:
                        os.write(master_fd, data.encode("utf-8", errors="replace"))

        output_task = asyncio.create_task(send_output())
        input_task = asyncio.create_task(receive_input())
        done, pending = await asyncio.wait(
            [output_task, input_task], return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        for task in done:
            try:
                task.result()
            except (WebSocketDisconnect, OSError, RuntimeError):
                pass
    except (WebSocketDisconnect, OSError, RuntimeError):
        pass
    finally:
        if process and process.returncode is None:
            try:
                os.killpg(process.pid, signal.SIGTERM)
                await asyncio.wait_for(process.wait(), timeout=2)
            except (ProcessLookupError, asyncio.TimeoutError):
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        for fd in (master_fd, slave_fd):
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
        # Remove the per-visitor save files when the session ends.
        for item in workdir.iterdir():
            try:
                item.unlink()
            except OSError:
                pass
        try:
            workdir.rmdir()
        except OSError:
            pass
        active_sessions.discard(session_id)
        try:
            await websocket.close()
        except Exception:
            pass
