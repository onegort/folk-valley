# Folk Valley V3.0 — browser terminal starter

This project wraps the supplied `main (3).py` game in a browser terminal using xterm.js and a Python WebSocket server. The game source is copied unchanged to `main.py`.

## What it does

- Displays the game in a black terminal-style box with ANSI colors and screen clearing.
- Sends typed input to a real Python process, so ordinary `input()` calls and `time.sleep()` work without rewriting the game.
- Starts a separate game process and temporary working directory for each browser connection. Save files are isolated per visitor and deleted when that connection ends.
- Runs in a Linux container, which provides a pseudo-terminal (PTY) for terminal behavior.

## Run locally

Requires Docker Desktop. From this folder:

```sh
docker build -t folk-valley-web .
docker run --rm -p 8000:8000 folk-valley-web
```

Then open <http://localhost:8000>.

You can also run it directly on Linux/macOS with Python 3.11+:

```sh
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --host 127.0.0.1 --port 8000
```

The direct-run option uses Unix PTY APIs, so it is intended for Linux/macOS. Use Docker on Windows.

## Publish and embed in Google Sites

1. Deploy this folder as a **Docker web service** on a host that supports long-lived WebSocket connections and persistent running containers. Configure the service to use the included `Dockerfile` and expose HTTP port `8000` (many hosts set a `PORT` environment variable; if yours requires that, adjust the command to use that port).
2. Open the deployed HTTPS URL and test the game, especially the title screen, menus, ANSI colors, and save/load behavior.
3. In Google Sites, choose **Insert → Embed → By URL**, paste the deployed site URL, and insert it. Resize the embed area to suit the terminal.

A static host such as GitHub Pages cannot run this Python backend by itself. The host must support WebSockets and a Python process/container.

## Important notes before public launch

- The current implementation is a prototype. Anyone with the URL can start a game process; `MAX_SESSIONS` limits concurrent sessions to 30, but production hosting should add rate limits and resource limits.
- Per-visitor save files live only for the browser session and are removed on disconnect. They are not permanent saves.
- Terminal library files are loaded from jsDelivr, so visitors need access to that CDN. For a stricter offline deployment, vendor xterm.js and the fit addon locally.
- The server starts only the fixed `main.py` program; it does not expose a shell or accept arbitrary command names.
- Test carefully before sharing publicly. The game has not yet been fully play-tested through the browser wrapper.
