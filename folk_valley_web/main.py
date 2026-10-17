# FOLK VALLEY MADE BY ME!!! :3

""" FOLK VALLEY V2.0: revolution (summary)
revamped time mechanics
added sanity and madness events
added distance mechanics
remastered hunger
"""

""" FOLK VALLEY V2.1: (summary)
fixed many inital bugs
fixed some input bugs
added title screen
"""

""" FOLK VALLEY V2.2: (summary)
created save files
finally nerfed diseases
added death messages
"""

""" FOLK VALLEY V2.3: light in the darkness (4/23/26)
nerfed distance (4000 -> 2000)
fixed save bug 
fixed madness event bug
fixed madness and event roll bug
added notifications maybe
actually fixed diseases
passive health regen
medibedis!
"""

""" FOLK VALLEY V2.4: blooming (4/24/26)
added floral curse (peak)
added group commands
  added the dungeon and the library
added resting
distance loss is less punishing (min 50% loss -> min 70% loss)
fixed other bugs idk
"""

""" FOLK VALLEY V2.5: a word worth thousands of pictures (5/6/26)
added the dungeon and the library
added book mechanics
added shop presets

"""

""" FOLK VALLEY V3.0: finis in aspectu
removed ALL downtime during game! (major addition)

added terminal (major addition)
  added expansions
    time
    manipulation
    infection
    vengance
  added generations
  added lincoln
  added simulations
    tbd
    
added lore
started to revamped text colors
REMOVED SPECIAL INVENTORY!!! (major addition)

added antidotes
changed pink flower and added new flowers
  rosavale
  wyrmrose
  slyphora
  velisara
  luneblossom

added some cutscenes
added splash text

"""

"""todo:
make game playable (ig bro)

change text and events when all/some folks are dead
winscreen
deathscreen revamp
terminus
chilled meat usage


character specialties??
fight mechanics??

"""

from linecache import getline
import time
import random
import math
import curses

  
#variables!!!

#static variables

class endrun(Exception):
  pass

class color:
  
  red = "\033[31m"
  bred = "\033[91m"
  green = "\033[32m"
  bgreen = "\033[92m"
  yellow = "\033[33m"
  byellow = "\033[93m"
  blue = "\033[34m"
  bblue = "\033[94m"
  pink = "\033[35m"
  bpink = "\033[95m"
  cyan = "\033[36m"
  bcyan = "\033[96m"
  bold = "\033[1m"
  white = "\033[37m"
  bgt = "\033[44m"
  resetbold = "\033[22m"
  reset = "\033[0m"
  
  
orderlist = [
  "leisurely pace (slow, efficent stamina, could find other goodies!)",
  "normal pace (determination for a end, but no need to rush)",
  "hastily pace (fastest, fast stamina loss, disease becomes more common)"
  ]
orders = [
  "leasurely pace",
  "normal pace",
  "hastily pace"
]
madnesslist = [
  "MILISTORE",
  "STAN",
  "SPINO_ANG",
  "FLOWERFIELD",
  "SPINO"
]
eventlist = [
  "LUCKYDROID", 
  "FLOWERFIELD", 
  "SPINO_NICE", 
  "SERENITY", 
  "SPINO", 
  "MYTH_TREE", 
  "NOAH", 
  "EVAN", 
  "SHAL_RIVER", 
  "DEEP_RIVER", 
  "THEGIVER", 
  "SPINO_ANG", 
  "STAN", 
  "MILISTORE",
  "NIGHT",
  "FLOWERFIELD",
  "MATHTEST",
  "MOUNTAIN",
  "ROULETTE",
  "ENCHWOOD"
]
splashtextlist = [
  ""
]

manuords = [
  "lose 3 health from the math test",
  "gain 20 george from the lucky droid",
  "complete baybaki's game without spining the gun",
  "use LUST",
  "reject spencers gift",
  "encounter stan",
  "escape the mountain via cave",
  "answer one of giver questions incorrectly",
  "obtain evah",
  "obtain the floral curse",
  "leave the flowerfield without picking a flower",
  "outsmart a madness event",
  "give yourself a disease",
  "cure nyxophilia",
  "cure virellosis",
  "cure umbrythia",
  "obtain a luneblossom",
  "obtain a folknix",
  "complete the mountain in less than a minute",
  "witness the death of a folk"
]
manuord1 = ""
manuord2 = ""
manuord3 = ""
manuord1ID = 0
manuord2ID = 0
manuord3ID = 0

lincoln = 0
runactive = 0
textbold = 0
textspeed = 3
debugmode = 0
testmode = 0
savecontinue = 0
savedticknum = 0
totdistance = 3000
rollseed = ""
ex_time = 0
ex_infection = 0
ex_manipulation = 0
ex_vengeance = 0
active_expansion = 0
difficulty = 1
simulation = "FOLK_VALLEY_421"
isday = 0

pres1status = 0
pres2status = 0
pres3status = 0
startgeorge = 100
bookid = 0
libhallskip = 0   
order = 1    
libraryskip = 0
dungeonskip = 0    
playerprevioushealth = 0
f1previoushealth = 0
f2previoushealth = 0
f3previoushealth = 0
diseasecooldown = 0
previousevent = -999     
specialinventory = {}
eventresult = 0    
madnessresult = 0
madnesschance = 0
sleepmode = 0
distancemultiplier = 1     
frame = 0
tickamm = 0
savedticknum = 0
eventrolls = []   
tickspeed = 0.1   
f1madness = 0
f2madness = 0
f3madness = 0    
loadday = 0
loaddistance = 0    
diseaserandom = 0     
umbrythiaSpread = []    
noHealing = 0
playerfoodmultiplier = 1
f1foodmultiplier = 1
f2foodmultiplier = 1
f3foodmultiplier = 1
playerinfectionTimer = 0
f1infectionTimer = 0
f2infectionTimer = 0
f3infectionTimer = 0   
foodvalue = 0
shortrandom = 0
shortinput = ""  
shortintinput = 0  
giverwantinput = 0   
showprincess = 0
smt = 0
dontresettime = 0    
giveriteration = 0      
milishopbuy = 0   
sloth = 0
glutton = 0     
event = 0
eventname = ""
midday = 0
correctanswergiver = 0
givergame = 0
infs1 = 1
vrep = 0

#check




"""

def inputcheck (input):
  try int(input)
  
"""

def runstartanim():
  print("\033[H\033[2J", end="")
  print("loading events...")
  time.sleep(0.05)
  print("loading selected expansion...")
  time.sleep(0.05)
  print("configuring to", simulation, "settings...")
  time.sleep(0.05)
  print("loading folk module...")
  time.sleep(0.05)
  print("loading mili.exe...")
  time.sleep(0.05)
  print("loading folkmarket...")
  time.sleep(0.05)
  print("loading simulated scenario...")
  time.sleep(0.05)
  print("loading :3...")
  time.sleep(0.05)
  print("loading intermission menu...")
  time.sleep(0.05)
  print("loading internal engine v3.0...")
  time.sleep(0.05)
  print("finalizing...")
  time.sleep(0.1)

def expansionsave():
  file = open("expansions.dat", "w")
  file.write(str(ex_time))
  file.write("\n")
  file.write(str(ex_infection))
  file.write("\n")
  file.write(str(ex_manipulation))
  file.write("\n")
  file.write(str(ex_vengeance))
  file.write("\n")
  file.close()
  
def generator(type):
  print("\033[H\033[2J", end="")
  global rollseed
  global ex_time
  global ex_infection
  global ex_manipulation
  global ex_vengeance
  rollseed = ""
  iter = 0
  result = 0

  
  if type == 1:
    #roll
    roll = random.randint(1,100)
    if roll == 1 or roll == 2:
      result = "3"
    elif roll < 10:
      result = "2"
    else:
      result = "1"
      
    #anim
    for val in range(20):
      print("\033[H\033[2J", end="")
      for let in "GENERATING":
        roll = random.randint(1,5)
        if roll == 1:
            print(f"{color.green}{let}", end="", flush=True)
        if roll == 2:
            print(f"{color.blue}{let}", end="", flush=True)
        if roll == 3:
            print(f"{color.red}{let}", end="", flush=True)
        if roll == 4:
            print(f"{color.byellow}{let}", end="", flush=True)
        if roll == 5:
            print(f"{color.white}{let}", end="", flush=True)
      time.sleep(0.1) 

    #reveal
    if result == "1":
      print(f"{color.green}{let}", end="", flush=True)
    if result == "2":
      print(f"{color.blue}{let}", end="", flush=True)
    if result == "3":
      print(f"{color.byellow}{let}", end="", flush=True)
    print("\033[H\033[2J", end="")
    print("GENERATING")
    time.sleep(1)

    #result
    print("\033[H\033[2J", end="")
    if result == "1":
      print(f"{color.green}", end="")
      for let in "STAGE ONE:":
        print(f"{let}", end = "", flush = True)
        time.sleep(0.05)
      time.sleep(0.5)
      roll = random.randint(1,4)
      
      if roll == 1:
        for let in " TIME EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.05)
          
        if ex_time < 1:
          ex_time = 1
          print("")
          print("new expansion!")
          
      if roll == 2:
        for let in " INFECTION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.05)

        if ex_infection < 1:
          ex_infection = 1
          print("")
          print("new expansion!")
          
      if roll == 3:
        for let in " MANIPULATION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.05)
          
        if ex_manipulation < 1:
          ex_manipulation = 1
          print("")
          print("new expansion!")
                  
      if roll == 4:
        for let in " VENGEANCE EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.05)
        if ex_vengeance < 1:
          ex_vengeance = 1
          print("")
          print("new expansion!")

    if result == "2":
      print(f"{color.blue}", end="")
      for let in "STAGE TWO:":
        print(f"{let}", end = "", flush = True)
        time.sleep(0.2)
      time.sleep(0.1)
      roll = random.randint(1,4)
      
      if roll == 1:
        for let in " TIME EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.1)
          
        if ex_time < 2:
          ex_time = 2

          print("")
          print("new expansion!")
          
      if roll == 2:
        for let in " INFECTION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.1)
        if ex_infection < 2:
          ex_infection = 2
          print("")
          print("new expansion!")
          
      if roll == 3:
        for let in " MANIPULATION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.1)
          
        if ex_manipulation < 2:
          ex_manipulation = 2
          print("")
          print("new expansion!")
        
      if roll == 4:
        for let in " VENGEANCE EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.1)
          
        if ex_vengeance < 2:
          ex_vengeance = 2
          print("")
          print("new expansion!")

    if result == "3":
      print(f"{color.byellow}", end="")
      for let in "STAGE THREE:":
        print(f"{let}", end = "", flush = True)
        time.sleep(0.2)
      time.sleep(1)
      roll = random.randint(1,4)
      
      if roll == 1:
        for let in " TIME EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
          
        if ex_time < 3:
          ex_time = 3
          print("")
          print("new expansion!")
          
      if roll == 2:
        for let in " INFECTION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
          
        if ex_infection < 3:
          ex_infection = 3
          print("")
          print("new expansion!")
          
      if roll == 3:
        for let in " MANIPULATION EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
          
        if ex_manipulation < 3:
          ex_manipulation = 3
          print("")
          print("new expansion!")
          
      if roll == 4:
        for let in " VENGEANCE EXPANSION":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
          
        if ex_vengeance < 3:
          ex_vengeance = 3
          print("")
          print("new expansion!")
          
    print("")
    print("any key for next")
    shortinput4 = input("")
  
  if type == 10:
    #roll
    for val in range(10):
      roll = random.randint(1,100)
      if roll == 1 or roll == 2:
        rollseed += "3"
      elif roll < 10:
        rollseed += "2"
      else:
        rollseed += "1"
        
    #anim
    for val in range(20):
      print("\033[H\033[2J", end="")
      for let in "GENERATING":
        roll = random.randint(1,5)
        if roll == 1:
            print(f"{color.green}{let}", end="", flush=True)
        if roll == 2:
            print(f"{color.blue}{let}", end="", flush=True)
        if roll == 3:
            print(f"{color.red}{let}", end="", flush=True)
        if roll == 4:
            print(f"{color.byellow}{let}", end="", flush=True)
        if roll == 5:
            print(f"{color.white}{let}", end="", flush=True)
      time.sleep(0.1) 

    #reveal
    print("\033[H\033[2J", end="")
    for let in "GENERATING":   
      roll = rollseed[iter]
      if roll == "1":
        print(f"{color.green}{let}", end="", flush=True)
      if roll == "2":
        print(f"{color.blue}{let}", end="", flush=True)
      if roll == "3":
        print(f"{color.byellow}{let}", end="", flush=True)
      iter += 1
    time.sleep(2)

    #results
    for val in rollseed:
      print("\033[H\033[2J", end="")
      if val == "1":
        print(f"{color.green}", end="")
        for let in "STAGE ONE:":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.05)
        time.sleep(0.5)
        roll = random.randint(1,4)
        
        if roll == 1:
          for let in " TIME EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.05)
            
          if ex_time < 1:
            ex_time = 1
            print("")
            print("new expansion!")
            
        if roll == 2:
          for let in " INFECTION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.05)

          if ex_infection < 1:
            ex_infection = 1
            print("")
            print("new expansion!")
            
        if roll == 3:
          for let in " MANIPULATION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.05)
            
          if ex_manipulation < 1:
            ex_manipulation = 1
            print("")
            print("new expansion!")
                    
        if roll == 4:
          for let in " VENGEANCE EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.05)
          if ex_vengeance < 1:
            ex_vengeance = 1
            print("")
            print("new expansion!")

      if val == "2":
        print(f"{color.blue}", end="")
        for let in "STAGE TWO:":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
        time.sleep(0.1)
        roll = random.randint(1,4)
        
        if roll == 1:
          for let in " TIME EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.1)
            
          if ex_time < 2:
            ex_time = 2

            print("")
            print("new expansion!")
            
        if roll == 2:
          for let in " INFECTION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.1)
          if ex_infection < 2:
            ex_infection = 2
            print("")
            print("new expansion!")
            
        if roll == 3:
          for let in " MANIPULATION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.1)
            
          if ex_manipulation < 2:
            ex_manipulation = 2
            print("")
            print("new expansion!")
          
        if roll == 4:
          for let in " VENGEANCE EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.1)
            
          if ex_vengeance < 2:
            ex_vengeance = 2
            print("")
            print("new expansion!")

      if val == "3":
        print(f"{color.byellow}", end="")
        for let in "STAGE THREE:":
          print(f"{let}", end = "", flush = True)
          time.sleep(0.2)
        time.sleep(1)
        roll = random.randint(1,4)
        
        if roll == 1:
          for let in " TIME EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.2)
            
          if ex_time < 3:
            ex_time = 3
            print("")
            print("new expansion!")
            
        if roll == 2:
          for let in " INFECTION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.2)
            
          if ex_infection < 3:
            ex_infection = 3
            print("")
            print("new expansion!")
            
        if roll == 3:
          for let in " MANIPULATION EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.2)
            
          if ex_manipulation < 3:
            ex_manipulation = 3
            print("")
            print("new expansion!")
            
        if roll == 4:
          for let in " VENGEANCE EXPANSION":
            print(f"{let}", end = "", flush = True)
            time.sleep(0.2)
            
          if ex_vengeance < 3:
            ex_vengeance = 3
            print("")
            print("new expansion!")
            
      print("")
      print("any key for next")
      print("(0) to skip")
      shortinput4 = input("")
      if shortinput4 == "0":
        break
        
def savegame():
  
  save = open("savedata.csv", "w")
  
  save.write("names")
  save.write("\n")
  save.write(playername)
  save.write("\n")
  save.write(folk1name)
  save.write("\n")
  save.write(folk2name)
  save.write("\n")
  save.write(folk3name)
  save.write("\n")

  save.write("health")
  save.write("\n")
  save.write(str(playerhealth))
  save.write("\n")
  save.write(str(f1health))
  save.write("\n")
  save.write(str(f2health))
  save.write("\n")
  save.write(str(f3health))
  save.write("\n")


  save.write("hunger")
  save.write("\n")
  save.write(str(playerhunger))
  save.write("\n")
  save.write(str(f1hunger))
  save.write("\n")
  save.write(str(f2hunger))
  save.write("\n")
  save.write(str(f3hunger))
  save.write("\n")

  save.write("stamina")
  save.write("\n")
  save.write(str(playerstamina))
  save.write("\n")
  save.write(str(f1stamina))
  save.write("\n")
  save.write(str(f2stamina))
  save.write("\n")
  save.write(str(f3stamina))
  save.write("\n")

  save.write("items")
  save.write("\n")
  save.write(str(george))
  save.write("\n")
  save.write(str(folkfood))
  save.write("\n")
  save.write(str(momsmeal))
  save.write("\n")
  save.write(str(folkmusket))
  save.write("\n")
  save.write(str(folksword))
  save.write("\n")
  save.write(str(ammo))
  save.write("\n")
  save.write(str(parts))
  save.write("\n")
  save.write(str(pickaxe))
  save.write("\n")
  save.write(str(chillmeat))
  save.write("\n")
  save.write(str(rosavale))
  save.write("\n")
  save.write(str(terminus))
  save.write("\n")
  save.write(str(folknix))
  save.write("\n")
  save.write(str(folkcorpbeacon))
  save.write("\n")
  save.write(str(envyitem))
  save.write("\n")
  save.write(str(lustitem))
  save.write("\n")
  save.write(str(greeditem))
  save.write("\n")
  save.write(str(slothitem))
  save.write("\n")
  save.write(str(prideitem))
  save.write("\n")
  save.write(str(wrathitem))
  save.write("\n")
  save.write(str(gluttonyitem))
  save.write("\n")
  save.write(str(tooth))
  save.write("\n")

  save.write("states")
  save.write("\n")
  save.write(str(serene))
  save.write("\n")
  save.write(str(NOmountain))
  save.write("\n")
  save.write(str(baybakidead))
  save.write("\n")
  save.write(str(deaddino))
  save.write("\n")
  save.write(str(deadtree))
  save.write("\n")
  save.write(str(happydino))
  save.write("\n")
  save.write(str(fcplayer))
  save.write("\n")
  save.write(str(fcfolk1))
  save.write("\n")
  save.write(str(fcfolk2))
  save.write("\n")
  save.write(str(fcfolk3))
  save.write("\n")
  save.write(str(lustactive))
  save.write("\n")
  save.write(str(lustfolk1))
  save.write("\n")
  save.write(str(lustfolk2))
  save.write("\n")
  save.write(str(lustfolk3))
  save.write("\n")

  save.write("other")
  save.write("\n")
  save.write(str(daynum))
  save.write("\n")
  save.write(str(distance))
  save.write("\n")
  save.write(str(playerfoodgainmultiplier))
  save.write("\n")
  save.write(str(f1foodgainmultiplier))
  save.write("\n")
  save.write(str(f2foodgainmultiplier))
  save.write("\n")
  save.write(str(f3foodgainmultiplier))
  save.write("\n")
  save.write(str(timesec))
  save.write("\n")
  save.write(str(timehr))
  save.write("\n")
  save.write(str(textbold))
  save.write("\n")
  save.write(str(textspeed))
  save.write("\n")
  save.write(str(debugmode))
  save.write("\n")

  save.write(str(playerdis))
  save.write("\n")
  save.write(str(folk1dis))
  save.write("\n")
  save.write(str(folk2dis))
  save.write("\n")
  save.write(str(folk3dis))
  save.write("\n")
  save.write(str(nyxoplasiaID))
  save.write("\n")
  save.write(str(virellosisID))
  save.write("\n")
  save.write(str(umbrythiaID))
  save.write("\n")

  save.write(str(noah))
  save.write("\n")
  save.write(str(evan))
  save.write("\n")
  save.write(str(evah))
  save.write("\n")
  save.write(str(medibedi))
  save.write("\n")
  save.write(str(maxhp))
  save.write("\n")
  save.write(str(fcstage))
  save.write("\n")
  save.write(str(order))
  save.write("\n")
  save.write(str(testmode))
  save.write("\n")
  save.write(str(score))
  save.write("\n")
  save.write(str(bandname))
  save.write("\n")
  save.write(str(wyrmrose))
  save.write("\n")
  save.write(str(slyphora))
  save.write("\n")
  save.write(str(velisara))
  save.write("\n")
  save.write(str(luneblossom))
  save.write("\n")
  save.write(str(meteor))
  save.write("\n")
  save.write(str(s1))
  save.write("\n")
  save.write(str(s2))
  save.write("\n")
  save.write(str(s3))
  save.write("\n")
  save.write(str(difficulty))
  save.write("\n")
  save.write(str(simulation))
  save.write("\n")
  save.write(str(active_expansion))
  save.write("\n")
  save.write(str(morn))
  save.write("\n")
  save.write(str(even))
  save.write("\n")
  save.write(str(manuord1))
  save.write("\n")
  save.write(str(manuord2))
  save.write("\n")
  save.write(str(manuord3))
  save.write("\n")
  save.write(str(manuord1ID))
  save.write("\n")
  save.write(str(manuord2ID))
  save.write("\n")
  save.write(str(manuord3ID))
  save.write("\n")
  save.write(str(infs1))
  save.write("\n")
  save.write(str(vrep))
  save.write("\n")
  save.write(str(antidote))
  save.write("\n")
  
  save.close()

def savepreset(slot, name):
  totalgeorge = 0
  if slot == "1":
    presetloc = open("preset1.csv", "w")
  if slot == "2":
    presetloc = open("preset2.csv", "w")
  if slot == "3":
    presetloc = open("preset3.csv", "w")

  presetloc.write(str(folkfood))
  presetloc.write("\n")
  presetloc.write(str(momsmeal))
  presetloc.write("\n")
  presetloc.write(str(folkmusket))
  presetloc.write("\n")
  presetloc.write(str(folksword))
  presetloc.write("\n")
  presetloc.write(str(ammo))
  presetloc.write("\n")
  presetloc.write(str(parts))
  presetloc.write("\n")
  presetloc.write(str(pickaxe))
  presetloc.write("\n")
  presetloc.write(str(medibedi))
  presetloc.write("\n")
  
  totalgeorge = startgeorge - george
  presetloc.write(str(totalgeorge))
  presetloc.write("\n")
  presetloc.write(str(name))

  presetloc.close()

def presetcheck():
  global pres1status
  global pres2status
  global pres3status

  try:
    file = open("preset1.csv", "r")
  except FileNotFoundError:
    pres1status = 0
  else: pres1status = 1
    
  try:
    file = open("preset2.csv", "r")
  except FileNotFoundError:
    pres2status = 0
  else: pres2status = 1

  try:
    file = open("preset3.csv", "r")
  except FileNotFoundError:
    pres3status = 0
  else: 
    pres3status = 1

def credits(page):
  if page == 1:
    print("\033[H\033[2J", end="")
    print("credits page 1: overview")
    print("FOLK VALLEY, by dailyn")
    print("a oregon trail inspired game")
    print("")
    print("created on: juicemind")
    print("for ap computer science principles")
    print("all code hand typed")
    print("")
    print("(0) exit")
    print("(1) next page")
  if page == 2:
    print("\033[H\033[2J", end="")
    print("credits page 2: references")
    print("")
    print("*** isle by badorkbee (best roblox game) ***")
    print("^ heavy inspiration ^")
    print("")
    print("randomly generated droids by justenoughideas")
    print("genshin impact by mihoyo")
    print("eaden wright")
    print("lexycat")
    print("doors by lightning_splash")
    print("(more to come)")
    print("")
    print("(0) exit")
    print("(1) next page")
    print("(2) back page")

  if page == 3:
    print("\033[H\033[2J", end="")
    print("credits page 1: other")
    print("playtesters:")
    print("byron q")
    print("eaden w")
    print("jacob s")
    print("gram m")
    print("jeremy oc")
    print("")
    print("(0) exit")
    print("(1) back page")

#check files
try: file = open("fv.dat", "r")
except FileNotFoundError:
  file = open("fv.dat", "w")
  file.write("0")
  file.close()
else:
  lincoln = int(float(getline("fv.dat", 1).strip()))
  file.close()

try: file = open("expansions.dat", "r")
except FileNotFoundError:
  file = open("expansions.dat", "w")
  file.write("0")
  file.write("\n")
  file.write("0")
  file.write("\n")
  file.write("0")
  file.write("\n")
  file.write("0")
  file.write("\n")
  
  file.close()
else:
  ex_time = int(float(getline("expansions.dat", 1).strip()))
  ex_infection = int(float(getline("expansions.dat", 2).strip()))
  ex_manipulation = int(float(getline("expansions.dat", 3).strip()))
  ex_vengeance = int(float(getline("expansions.dat", 4).strip()))
  file.close()

#game start
print("enter 0 to skip opening text")
shortinput = input()



#THE LOOP 

if shortinput == "0":
  pass
else:
  print("\033[H\033[2J", end="")
  print("the glistening sun, the radiating heat, the sturdy rock")
  time.sleep(2)
  print("you open your eyes")
  time.sleep(1)
  print("three people with you")
  time.sleep(1)
  print("two large mountains on either side")
  time.sleep(1)
  print("one direction is forward")
  time.sleep(2)
    
while True: 
  menuphase = 1
  active_expansion = active_expansion // 10
  while menuphase == 1:
    if savecontinue == 1:
      menuphase = 0
      break
    print("\033[H\033[2J", end="")
    print(f"{color.reset}{color.byellow}FOLK VALLEY")
    print("(1) start game")
    print("(2) settings")
    print("(3) credits")
    print("(4) load game")
    print("(5) the terminal")
    shortinput = input("")
    if shortinput == "1":
      runstartanim()
      menuphase = 0
      runactive = 1
      
    while shortinput == "2":
      if savecontinue == 1:
        break
      if textbold == 1:
        print(f"{color.bold}\033[H\033[2J", end="")
      else:
        print(f"{color.resetbold}\033[H\033[2J", end="")
      print("\033[H\033[2J", end="")
      print("(1) text speed:", textspeed)
      print("(2) text bold:", textbold)
      print("(3) debug mode:", debugmode)
      print("(4) test mode:", testmode)
      print("(5) back")
      
      shortinput2 = input("")
      while shortinput2 == "1":
        print("\033[H\033[2J", end="")
        print("text speed: (enter whole number)")
        print("text speed is the time that text will wait to show")
        print("press enter to test text speed")
        shortinput3 = input("")
        if shortinput3 == "":
          print("\033[H\033[2J", end="")
          print("1")
          time.sleep(textspeed)
          print("2")
          time.sleep(textspeed)
          print("3")
          time.sleep(textspeed)
        else:
          shortinput3 = int(shortinput3)
          textspeed = shortinput3
          shortinput2 = 0
      if shortinput2 == "2":
        if textbold == 0:
          textbold = 1
        else:
          textbold = 0
      if shortinput2 == "3":
        if debugmode == 1:
          debugmode = 0
        else:
          debugmode = 1
      if shortinput2 == "4":
        if testmode == 1:
          testmode = 0
        else:
          testmode = 1
      if shortinput2 == "5":
        shortinput = 0
  
    if shortinput == "3":
      credpage = 1
    while shortinput == "3":
      while credpage == 1:
        credits(1)
        shortinput2 = input("")
        if shortinput2 == "0":
          credpage = 0
          shortinput = 0
        if shortinput2 == "1":
          credpage = 2
          
      while credpage == 2:
        credits(2)
        shortinput2 = input("")
        if shortinput2 == "0":
          credpage = 0
          shortinput = 0
        if shortinput2 == "1":
          credpage = 3
        if shortinput2 == "2":
          credpage = 1
          
      while credpage == 3:
        credits(3)
        shortinput2 = input("")
        if shortinput2 == "0":
          credpage = 0
          shortinput = 0
        if shortinput2 == "1":
          credpage = 2
        
    while shortinput == "4":
      try: save = open("savedata.csv", "r")
      except FileNotFoundError:
        print("you do not have a save file!")
        time.sleep(2)
        shortinput = 0
      except ValueError:
        print("your save file is outdated :c")
        time.sleep(2)
        shortinput = 0
      else:
        if getline("savedata.csv", 1) != "":
          print("\033[H\033[2J", end="")
          print("save file found!")
          print("distance left:", math.ceil(int(float(getline("savedata.csv", 60).strip()))))
          print("day:", math.ceil(int(float(getline("savedata.csv", 59).strip()))))
          print("time:", math.ceil(int(float(getline("savedata.csv", 66).strip()))), ":", math.ceil(int(float(getline("savedata.csv", 65).strip()))))
          print("do you want to load this file?")
          print("(1) yes")
          print("(2) no")
          shortinput = input("")
          if shortinput == "1":
            playername = getline("savedata.csv", 2).strip()
            folk1name = getline("savedata.csv", 3).strip()
            folk2name = getline("savedata.csv", 4).strip()
            folk3name = getline("savedata.csv", 5).strip()
            
            playerhealth = int(float(getline("savedata.csv", 7).strip()))
            f1health = int(float(getline("savedata.csv", 8).strip()))
            f2health = int(float(getline("savedata.csv", 9).strip()))
            f3health = int(float(getline("savedata.csv", 10).strip()))
    
            playerhunger = int(float(getline("savedata.csv", 12).strip()))
            f1hunger = int(float(getline("savedata.csv", 13).strip()))
            f2hunger = int(float(getline("savedata.csv", 14).strip()))
            f3hunger = int(float(getline("savedata.csv", 15).strip()))
    
            playerstamina = int(float(getline("savedata.csv", 17).strip()))
            f1stamina = int(float(getline("savedata.csv", 18).strip()))
            f2stamina = int(float(getline("savedata.csv", 19).strip()))
            f3stamina = int(float(getline("savedata.csv", 20).strip()))
    
            george = int(float(getline("savedata.csv", 22).strip()))
            folkfood = int(float(getline("savedata.csv", 23).strip()))
            momsmeal = int(float(getline("savedata.csv", 24).strip()))
            folkmusket = int(float(getline("savedata.csv", 25).strip()))
            folksword = int(float(getline("savedata.csv", 26).strip()))
            ammo = int(float(getline("savedata.csv", 27).strip()))
            parts = int(float(getline("savedata.csv", 28).strip()))
            pickaxe = int(float(getline("savedata.csv", 29).strip()))
            chillmeat = int(float(getline("savedata.csv", 30).strip()))
            rosavale = int(float(getline("savedata.csv", 31).strip()))
            terminus = int(float(getline("savedata.csv", 32).strip()))
            folknix = int(float(getline("savedata.csv", 33).strip()))
            folkcorpbeacon = int(float(getline("savedata.csv", 34).strip()))
            envyitem = int(float(getline("savedata.csv", 35).strip()))
            lustitem = int(float(getline("savedata.csv", 36).strip()))
            greeditem = int(float(getline("savedata.csv", 37).strip()))
            slothitem = int(float(getline("savedata.csv", 38).strip()))
            prideitem = int(float(getline("savedata.csv", 39).strip()))
            wrathitem = int(float(getline("savedata.csv", 40).strip()))
            gluttonyitem = int(float(getline("savedata.csv", 41).strip()))
            tooth = int(float(getline("savedata.csv", 42).strip()))
    
            serene = int(float(getline("savedata.csv", 44).strip()))
            NOmountain = int(float(getline("savedata.csv", 45).strip()))
            baybakidead = int(float(getline("savedata.csv", 46).strip()))
            deaddino = int(float(getline("savedata.csv", 47).strip()))
            deadtree = int(float(getline("savedata.csv", 48).strip()))
            happydino = int(float(getline("savedata.csv", 49).strip()))
            fcplayer = int(float(getline("savedata.csv", 50).strip()))
            fcfolk1 = int(float(getline("savedata.csv", 51).strip()))
            fcfolk2 = int(float(getline("savedata.csv", 52).strip()))
            fcfolk3 = int(float(getline("savedata.csv", 53).strip()))
            lustactive = int(float(getline("savedata.csv", 54).strip()))
            lustfolk1 = int(float(getline("savedata.csv", 55).strip()))
            lustfolk2 = int(float(getline("savedata.csv", 56).strip()))
            lustfolk3 = int(float(getline("savedata.csv", 57).strip()))
    
            daynum = int(float(getline("savedata.csv", 59).strip()))
            distance = int(float(getline("savedata.csv", 60).strip()))
            playerfoodgainmultiplier = int(float(getline("savedata.csv", 61).strip()))
            f1foodgainmultiplier = int(float(getline("savedata.csv", 62).strip()))
            f2foodgainmultiplier = int(float(getline("savedata.csv", 63).strip()))
            f3foodgainmultiplier = int(float(getline("savedata.csv", 64).strip()))
            timesec = int(float(getline("savedata.csv", 65).strip()))
            timehr = int(float(getline("savedata.csv", 66).strip()))
            textbold = int(float(getline("savedata.csv", 67).strip()))
            textspeed = int(float(getline("savedata.csv", 68).strip()))
            debugmode = int(float(getline("savedata.csv", 69).strip()))
    
            playerdis = int(float(getline("savedata.csv", 70).strip()))
            folk1dis = int(float(getline("savedata.csv", 71).strip()))
            folk2dis = int(float(getline("savedata.csv", 72).strip()))
            folk3dis = int(float(getline("savedata.csv", 73).strip()))
            nyxoplasiaID = int(float(getline("savedata.csv", 74).strip()))
            virellosisID = int(float(getline("savedata.csv", 75).strip()))
            umbrythiaID = int(float(getline("savedata.csv", 76).strip()))
    
            noah = int(float(getline("savedata.csv", 77).strip()))
            evan = int(float(getline("savedata.csv", 78).strip()))
            evah = int(float(getline("savedata.csv", 79).strip()))
            medibedi = int(float(getline("savedata.csv", 80).strip()))
            maxhp = int(float(getline("savedata.csv", 81).strip()))
            fcstage = int(float(getline("savedata.csv", 82).strip()))
            order = int(float(getline("savedata.csv", 83).strip()))
            testmode = int(float(getline("savedata.csv", 84).strip()))
            score = int(float(getline("savedata.csv",85).strip()))
            bandname = getline("savedata.csv",86).strip()
            wyrmrose = int(float(getline("savedata.csv",87).strip()))
            slyphora = int(float(getline("savedata.csv",88).strip()))
            velisara = int(float(getline("savedata.csv",89).strip()))
            luneblossom = int(float(getline("savedata.csv",90).strip()))
            meteor = int(float(getline("savedata.csv",91).strip()))
            s1 = int(float(getline("savedata.csv",92).strip()))
            s2 = int(float(getline("savedata.csv",93).strip()))
            s3 = int(float(getline("savedata.csv",94).strip()))
            difficulty = int(float(getline("savedata.csv",95).strip()))
            simulation = getline("savedata.csv",96).strip()
            active_expansion = int(float(getline("savedata.csv",97).strip()))
            morn = int(float(getline("savedata.csv",98).strip()))
            even = int(float(getline("savedata.csv",99).strip()))
            manueventcd = int(float(getline("savedata.csv",99).strip()))
            manuord1 = getline("savedata.csv",100).strip()
            manuord2 = getline("savedata.csv",101).strip()
            manuord3 = getline("savedata.csv",102).strip()
            manuord1ID = int(float(getline("savedata.csv",103).strip()))
            manuord2ID = int(float(getline("savedata.csv",104).strip()))
            manuord3ID = int(float(getline("savedata.csv",105).strip()))
            infs1 = int(float(getline("savedata.csv",106).strip()))
            vrep = int(float(getline("savedata.csv",107).strip()))
            antidote = int(float(getline("savedata.csv",108).strip()))
            save.close()
            savecontinue = 1
            runactive = 1
            runstartanim()
            break
          else:
            shortinput = 0
        else:
          print("no save found")
          time.sleep(textspeed)
          shortinput = 0     

    while shortinput == "5":
      print(f"\033[H\033[2J", end="")
      print(f"{color.white}THE TERMINAL")
      print(f"welcome{color.red} SUBJECT 6126{color.white}")
      print("(1) cmd.SIMULATION_SET")
      print("(2) cmd.CAPABILITY_EXPANDER")
      print("(3) cmd.EXPANSION_LOADER")
      print("(4) RETURN ZERO")

      shortinput2 = input("")
      while shortinput2 == "1":
        print("\033[H\033[2J", end="")
        print(f"{color.white}THE TERMINAL")
        print(f"welcome{color.red} SUBJECT 6126{color.white}")
        print("welcome to the simulation loader!")
        print("simulations edit the experience of the valley!")
        print("")
        print(f"{color.bblue}(1) FOLK_VALLEY_421 (easiest)")
        print(f"{color.green}(2) FOLK_VALLEY_2672")
        print(f"{color.yellow}(3) FOLK_VALLEY_4106")
        print(f"{color.red}(4) FOLK_VALLEY_8321")
        print(f"{color.pink}(5) FOLK_VALLEY_13 (hardest)")
        print("")
        print(f"{color.white}current simulation:", simulation)
        print("press 0 to go back")

        shortinput3 = input("")
        if shortinput3 == "0":
          shortinput2 = 0
        if shortinput3 == "1":
          simulation = "FOLK_VALLEY_421"
          difficulty = 1
        if shortinput3 == "2":
          simulation = "FOLK_VALLEY_2672"
          difficulty = 2
        if shortinput3 == "3":
          simulation = "FOLK_VALLEY_4106"
          difficulty = 3
        if shortinput3 == "4":
          simulation = "FOLK_VALLEY_8321"
          difficulty = 4
        if shortinput3 == "5":
          simulation = "FOLK_VALLEY_13"
          difficulty = 5
      
      while shortinput2 == "2":
        expansionsave()
        print("\033[H\033[2J", end="")
        print(f"{color.white}THE TERMINAL")
        print(f"welcome{color.red} SUBJECT 6126{color.white}")
        print("the capability expander allows you to generate new expansions for your experiences!")  
        print("")
        print("(1) one generation: 50 lincoln")
        print("(2) ten generation: 500 lincoln")
        print("(3) read manual")
        print("(4) CAPABILITY_EXPANDER.exit")

        shortinput3 = input("")

        if shortinput3 == "1":
          if lincoln >= 10:
            print("are you sure you want to spend 50 lincoln for one generation?")
            print("(1) yes")
            shortinput4 = input("")
            if shortinput4 == "1":
              lincoln -= 50
              file = open("fv.dat", "w")
              file.write(str(lincoln))
              file.close()
              generator(1)
            else:
              continue
          else:
            print("you cannot afford this!")
            time.sleep(2)
            
        if shortinput3 == "2":
          if lincoln >= 100:
            print("are you sure you want to spend 500 lincoln for ten generations?")
            print("(1) yes")
            shortinput4 = input("")
            if shortinput4 == "1":
              lincoln -= 500
              file = open("fv.dat", "w")
              file.write(str(lincoln))
              file.close()
              generator(10)
            else:
              continue
          else:
            print("you cannot afford this!")
            time.sleep(2)
          
        if shortinput3 == "3":
          print("\033[H\033[2J", end="")
          print(f"{color.white}THE TERMINAL")
          print(f"welcome{color.red} SUBJECT 6126{color.white}")
          print("")
          print("stage 3 expansion: 2%")
          print("stage 2 expansion: 8%")
          print("stage 1 expansion: 90%")
          print("")
          print("possible expansions come from this list:")
          print("time, manipulation, infection, vengeance")
          print("")
          print("SKIPPING WILL RESULT IN THE LOSS OF THE REST OF THE GENERATION")
          print("pro tip: looking at the text may indicate your results")
          print("")
          print("(1) back")

          shortinput4 = input("")
          
        if shortinput3 == "4":
          shortinput2 = 0

      while shortinput2 == "3":
        print("\033[H\033[2J", end="")
        print(f"{color.white}THE TERMINAL")
        print(f"welcome{color.red} SUBJECT 6126{color.white}")
        print(f"the expansion loader allows you to load your expansions into your {color.red}experiments... {color.white}")  
        print("")
        print("your expansions:")
        print("")
        
        if ex_time != 0:
          print(f"{color.white}(1) stage {ex_time} time expansion!")
        if active_expansion == 1:
          print("active!")
        else:
          print("inactive")
        print("")
        
        if ex_infection != 0:
          print(f"{color.green}(2) stage {ex_infection} infection expansion!")
        if active_expansion == 2:
          print("active!")
        else:
          print("inactive")
        print("")

        if ex_manipulation != 0:
          print(f"{color.bpink}(3) stage {ex_manipulation} manipulation expansion!")
        if active_expansion == 3:
          print("active!")
        else:
          print("inactive")
        print("")

        if ex_vengeance != 0:
          print(f"{color.red}(4) stage {ex_vengeance} vengeance expansion!")
        if active_expansion == 4:
          print("active!")
        else:
          print("inactive")

        print(f"{color.white}")
        print("(0) EXPANSION_LOADER.exit")
        print("(-1) information")

        shortinput3 = input("")

        if shortinput3 == "0":
          shortinput2 = 0

        if shortinput3 == "1" and ex_time != 0:
          active_expansion = 1

        if shortinput3 == "2" and ex_infection != 0:
          active_expansion = 2

        if shortinput3 == "3" and ex_manipulation != 0:
          active_expansion = 3

        if shortinput3 == "4" and ex_vengeance != 0:
          active_expansion = 4
      if shortinput2 == "4":
        shortinput = 0
        
  try:  
    while runactive == 1:
      if active_expansion == 1:
        if ex_time == 1:
          active_expansion = 11
        if ex_time == 2:
          active_expansion = 12
        if ex_time == 3:
          active_expansion = 13
          
      if active_expansion == 2:
        if ex_infection == 1:
          active_expansion = 21
        if ex_infection == 2:
          active_expansion = 22
        if ex_infection == 3:
          active_expansion = 23

      if active_expansion == 3:
        if ex_manipulation == 1:
          active_expansion = 31
        if ex_manipulation == 2:
          active_expansion = 32
        if ex_manipulation == 3:
          active_expansion = 33
          
      if active_expansion == 4:
        if ex_vengeance == 1:
          active_expansion = 41
        if ex_vengeance == 2:
          active_expansion = 42
        if ex_vengeance == 3:
          active_expansion = 43
          
      #varible set
      if savecontinue == 0:
        playername = ""
        folk1name = ""
        folk2name = ""
        folk3name = ""
        bandname = ""
  
        f1health = 10
        f2health = 10
        f3health = 10
        f1hunger = 100
        f2hunger = 100
        f3hunger = 100
        f1stamina = 100
        f2stamina = 100
        f3stamina = 100
  
        folkcount = 3
        playerhealth = 10
        playerhunger = 100
        playerstamina = 100
        playermadness = 0
        maxhp = 10
  
        gluttonyitem = 0
        wrathitem = 0
        prideitem = 0
        greeditem = 0
        lustitem = 0
        envyitem = 0
        slothitem = 0
        lustactive = 0
        lustfolk1 = 0
        lustfolk2 = 0
        lustfolk3 = 0
        
        george = 100
        folkfood = 0
        medibedi = 0
        momsmeal = 0
        chillmeat = 0
        folksword = 0
        folkmusket = 0 
        folkrapier = 0
        folkrifle = 0
        nuke = 0
        ammo = 0
        parts = 0
        antidote = 0
        pickaxe = 0
        folkcorpbeacon = 0
        folknix = 0
        terminus = 0
        
        rosavale = 0
        wyrmrose = 0
        slyphora = 0
        velisara = 0
        luneblossom = 0
        s1 = 0
        s2 = 0
        s3 = 0
        
        playerfoodgainmultiplier = 1
        f1foodgainmultiplier = 1
        f2foodgainmultiplier = 1
        f3foodgainmultiplier = 1
  
        evan = 0
        noah = 0
        evah = 0
  
        folk1dis = 0
        folk2dis = 0
        folk3dis = 0
        playerdis = 0
        fcplayer = 0
        fcfolk1 = 0
        fcfolk2 = 0
        fcfolk3 = 0
        nyxoplasiaID = 0
        virellosisID = 0
        umbrythiaID = 0
  
        happydino = 0
        serene = 0
        deaddino = 0
        deadtree = 0
        baybakidead = 0
        NOmountain = 0
        distance = 3000
        daynum = 1
        score = 0
        timesec = "0"
        timehr = "00"
        fcstage = 0
        tooth = 0
        meteor = 0

        morn = 6
        even = 20
        manueventcd = 0
        isday = 0
        manuord1ID = 0
        manuord2ID = 0
        manuord3ID = 0
        infs1 = 1
        vrep = 0
        
      if debugmode == 1:
        momsmeal = 9999
        george = 9999
      nameskip = 0
      
      if debugmode == 0 and savecontinue == 0 and nameskip == 0:
        print("\033[H\033[2J", end="")
        print("type the name of your character")
        playername = input("")
        if playername == ":3":
          playername = "furina"
          folk1name = "columbina"
          folk2name = "arlechinno"
          folk3name = "sandrone"
          bandname = "tuff"
          nameskip = 1
        else:    
          print("hi", playername, "! it is time for you name 3 other folks")
          folk1name = input("folk 1: ")
          folk2name = input("folk 2: ")
          folk3name = input("folk 3: ")
          
          print("finally what is the name of your new band")
          bandname = input("band name:")
          
          print("the band of", bandname, "led by", playername, "with", folk1name, ",", folk2name, "and," ,folk3name)
          print("is this correct? yes/no")
          shortinput = input("")
          print("entering the folkchamber")
          time.sleep(3)
          print("\033[H\033[2J", end="")
      elif debugmode == 1:
        playername = "player"
        folk1name = "folk1"
        folk2name = "folk2"
        folk3name = "folk3"
        bandname = "band"
      #more setup for packing stage!
      menuinput = ""
    
      if debugmode == 1:
        folkfood = 999 
        momsmeal = 999
        folksword = 999
        folkmusket = 999
        folkrapier = 999
        antidote = 999
        folkrifle = 999
        medibedi = 99
        parts = 999
        startgeorge = 999
        george = 999
        ammo = 999
        textspeed = 0.5
      if testmode == 1:
        folkfood = 999 
        momsmeal = 999
        startgeorge = 999
        antidote = 999
        george = 999
        folksword = 999
        folkmusket = 999
        medibedi = 999
        folkrapier = 999
        folkrifle = 999
        parts = 999
        ammo = 999
        savecontinue = 1
      
      def menu ():
        menuinput = 0
        print("\033[H\033[2J", end="")
        print("george balance:", george,)
        print("you can spend this currency in the following shops")
        print("be careful, as this may be the only shop you will get!")
        print("although saving money might help you later on!")
        print("")
        print("wat do u want to do (type the number)")
        print("(0) move past the stores (recommended for new players)")
        if active_expansion // 10 == 4:
          print(f"{color.red}(CLOSED) foodstore{color.white}")
        else:
          print("(1) food store")
        print("(2) weapons store")
        print("(3) tim store")
        print("(4) inventory")
        print("(5) ENTER THE VALLEY c:<")
        print("(6) preset terminal")
      
      def dungeon():
        global dungeonskip
        if dungeonskip == 0:
          print("\033[H\033[2J", end="")
          print("you open the small crooked door and enter a dimly lit stone room")
          time.sleep(textspeed)
          print("as your eyes adjust you notice plenty of cells with desperate folks and skeletons")
          time.sleep(textspeed)
          dungeonskip = 1
        print("(1) move to the first cell")
        print("(2) leave")
      
      def library():
        global libraryskip
        if libraryskip == 0:
          print("\033[H\033[2J", end="")
          print("you move through the large gates to the library")
          time.sleep(textspeed)
          print("stacks and stacks of bookshelves stretch the towering walls")
          time.sleep(textspeed)
          print("5 books lay on the table in front of you")
          print("")
        if libraryskip == 1:
          print("\033[H\033[2J", end="")
        libraryskip = 1
        print("(1) basic skills for great adventures")
        print("(2) the mysteries of folk valley")
        print("(3) how to not suck at being a leader")
        print("(4) the inventions of folk valley")
        print("(5) TIMS COOL BOOK")
        print("(6) leave")
                
      def books(id):
                
        if id == 11:
          print("\033[H\033[2J", end="")
          print("BASIC SKILLS FOR GREAT ADVENTURE")
          print("")
          print("TABLE OF CONTENTS")
          print("(1) status")
          print("(2) days")
          print("(3) diseases")
          print("")
          print("(0) put book away")
        
        if id == 12:
          print("\033[H\033[2J", end="")
          print("BASIC SKILLS FOR GREAT ADVENTURE")
          print("CHAPTER 1: STATUS")
          print("")
          print("in the folk valley, you are not immortal, and you are far from it")
          print("every character including yourself has 10 health, 100 hunger, and 100 stamina")
          print("")
          print("hunger decrease per tick (see page 2 for day info): random 0 - 0.5 * the character's food loss multiplier (random per day and can be altered)")
          print("you will lose around 30 hunger a day, but it can vary")
          print("")
          print("stamina decrease per tick: 0.3 + (0.1 per dead folk)")
          print("**stamina is very important to keep up, as its never a good experience to go mad!**")
          print("you can increase stamina by resting and sleeping")
          print("")
          print("if hunger depletes to zero, health decreases by 2 for every")
          print("")
          print("diseases will also affect your status immensely (see page 3)")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")         
        
        if id == 13:
          print("\033[H\033[2J", end="")
          print("BASIC SKILLS FOR GREAT ADVENTURE")
          print("CHAPTER 2: DAYS")
          print("")
          print("days and nights, the empowering force behind mental progress")
          print("there are 72 ticks in 6 hours, after that 6 hour mark, the time period will end")
          print("each tick depletes hunger and stamina, and rolls for events and diseases")
          print("")
          print("there is a 1/600 chance for a disease every tick (see page 3 for disease info)")
          print("there is a 1/300 chance for a event every tick, with the chance increasing every roll")
          print("")
          print("not taking damage for a time period will heal that character for 1 health")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
          
        if id == 14:
          print("\033[H\033[2J", end="")
          print("BASIC SKILLS FOR GREAT ADVENTURE")
          print("CHAPTER 3: DISEASES")
          print("")
          print("diseases can single handedly bring many bands to the grave")
          print("each disease comes in stages, 3 being the worst")
          print("the higher stages also cause the effects of the lower stages (stage 3 also causes stage 1 and 2)")
          print("each effect happens once at the end of a time period")
          print("")
          print("nyxoplasia")
          print("stage 1: -1 health to target and other character")
          print("stage 2: -1 health from everyone (overrides stage 1)")
          print("stage 3: prevents all healing and serene effects")
          print("")
          print("virellosis")
          print("stage 1: -20 hunger to target")
          print("stage 2: rids of a random food item")
          print("stage 3: character permanently gains half food from eating")
          print("")
          print("umbrythia")
          print("stage 1: -1 health to target")
          print("stage 2: -20 hunger to target")
          print("stage 3: chance to spread stage 1 variant to other folk")
          print("")
          print("diseases will have a random amount of time before the character will recover")
          print("this time is usually 1 - 2 days")
          print("the target recovers much faster if sleeping or resting")
          print("")
          print("(1) back a page")
          print("(0) put book away")
      
          
        if id == 21:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("")
          print("TABLE OF CONTENTS")
          print("(1) LUCKYDROID")
          print("(2) FIELDS")
          print("(3) SPENCER THE SPINO")
          print("(4) TREE")
          print("(5) NOAH + EVAN")
          print("(6) RIVERS")
          print("(7) GIVER")
          print("(8) BAYBAKI'S GAMES")
          print("(9) MOUNTAIN")
          print("")
          print("(0) put book away")
      
        if id == 22:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER ONE: LUCKYDROID")
          print("")
          print("this occurence begins with the introduction of a blocky white and yellow character resembling a cat")
          print("it is stationary and desolate, as if its a statue...")
          print("reports tell great wealth comes with striking the statue, it seemingly being more generous the faster its struck")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
        
        if id == 23:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER TWO: FIELDS")
          print("")
          print("fields are common occurences in the valley, with reports of strange side effects")
          print("")
          print("a normal serene field inflicts great reassurance within the observer")
          print("additionaly, flowers can grow in great numbers on these fields, and may possess unusual effects")
          print("legend says a lethal curse and its cure surround these very flowers")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
        
        if id == 24:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER THREE: SPENCER THE SPINO")
          print("")
          print("spencer is the local friendly spinosaurus")
          print("he is usually found sleeping, and posseses a wide range of emotion when hes awake")
          print("encountering him while hes hungry is extremely suboptimal")
          print("")
          print('"I WROTE THIS SENTENCE OF MY VERY OWN CHAPTER"- spencer')
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 25:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER FOUR: WISE THE TREE")
          print("")
          print("wise is a powerful judgmental tree")
          print("his domain seemingly moves from spot to spot around the forests")
          print("he can give great fortune, or deal 3 damage to every member of the witnessing party")
          print("some folks even report reciveing a legendary folknix")
          print("")
          print("you may avoid the tree once, but doing so again wont be so relieving")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 26:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER FIVE: NOAH + EVAN")
          print("")
          print("the dream duo")
          print("they might just say wsg bro to you")
          print("but together")
          print("a legend may be born")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 27:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER SIX: RIVERS")
          print("")
          print("rivers spread vastly among the valley")
          print("")
          print("important!:")
          print("a deep river you must float")
          print("a shallow river you must drive")
          print("it is wise to keep spare parts with you, as river beds are never consistant")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 28:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER SEVEN: GIVER")
          print("")
          print("a mythical legend")
          print("")
          print("a house may appear in front of the target")
          print("a deceptivly immense risk, with great reward and great faliure")
          print("")
          print("all reported info suggests to be careful what you say, and how you answer its game")
          print("additionally, if you take the great risk, dont stay for too long")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 29:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER EIGHT: BAYBAKI")
          print("")
          print("baybaki is a powerful trickster that loves to play games with his targets")
          print("he has a mysterious figure, and only appears on his own will")
          print("")
          print("his reported games include a relentless roulette with his gun")
          print("and his math test, and inflicts damage upon a incorrect or slow answer")
          print("")
          print("there are theories about his connection to the creature of the night, stan")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 210:
          print("\033[H\033[2J", end="")
          print("THE MYSTERIES OF FOLK VALLEY")
          print("CHAPTER NINE: MOUNTAIN")
          print("")
          print("the dire enviorment that sorts the worthy from the weak")
          print("additionaly, this is a mysterious subject, as some report a unavoidable mountain on the valley")
          print("and others report not encounting a mountain at all")
          print("")
          print("important notes:")
          print("- mining through the mountain is usually easier than going above the mountain")
          print("- NEVER INVESTIGATE THE CRIMSON TREE WITHOUT THE CRIMSON ROCK")
          print("- dont spend too much time in the town")
          print("- the princess has greed issues, and will submit to the gods say")
          print("- only attempt to move past the town or the tree, if you use the rock on the tree, or talk to the princess")
          print("")
          print("(1) back a page")
          print("(0) put book away")
      
      
        if id == 31:
          print("\033[H\033[2J", end="")
          print("HOW TO NOT SUCK AT BEING A LEADER")
          print("")
          print("TABLE OF CONTENTS")
          print("(1) orders")
          print("(2) practices")
          print("")
          print("(0) put book away")
      
        if id == 32:
          print("\033[H\033[2J", end="")
          print("HOW TO NOT SUCK AT BEING A LEADER")
          print("CHAPTER ONE: ORDERS")
          print("")
          print("there are different paces you may take through the valley")
          print("leasurly - normal - hasty")
          print("")
          print("leasurly is the slowest: traveling 20% slower than normal")
          print("while this pace is slow, this pace has many benifits")
          print(" - reduces disease chance (0.16% per tick -> 0.11% per tick")
          print(" - decreases stamina loss")
          print(" - gives a chance to find items while moving")
          print("(this is recommended when your situation is dire)")
          print("")
          print("hasty is the fastest: traveling 30% faster than normal")
          print("this pace is the fastest, yet brings other side effects")
          print(" - increases disease chance (0.16% per tick -> 0.33% per tick")
          print(" - increased stamina loss")
          print("(this is recommended when you are near the end, or safe on resources)")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 33:
          print("\033[H\033[2J", end="")
          print("HOW TO NOT SUCK AT BEING A LEADER")
          print("CHAPTER ONE: practices")
          print("")
          print("here are some of the best tips for the valley:")
          print(" - sleep when someone has a disease, as its best to rid all diseases as soon as possible")
          print(" - keep your folks alive, as dropping numbers increases stamina")
          print(" - rest every once in a while, its not good to go insane")
          print(" - keep everyone hungers above 50, as they can regenerate health above this hunger")
          print(" - sleep during the night, its much more effective for stamina gain than resting")
          print("(1) back a page")
          print("(0) put book away")
      
      
        if id == 41:
          print("\033[H\033[2J", end="")
          print("MYSTERIES OF FOLK VALLEY")
          print("")
          print("TABLE OF CONTENTS")
          print("(1) weapons")
          print("(2) consumables")
          print("(3) other")
          print("(4) nuke")
          print("")
          print("(0) put book away")
          
        if id == 42:
          print("\033[H\033[2J", end="")
          print("MYSTERIES OF FOLK VALLEY")
          print("CHAPTER ONE: WEAPONS")
          print("")
          print("FOLK SWORD")
          print("the close range menace, cheap and effective")
          print("the swords are much more effective at defending attacks")
          print("FOLK RAPIER")
          print("the upgraded version of the folk sword, unmatched in combat")
          print("there are many interaction that require this weapon")
          print("can take down the scariest beasts")
          print("")
          print("FOLK MUSKET")
          print("the easy, effective ranged weapon")
          print("the guns are much more effective at taking shots at targets from a distance, like hunting")
          print("FOLK RIFLE")
          print("the upgraded version of the folk musket, unmatched in combat")
          print("there are many interaction that require this weapon")
          print("extreme power and precision")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 43:
          print("\033[H\033[2J", end="")
          print("MYSTERIES OF FOLK VALLEY")
          print("CHAPTER TWO: CONSUMABLES")
          print("")
          print("FOOD:")
          print("FOLK FOOD")
          print("local specialty: cheap, simple, yummy")
          print("feeds one folk: 50 hunger")
          print("MOMS THANKSGIVING: questionable meal for everyone to share")
          print("feeds every folk: 20 hunger")
          print("")
          print("the difference between the two food is preference:")
          print("folk food is more worth the money, and comes in more quantity in case of losing food")
          print("moms meals are more consistant, giving each member food and preventing wasted food")
          print("")
          print("MEDICAL:")
          print("MEDI BEDI: the classic healing item of the valley")
          print("heals one folk 5 health")
          print("ANTIDOTE: base model / life saver")
          print("can combine with flowers to create a cure to diseases")
          print("rosavale: cures the floral curse")
          print("wyrmrose: cures all instances of umbrythia")
          print("slyphora: cures nyxoplasia") 
          print("velisara: cures virellosis") 
          print("luneblossom: can combine to cure every disease")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 44:
          print("\033[H\033[2J", end="")
          print("MYSTERIES OF FOLK VALLEY")
          print("CHAPTER THREE: OTHER")
          print("")
          print("TOOLS:")
          print("PICKAXE: ole reliable")
          print("when you need it, you're gonna wish you had it")
          print("")
          print("SPARE PARTS: as essential as food?")
          print("allows for the repair of your folkmobile")
          print("")
          print("COOL ITEMS:")
          print("FOLKNIX: straight out of the fables")
          print("revives a folk, puts revived folk on max stats")
          print("")
          print("FOLK CORP BEACON: holds wonders")
          print("use to get a random assortment of goodies, can explode (see giver info)")
          print("")
          print("STRANGE TOOTH: the mountains remains")
          print("can forge a legendary blade")
          print("")
          print("PINK FLOWER: blossoms hope into the dire")
          print("will cure the floral curse")
          print("")
          print("(1) back a page")
          print("(2) forward a page")
          print("(0) put book away")
      
        if id == 45:
          print("\033[H\033[2J", end="")
          print("MYSTERIES OF FOLK VALLEY")
          print("CHAPTER FOUR: NUKE")
          print("")
          print("dont buy the nuke")
          print("")
          print("(1) back a page")
          print("(0) put book away")
        
      
        if id == 51:
          print("\033[H\033[2J", end="")
          print("my name is tim, this is my book")
          print("")
          print("(0) put book away")
          
      def foodstore ():
        menuinput = 1
        print("\033[H\033[2J", end="")
        print("hi im bob the food folk wat food u want")
        print("(1) folkfood (feeds 50 to one person): 2 george")
        print("(2) moms thanksgiving meal (feeds 20 to everyone): 4 george")
        print("(3) medibedi (heals one folk for 5 health): 5 george")
        print("(4) im out (back)")
      
      def weaponstore():
        print("\033[H\033[2J", end="")
        print("hi im mili!! please buy something!!!")
        print("(1) folksword (may protect all folks from physical encounters, but can break): 10 george")
        print("(2) folkmusket (like the sword but for ranged encounters): 10 george")
        print("(3) nuke: 100 george")
        print("(4) ammo (required for gun): 1 george for 5 bullets")
        print("(5) im out (back)")
      
      def inventory():
        print("\033[H\033[2J", end="")
        print("you have:")
        print("folk food:", folkfood)
        print("moms thanksgiving meal:", momsmeal)
        print("medibedi:", medibedi)
        print("folk sword:", folksword)
        print("folkmusket:", folkmusket)
        print("ammo:", ammo)
        print("nuke:", nuke)
        print("spare parts:", parts)
        print("antidote:", antidote)
        print("pickaxe:", pickaxe)
        print("")
        print("type 1 to go back")
      
      def otherstore():
        print("\033[H\033[2J", end="")
        print("tim want money")
        print("(1) spare parts (general useful parts for your folkmobile): 2 george")
        print("(2) antidote (required for creating cures): 3 george")
        print("(3) pickaxe: 4 george")
        print("(4) im out (back)")
        
      #packing stage (folk chamber)
      menuinput = "0"

  
      startgeorge = 150 - ((difficulty - 1) * 30)
      george = startgeorge
        
      
      while menuinput != 1 and savecontinue == 0:
        menu()
        menuinput = input("")
      
        #vv ts library
        while menuinput == "0":
          print("\033[H\033[2J", end="")
          if libhallskip == 0:
            print("you move past the shops, through a hallway")
            time.sleep(textspeed)
            print('the end of the hallway presents a pristine wood door, with a sign reading "library"')
            time.sleep(textspeed)
            #print("there is also a small scratched up crooked door to the side")
            #time.sleep(textspeed)
            libhallskip = 1
          print("(1) enter library (recommended for beginners)")
         # print("(2) enter crooked door")
      
          shortinput3 = input("")
      
          while shortinput3 == "1":
            library()
            shortinput = input("")
            
            if shortinput == "1":
              bookid = 11
            while shortinput == "1":
              while bookid == 11:
                books(11)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 12
                if shortinput2 == "2": bookid = 13
                if shortinput2 == "3": bookid = 14
                if shortinput2 == "0": 
                  bookid = 0
                  shortinput = 0
              while bookid == 12:
                books(12)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 11
                if shortinput2 == "2": bookid = 13
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 13:
                books(13)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 12
                if shortinput2 == "2": bookid = 14
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 14:
                books(14)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 13
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
      
            if shortinput == "2":
              bookid = 21
            while shortinput == "2":
              while bookid == 21:
                books(21)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 22
                if shortinput2 == "2": bookid = 23
                if shortinput2 == "3": bookid = 24
                if shortinput2 == "4": bookid = 25
                if shortinput2 == "5": bookid = 26
                if shortinput2 == "6": bookid = 27
                if shortinput2 == "7": bookid = 28
                if shortinput2 == "8": bookid = 29
                if shortinput2 == "9": bookid = 210
                if shortinput2 == "0": 
                  bookid = 0
                  shortinput = 0
              while bookid == 22:
                books(22)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 21
                if shortinput2 == "2": bookid = 23
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 23:
                books(23)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 22
                if shortinput2 == "2": bookid = 24
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 24:
                books(24)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 23
                if shortinput2 == "2": bookid = 25
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 25:
                books(25)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 24
                if shortinput2 == "2": bookid = 26
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 26:
                books(26)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 25
                if shortinput2 == "2": bookid = 27
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 27:
                books(27)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 26
                if shortinput2 == "2": bookid = 28
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 28:
                books(28)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 27
                if shortinput2 == "2": bookid = 29
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 29:
                books(29)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 28
                if shortinput2 == "2": bookid = 210
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 210:
                books(210)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 29
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0 
      
            if shortinput == "3":
              bookid = 31
            while shortinput == "3":
              while bookid == 31:
                books(31)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 32
                if shortinput2 == "2": bookid = 33
                if shortinput2 == "0": 
                  bookid = 0
                  shortinput = 0
              while bookid == 32:
                books(32)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 31
                if shortinput2 == "2": bookid = 33
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 33:
                books(33)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 32
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
      
            if shortinput == "4":
              bookid = 41
            while shortinput == "4":
              while bookid == 41:
                books(41)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 42
                if shortinput2 == "2": bookid = 43
                if shortinput2 == "3": bookid = 44
                if shortinput2 == "4": bookid = 45
                if shortinput2 == "0": 
                  bookid = 0
                  shortinput = 0
              while bookid == 42:
                books(42)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 41
                if shortinput2 == "2": bookid = 43
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 43:
                books(43)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 42
                if shortinput2 == "2": bookid = 44
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0       
              while bookid == 44:
                books(44)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 43
                if shortinput2 == "2": bookid = 45
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
              while bookid == 45:
                books(45)
                shortinput2 = input("")
                if shortinput2 == "1": bookid = 44
                if shortinput2 == "0":
                  bookid = 0
                  shortinput = 0
      
            if shortinput == "5":
              bookid = 51
            while shortinput == "5":
              while bookid == 51:
                books(51)
                shortinput2 = input("")
                if shortinput2 == "0": 
                  bookid = 0
                  shortinput = 0
      
            if shortinput == "6":
              shortinput3 = 0
              menuinput = 0
              
        #vv bobs food store vv
        while menuinput == "1" and not active_expansion // 10 == 4:
          shortinput = ""
          foodstore()
          shortinput = input("")
          
          #vv folkfood vv
          while shortinput == "1":
            print("how much folkfood u want (type a number)")
            print("george balance:", george)
            shortintinput = input()
            
          #check if bob is getting scammed 
            shortintinput = int(shortintinput)
            george = george - shortintinput*2  
          
            if george < 0:
              print("you are to broke lol")
              george = george + shortintinput*2            
            else:
              folkfood = folkfood + shortintinput
              print("you bought", shortintinput, "folkfood")
              time.sleep(1)
              shortintinput = 0
              shortinput = 0
                      
          #vv mums meals vv
          while shortinput == "2":
            print("how much of mums meals u want (type a number)")
            print("george balance:", george)
            shortintinput = input()
            #check if bob is getting scammed 
            shortintinput = int(shortintinput)
            george = george - shortintinput*4
            if george < 0:
              print("you are to broke lol")
              george = george + shortintinput*4
              
            else:
              momsmeal = momsmeal + shortintinput
              print("you bought", shortintinput, "of mums meals")
              time.sleep(1)
              shortintinput = 0
              shortinput = 0
      
          #vv medibedi vv
          while shortinput == "3":
            print("how much of medibedis u want (type a number)")
            print("george balance:", george)
            shortintinput = input()
            #check if bob is getting scammed 
            shortintinput = int(shortintinput)
            george = george - shortintinput*5
            if george < 0:
              print("you are to broke lol")
              george = george + shortintinput*5
              
            else:
              medibedi = medibedi + shortintinput
              print("you bought", shortintinput, "medibedi(s)")
              time.sleep(1)
              shortintinput = 0
              shortinput = 0
      
          #vv back command
          if  shortinput == "4":
            print ("bye bye")
            time.sleep(2)
            menuinput = "0"
            shortinput = 0
      
        #vv mili's weapon store vv
        while menuinput == "2":
          shortinput = ""
          weaponstore()
          shortinput = input("")
          
          #vv folksword vv
          while shortinput == "1":
              print("how many folkswords u want! (type a number)")
              print("george balance:", george)
              shortintinput = input()
              
            #check if mili is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*10 
            
              if george < 0:
                print("u dont have enough money for that :c")
                george = george + shortintinput*10           
              else:
                folksword = folksword + shortintinput
                print("you bought", shortintinput, "folkswords! ty!!!!11!")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
                      
          #vv folkmusket vv
          while shortinput == "2":
              print("how many folkmuskets u want! (type a number)")
              print("george balance:", george)
              shortintinput = input()
              #check if mili is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*10
              if george < 0:
                print("u dont have enough money for that :c")
                george = george + shortintinput*10
                
              else:
                folkmusket = folkmusket + shortintinput
                print("you bought", shortintinput, "folkmuskets! ty!!!!11!")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
                
          #vv nuke... vv
          while shortinput == "3":
              print("how many nukes do u want! (type a number)")
              print("george balance:", george)
              shortintinput = input()
              #check if mili is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*100
              if george < 0:
                print("u dont have enough money for that :c")
                george = george + shortintinput*100
                
              else:
                nuke = nuke + shortintinput
                print("you bought", shortintinput, "nukes! ty!!!!11!")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
          
          #vv ammo... vv
          while shortinput == "4":
              print("how much rounds (5 ammo, 1 george) u want! (type a number)")
              print("george balance:", george)
              shortintinput = input()
              #check if mili is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput
              if george < 0:
                print("u dont have enough money for that :c")
                george = george + shortintinput
                
              else:
                ammo = ammo + shortintinput*5
                print("you bought", shortintinput, "rounds! ty!!!!11!")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
      
          #vv back command
          if  shortinput == "5":
            print ("byeee")
            time.sleep(2)
            menuinput = "0"
            shortinput = 0
      
        #vv tims's store vv
        while menuinput == "3":
          shortinput = ""
          otherstore()
          shortinput = input("")
          
          #vv parts vv
          while shortinput == "1":
              print("how many part (type a number)")
              print("george balance:", george)
              shortintinput = input()
              
            #check if tim is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*2
            
              if george < 0:
                print("no money")
                george = george + shortintinput*2           
              else:
                parts = parts + shortintinput
                print("bought", shortintinput, "part")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
                      
          #vv antidote vv
          while shortinput == "2":
              print("how many antidote (type a number)")
              print("george balance:", george)
              shortintinput = input()
              #check if tim is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*3
              if george < 0:
                print("no money")
                george = george + shortintinput*3
                
              else:
                antidote = antidote + shortintinput
                print("bought", shortintinput, "antidote")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
      
          #vv pickaxe
          while shortinput == "3":
              print("how many pickaxe (type a number)")
              print("george balance:", george)
              shortintinput = input()
              #check if tim is getting scammed 
              shortintinput = int(shortintinput)
              george = george - shortintinput*4
              if george < 0:
                print("no money")
                george = george + shortintinput*4
                
              else:
                pickaxe = pickaxe + shortintinput
                print("bought", shortintinput, "pickaxe")
                time.sleep(1)
                shortintinput = 0
                shortinput = 0
              
      
          #vv back command
          if  shortinput == "4":
            print ("...")
            time.sleep(2)
            menuinput = "0"
            shortinput = 0
      
        #vv inventory vv
        while menuinput == "4":
          inventory ()
          shortinput = ""
          shortinput = input("")   
          if shortinput == "1":
            shortinput = 0
            menuinput = "0"
          else:
            print("bro had one job")
            time.sleep(1)
      
        #vv the entrance.... vv
        while menuinput == "5":
          print("\033[H\033[2J", end="")
          print("entering the valley....")
          time.sleep(3)
          menuinput = 1
          print("\033[H\033[2J", end="")
      
        #vv presets vv
        while menuinput == "6":
          presetcheck()
          print(pres1status, pres2status, pres3status)
          print("\033[H\033[2J", end="")
          print("shop presets save what you buy, and lets you purchase the same itema again")
          if george == startgeorge:
            print("come back when you have bought something")
            print("(0) back")
            if pres1status == 1 or pres2status == 1 or pres3status == 1:
              print("(2) load a preset")
         
          else:
            print("would you like to create a preset")
            print("(0) back")
            print("(1) continue")
            if pres1status == 1 or pres2status == 1 or pres3status == 1:
              print("(2) load a preset")
            
          shortinput = input("")
          while shortinput == "1":
            print("\033[H\033[2J", end="")
            print("what slot would you like save to (slot 1, slot 2, slot 3)")
            shortinput2 = input("")
            if shortinput2 != "1" and shortinput2 != "2" and shortinput2 != "3":
              print("that wasnt a option silly!")
              time.sleep(1)
            else:
              if shortinput2 == "1" and pres1status == 1:
                print("are you sure you want to overwrite this slot (type 1 to confirm)")
                shortinput3 = input("")
                if shortinput3 != "1":
                  continue
                  
              if shortinput2 == "2" and pres2status == 1:
                print("are you sure you want to overwrite this slot (type 1 to confirm)")
                shortinput3 = input("")
                if shortinput3 != "1":
                  continue
                  
              if shortinput2 == "3" and pres3status == 1:
                print("are you sure you want to overwrite this slot (type 1 to confirm)")
                shortinput3 = input("")
                if shortinput3 != "1":
                  continue
                  
              print("what would you like to name your preset?")
              shortinput3 = input("")
              savepreset(shortinput2, shortinput3)
              print("saved!")
              time.sleep(1)
              menuinput = 0
              break
      
          while shortinput == "2":
            print("\033[H\033[2J", end="")
            print("which preset would you like to load?")
            print("")
            print("(0) back")
            if pres1status == 1:
              print("")
              print("(1) preset 1:", (getline("preset1.csv", 10)).strip())
              print("total george:", (getline("preset1.csv", 9)).strip())
            if pres2status == 1:
              print("")
              print("(2) preset 2:", (getline("preset2.csv", 10)).strip())
              print("total george:", (getline("preset2.csv", 9)).strip())
            if pres3status == 1:
              print("")
              print("(3) preset 3:", (getline("preset3.csv", 10)).strip())
              print("total george:", (getline("preset3.csv", 9)).strip())
      
            shortinput2 = input("")
            if shortinput2 == "1" and pres1status == 1:
              totgeorge = int(float(getline("preset1.csv", 9).strip()))
              if george - totgeorge < 0:
                print("you cannot afford this preset!")
                time.sleep(2)
              else:
                george -= totgeorge
                folkfood += int(float(getline("preset1.csv", 1).strip()))
                momsmeal += int(float(getline("preset1.csv", 2).strip()))
                folkmusket += int(float(getline("preset1.csv", 3).strip()))
                folksword += int(float(getline("preset1.csv", 4).strip()))
                ammo += int(float(getline("preset1.csv", 5).strip()))
                parts += int(float(getline("preset1.csv", 6).strip()))
                pickaxe += int(float(getline("preset1.csv", 7).strip()))
                medibedi += int(float(getline("preset1.csv", 8).strip()))
                print("transaction complete!")
                time.sleep(1)
                menuinput = 0
                break
      
            if shortinput2 == "2" and pres2status == 1:
              totgeorge = int(float(getline("preset2.csv", 9).strip()))
              if george - totgeorge < 0:
                print("you cannot afford this preset!")
                time.sleep(2)
              else:
                george -= totgeorge
                folkfood += int(float(getline("preset2.csv", 1).strip()))
                momsmeal += int(float(getline("preset2.csv", 2).strip()))
                folkmusket += int(float(getline("preset2.csv", 3).strip()))
                folksword += int(float(getline("preset2.csv", 4).strip()))
                ammo += int(float(getline("preset2.csv", 5).strip()))
                parts += int(float(getline("preset2.csv", 6).strip()))
                pickaxe += int(float(getline("preset2.csv", 7).strip()))
                medibedi += int(float(getline("preset2.csv", 8).strip()))
                print("transaction complete!")
                time.sleep(1)
                menuinput = 0
                break
      
            if shortinput2 == "3" and pres3status == 1:
              totgeorge = int(float(getline("preset3.csv", 9).strip()))
              if george - totgeorge < 0:
                print("you cannot afford this preset!")
                time.sleep(2)
              else:
                george -= totgeorge
                folkfood += int(float(getline("preset3.csv", 1).strip()))
                momsmeal += int(float(getline("preset3.csv", 2).strip()))
                folkmusket += int(float(getline("preset3.csv", 3).strip()))
                folksword += int(float(getline("preset3.csv", 4).strip()))
                ammo += int(float(getline("preset3.csv", 5).strip()))
                parts += int(float(getline("preset3.csv", 6).strip()))
                pickaxe += int(float(getline("preset3.csv", 7).strip()))
                medibedi += int(float(getline("preset3.csv", 8).strip()))
                print("transaction complete!")
                time.sleep(1)
                menuinput = 0
                break
                
            if shortinput2 == "0":
              menuinput = 0
              break
          if shortinput == "0":
            menuinput = 0
        
      """
      //////////////////////////////////////////////////////////////////////^PREPPHASE^//////////////////////////////////////////////////////////////////////////////////
      """
      def gameinventory():
        print("\033[H\033[2J", end="")
        print("you have:")
        print("(1) folk food:", folkfood)
        print("(2) moms thanksgiving meal:", momsmeal)
        print("(3) medibedi:", medibedi)
        if chillmeat > 0:
          print("(4) chilled meat:", chillmeat)
        print("folk sword:", folksword)
        print("folkmusket:", folkmusket)
        print("ammo:", ammo)
        print("antidote:", antidote)
        #print("(-) lottery ticket:", ticket)
        print("press button to feed you and your folks")
        print("press 0 to go back")
        print("press 9 to enter special inventory")

      def specialinventory():
        print("\033[H\033[2J", end="")
        if gluttonyitem > 0 or wrathitem > 0 or prideitem > 0 or greeditem > 0 or lustitem > 0 or envyitem > 0 or slothitem > 0:
          print(f"{color.pink}(sin) enter sin bag")
          print("")
        if rosavale > 0 or wyrmrose > 0 or slyphora > 0 or velisara > 0 or luneblossom > 0:
          print(f"{color.bgreen}(flower) enter flower bag")
          print("")
        if folknix > 0:
          print(f"{color.bred}(folknix) folknix:", folknix)
          print("")
        if folkcorpbeacon > 0:
          print(f"{color.white}(beacon) folk corp beacon:", math.ceil(folkcorpbeacon / 2))
          print("")
        if terminus > 0:
          print(f"{color.red}(term) terminus:", terminus)
          print("")
        if tooth > 0:
          print(f"{color.blue}(tooth) strange tooth:", tooth)
          print("")
        if meteor > 0:
          print(f"{color.pink}(meteor) meteoric rock:", meteor)
          print("")
        print(f"{color.white}")

      def flowerbag():
        """
        rosavale = 0
        wyrmrose = 0
        slyphora = 0
        velisara = 0
        luneblossom = 0
        """
        print("\033[H\033[2J", end="")
        print("flower bag:")
        if rosavale > 0:
          print(f"{color.bpink}rosavale:", rosavale)
          print("")

        if slyphora > 0:
          print(f"{color.yellow}slyphora:", slyphora)
          print("")
        
        if wyrmrose > 0:
          print(f"{color.pink}wyrmrose:", wyrmrose)
          print("")

        if velisara > 0:
          print(f"{color.green}velisara:", velisara)
          print("")

        if luneblossom > 0:
          print(f"{color.bblue}luneblossom:", luneblossom)
          print("")

        print(f"{color.white}antidotes:", antidote)
        print("")

        if s1 != 0:
          if s1 == 1:
            print(f"{color.bpink}SLOT 1: (rosa) rosacura (can cure floral curse){color.white}")
          if s1 == 2:
            print(f"{color.yellow}SLOT 1: (sly) slycura (can cure nyxoplasia){color.white}")
          if s1 == 3:
            print(f"{color.pink}SLOT 1: (wyrm) wyrmcura (can cure umbrythia){color.white}")
          if s1 == 4:
            print(f"{color.green}SLOT 1: (veli) velicura (can cure virellosis){color.white}")
          if s1 == 5:
            print(f"{color.bblue}SLOT 1: (lune) lunecura (can cure anything){color.white}")

        if s2 != 0:
          if s2 == 1:
            print(f"{color.bpink}SLOT 2: (rosa) rosacura (can cure floral curse){color.white}")
          if s2 == 2:
            print(f"{color.yellow}SLOT 2: (sly) slycura (can cure nyxoplasia){color.white}")
          if s2 == 3:
            print(f"{color.pink}SLOT 2: (wyrm) wyrmcura (can cure umbrythia){color.white}")
          if s2 == 4:
            print(f"{color.green}SLOT 2: (veli) velicura (can cure virellosis){color.white}")
          if s2 == 5:
            print(f"{color.bblue}SLOT 2: (lune) lunecura (can cure anything){color.white}")

        if s3 != 0:
          if s3 == 1:
            print(f"{color.bpink}SLOT 3: (rosa) rosacura (can cure floral curse){color.white}")
          if s3 == 2:
            print(f"{color.yellow}SLOT 3: (sly) slycura (can cure nyxoplasia){color.white}")
          if s3 == 3:
            print(f"{color.pink}SLOT 3: (wyrm) wyrmcura (can cure umbrythia){color.white}")
          if s3 == 4:
            print(f"{color.green}SLOT 3: (veli) velicura (can cure virellosis){color.white}")
          if s3 == 5:
            print(f"{color.bblue}SLOT 3: (lune) lunecura (can cure anything){color.white}")
          
        print("")
        print("0 to go back")
        print("1 to create mixture!")
          
      def sinbag():
        """
        gluttonyitem = 0
        wrathitem = 0
        prideitem = 0
        greeditem = 0
        lustitem = 0
        envyitem = 0
        slothitem = 0
        """
        print("\033[H\033[2J", end="")
        print("sin bag:")
        if gluttonyitem > 0:
          print(f"{color.bred}(glut) gluttony:", gluttonyitem)
          print("")

        if wrathitem > 0:
          print(f"{color.red}(wrath) wrath:", wrathitem)
          print("")
        
        if prideitem > 0:
          print(f"{color.yellow}(pride) pride:", prideitem)
          print("")

        if greeditem > 0:
          print(f"{color.bgreen}(greed) greed:", greeditem)
          print("")

        if lustitem > 0:
          print(f"{color.bpink}(lust) lust:", lustitem)
          print("")
          
        if envyitem > 0:
          print(f"{color.bblue}(envy) envy:", envyitem)
          print("")

        if slothitem > 0:
          print(f"{color.green}(sloth) sloth:", slothitem)
          print("")
          
        print("")
        print(f"{color.white} 0 to go back")
      
      def deathscreen(reason):
        global lincoln
        global runactive
        global shortinput
        
        time.sleep(textspeed)
        print("\033[H\033[2J", end="")
        print("YOU HAVE DIED")
        print("you died to:", reason)
        
        save = open("savedata.csv", "w")
        save.close()
        
        print("lincoln gain:", ((score // 10) * ((difficulty) * 0.5)))
        lincoln += ((score // 10) * ((difficulty) * 0.5))
        print("")
        print("total lincoln:", lincoln)
        print("press anything to continue")
        shortinput = input("")
        
        file = open("fv.dat", "w")
        file.write(str(lincoln))
        file.close()
        
        runactive = 0
        raise endrun  
        
      def charstatus():
        print("\033[H\033[2J", end="")
        print("george balance =", george)
        
        print(bandname, "stats:")
      
        print("")
        print(playername, "stats:")
        print("health:", playerhealth)
        print("hunger:", math.ceil(playerhunger))
        print("stamina:", math.ceil(playerstamina))
      
        if f1health > 0:
          print("")
          print(folk1name, "stats:")
          print("health:", f1health)
          print("hunger:", math.ceil(f1hunger))
          print("stamina:", math.ceil(f1stamina))
        
        if f2health > 0:
          print("")
          print(folk2name, "stats:")
          print("health:", f2health)
          print("hunger:", math.ceil(f2hunger))
          print("stamina:", math.ceil(f2stamina))
      
        if f3health > 0:
          print("")
          print(folk3name, "stats:")
          print("health:", f3health)
          print("hunger:", math.ceil(f3hunger))
          print("stamina:", math.ceil(f3stamina))
        
        print("")
          
        if f1health <= 0:
          print(folk1name, "is dead")
        if f2health <= 0:
          print(folk2name, "is dead")
        if f3health <= 0:
          print(folk3name, "is dead")
        if fcplayer == 1:
          print(playername, "has floral curse!")
        if f1health > 0 and fcfolk1 == 1:
          print(folk1name, "has floral curse!")
        if f2health > 0 and fcfolk2 == 1:
          print(folk2name, "has floral curse!")
        if f3health > 0 and fcfolk3 == 1:
          print(folk3name, "has floral curse!")
        if playerdis >= 1 and playerhealth > 0:
          print("")
          if playerdis == 2:
            print(f"{color.green}{playername} disease is mutated!{color.white}")
          if nyxoplasiaID // 10 == 1:
            print(playername, "has stage", nyxoplasiaID % 10, "nyxoplasia")
          if virellosisID // 10 == 1:
            print(playername, "has stage", virellosisID % 10, "virellosis")
          if umbrythiaID // 10 == 1:
            print(playername, "has stage", umbrythiaID % 10, "umbrythia")
        if folk1dis >= 1 and f1health > 0:
          print("")
          if folk1dis == 2:
            print(f"{color.green}{folk1name} disease is mutated!{color.white}")
          if nyxoplasiaID // 10 == 2:
            print(folk1name, "has stage", nyxoplasiaID % 10, "nyxoplasia")
          if virellosisID // 10 == 2:
            print(folk1name, "has stage", virellosisID % 10, "virellosis")
          if umbrythiaID // 10 == 2:
            print(folk1name, "has stage", umbrythiaID % 10, "umbrythia")
        if folk2dis >= 1 and f2health > 0:
          print("")
          if folk2dis == 2:
            print(f"{color.green}{folk2name} disease is mutated!{color.white}")
          if nyxoplasiaID // 10 == 3:
            print(folk2name, "has stage", nyxoplasiaID % 10, "nyxoplasia")
          if virellosisID // 10 == 3:
            print(folk2name, "has stage", virellosisID % 10, "virellosis")
          if umbrythiaID // 10 == 3:
            print(folk2name, "has stage", umbrythiaID % 10, "umbrythia")
        if folk3dis >= 1 and f3health > 0:
          print("")
          if folk3dis == 2:
            print(f"{color.green}{folk3name} disease is mutated!{color.white}")
          if nyxoplasiaID // 10 == 4:
            print(folk3name, "has stage", nyxoplasiaID % 10, "nyxoplasia")
          if virellosisID // 10 == 4:
            print(folk3name, "has stage", virellosisID % 10, "virellosis")
          if umbrythiaID // 10 == 4:
            print(folk3name, "has stage", umbrythiaID % 10, "umbrythia")
        print("")
        print("(0) back")
      
      def fixnum():
        global playerstamina
        global f1stamina
        global f2stamina
        global f3stamina
        global f1health
        global f2health
        global f3health
        global playerhunger
        global f1hunger
        global f2hunger
        global f3hunger
      
        if playerstamina < 0.1:
          playerstamina = 0
        if playerhunger < 0.1:
          playerhunger = 0
      
        if f1stamina < 0.1:
          f1stamina = 0
        if f2stamina < 0.1:
          f2stamina = 0
        if f3stamina < 0.1:
          f3stamina = 0
      
        if f1hunger < 0.1:
          f1hunger = 0
        if f2hunger < 0.1:
          f2hunger = 0
        if f3hunger < 0.1:
          f3hunger = 0
      
        if f1health < 0.1:
          f1health = 0
        if f2health < 0.1:
          f2health = 0
        if f3health < 0.1:
          f3health = 0
      
      def eventroll():
        global timehr
        global event
        global eventname
        global previousevent
        global eventrolls
        global manueventcd
        evrollmax = 300 - (25 * (difficulty - 1))
        
        shortrandom = random.randint(0,evrollmax)
        
        while shortrandom in eventrolls:
          shortrandom = random.randint(0,evrollmax)
        
        if shortrandom == 1:
          eventrolls = []
          #event
          event = random.randint(0,18)
          timehr = int(timehr)
          
          while (timehr < 20 and timehr > 5 and event == 14 or event == 12) or (happydino ==  1 and event == 11) or ((event == 11 or event == 2 or event == 4) and deaddino == 1) or (event == 5 and deadtree == 1) or (event == 17 and NOmountain == 1) or (event == 18 and baybakidead == 1) or (event == previousevent):
            event = random.randint(0,18)
            
          if debugmode == 1:
            print("\033[H\033[2J", end="")
            for val in eventlist: print(val)
            event = int(input("event id?"))
            if event == 99:
              event = random.randint(0,18)
            if event == -99:
              return 0

          while manueventcd == 0 and active_expansion // 10 == 3:
            print("\033[H\033[2J", end="")
            print("manipulation expansion bonus!")
            print("what event would you like? (enter num)")
            print("enter 'help' to view list of ids")

            shortinput = input("")

            if shortinput == "help":
              iter = 0
              for val in eventlist:
                print(f"{iter}:{val}")
                iter += 1
              print("press 0 to go back")
              shortinput = input("")

            else:
              try: int(shortinput)
              except ValueError:
                print("that is not a valid id!")
                time.sleep(1)
              except IndexError:
                print("that isnt a value")
                time.sleep(1)
              else:
                event = int(shortinput)
                manueventcd += 288
                if active_expansion == 22 or active_expansion == 23:
                  manueventcd -= 144
          eventname = eventlist[event]
          previousevent = event
          return 1
        else:
          eventrolls.append(shortrandom)
          return 0
      
      def restevent():
        global playerhealth
        global f1health
        global f2health
        global f3health
        global shortrandom
        global shortinput
        global folkfood
        global momsmeal
        global ammo
        global medibedi
        global rosavale
        global slyphora
        global wyrmrose
        global velisara
        global luneblossom
        global folkrapier
        global folkrifle
        global pickaxe
        global parts
        if sleepmode == 2:
          if (int(timehr) < 20 and int(timehr) > 5) or (active_expansion // 10 == 1):
            shortrandom = random.randint(1,50)
            if shortrandom == 1:
              shortrandom = random.randint(1,5)
              if folkcount != 0:
                shortrandom = random.randint(2,10)
      
              #chest
              if shortrandom < 5: 
                print("\033[H\033[2J", end="")
                print("you found a nearby chest!")
                print("(1) open!")
                shortinput = input("")
                shortrandom = random.randint(1,20)
                #legendary!
                if shortrandom == 1:
                  shortrandom = random.randint(1,2)
                  if shortrandom == 1:
                    print("you got a folk rapier")
                    time.sleep(textspeed)
                    folkrapier += 1
                  if shortrandom == 2:
                    print("you got a folk rifle")
                    time.sleep(textspeed)
                    folkrifle += 1
                #rare
                elif shortrandom > 1 and shortrandom < 5:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1:
                    print("you got a pickaxe")
                    time.sleep(textspeed)
                    pickaxe += 1
                  if shortrandom == 2:
                    print("you got 3 medibedis!")
                    time.sleep(textspeed)
                    medibedi += 3
                  if shortrandom == 3:
                    print("you got 4 folkfood!")
                    time.sleep(textspeed)
                    folkfood += 4
                #uncommon
                elif shortrandom > 4 and shortrandom < 11:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1:
                    shortrandom = random.randint(1,5)
                    if shortrandom == 1:
                      rosavale += 1
                      print("you got a rosavale")
                    if shortrandom == 2:
                      slyphora += 1
                      print("you got a slyphora")
                    if shortrandom == 3:
                      wyrmrose += 1
                      print("you got a wyrmrose")
                    if shortrandom == 4:
                      velisara += 1
                      print("you got a velisara")
                    if shortrandom == 5:
                      luneblossom += 1
                      manuroll(17)
                      print("you got a luneblossom")
                    time.sleep(textspeed)
                  elif shortrandom == 2:
                    print("you got 2 medibedis!")
                    time.sleep(textspeed)
                    medibedi += 2
                  elif shortrandom == 3:
                    print("you got 4 ammo!")
                    time.sleep(textspeed)
                    ammo += 4
                #common
                else:
                  shortrandom = random.randint(1,2)
                  if shortrandom == 1:
                    print("you got two folkfood")
                    time.sleep(textspeed)
                    folkfood += 2
                  if shortrandom == 2:
                    print("you got one moms thankgiving meal")
                    time.sleep(textspeed)
                    momsmeal += 2
      
              elif shortrandom < 7:
                shortrandom = random.randint(1,5)
                if shortrandom == 1:
                  rosavale += 1
                  print("you search the woods and find a rosavale and 2 medibedis")
                if shortrandom == 2:
                  slyphora += 1
                  print("you search the woods and find a slyphora and 2 medibedis")
                if shortrandom == 3:
                  wyrmrose += 1
                  print("you search the woods and find a wyrmrose and 2 medibedis")
                if shortrandom == 4:
                  velisara += 1
                  print("you search the woods and find a velisara and 2 medibedis")
                if shortrandom == 5:
                  luneblossom += 1
                  manuroll(17)
                  print("you search the woods and find a luneblossom and 2 medibedis")
                time.sleep(textspeed)
                medibedi += 2
      
              elif shortrandom < 8:
                print("your folks dig up something!")
                time.sleep(textspeed)
                shortrandom = random.randint(1,4)
                if shortrandom == 1:
                  print("they dug up 2 parts!")
                  time.sleep(textspeed)
                  parts += 2
                if shortrandom == 2:
                  print("they dug up a moms thankgiving meal!")
                  time.sleep(textspeed)
                  momsmeal += 1
                if shortrandom == 3:
                  print("they dug up a skull, ew...")
                  time.sleep(textspeed)
                if shortrandom == 4:
                  print("they dug up a angry spider, owch!")
                  time.sleep(textspeed)
                  f1health -= 1
                  f2health -= 1
                  f3health -= 1
      
              else: 
                print("you and your folks found a patch of flowers!")
                time.sleep(textspeed)
                shortrandom = random.randint(1,5)
                if shortrandom == 1:
                  rosavale += 1
                  print("you feel better and even pick a rosavale!")
                if shortrandom == 2:
                  slyphora += 1
                  print("you feel better and even pick a slyphora!")
                if shortrandom == 3:
                  wyrmrose += 1
                  print("you feel better and even pick a wyrmrose!")
                if shortrandom == 4:
                  velisara += 1
                  print("you feel better and even pick a velisara!")
                if shortrandom == 5:
                  luneblossom += 1
                  manuroll(17)
                  print("you feel better and even pick a luneblossom!")
                
                time.sleep(textspeed)
                playerhealth += 2
                if f1health != 0: f1health += 2
                if f2health != 0: f2health += 2
                if f3health != 0: f3health += 2
                rosavale += 1
      
          else:
            shortrandom = random.randint(1,50)
            if shortrandom == 1:
              shortrandom = random.randint(1,5)
              if shortrandom == 1:
                print("you find a small lit up shed")
                time.sleep(textspeed)
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,5)
                  if shortrandom == 1:
                    rosavale += 1
                    print("you found a rosavale")
                  if shortrandom == 2:
                    slyphora += 1
                    print("you found a slyphora")
                  if shortrandom == 3:
                    wyrmrose += 1
                    print("you found a wyrmrose")
                  if shortrandom == 4:
                    velisara += 1
                    print("you found a velisara")
                  if shortrandom == 5:
                    luneblossom += 1
                    manuroll(17)
                    print("you found a luneblossom")
                  time.sleep(textspeed)
                if shortrandom == 2:
                  print("you got 2 medibedis!")
                  time.sleep(textspeed)
                  medibedi += 2
                if shortrandom == 3:
                  print("you got 4 ammo!")
                  time.sleep(textspeed)
            
              
      
        else:
          pass  

      def vengeancekill(target):
        global maxhp 
        global playerhealth
        
        if folksword >= 1 or folkrapier >= 1:
          print("\033[H\033[2J", end="")
          
          if target == "spino":
            if vrep >= 3:
              shortrandom = random.randint(4,8)
            else:
              shortrandom = random.randint(vrep, 5)
              
            if shortrandom >= 5:
              print("you ready your blade")
              time.sleep(textspeed)
              print("one stab into the core of his body... he whimpers")
              time.sleep(textspeed)
              print("you extract the sword, spencer left on the ground in shock, yet still breathing")
              time.sleep(textspeed)
              print("you feel great")
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("your stab was caught in the teeth of the spino, he spits your sword out")
              time.sleep(textspeed)
              print('"MEANIE!" spencer runs off...')
              time.sleep(textspeed)
              print("you are injured and in distaught")
              time.sleep(textspeed)
              playerhealth -= 5 
              if playerhealth <= 0: 
                deathscreen("spencer (obtain 30 or more reputation)")
                
          if target == "mili":
            if vrep >= 20:
              shortrandom = random.randint(20,30)
            else:
              shortrandom = random.randint(vrep, 25)
              
            if shortrandom >= 25:
              print("you ready your blade")
              time.sleep(textspeed)
              print("one stab into her chest... she is left in shock")
              time.sleep(textspeed)
              print("she takes the sword out herself, stares at the blade")
              time.sleep(textspeed)
              print('"you continue to suprise me"')
              time.sleep(textspeed)
              print("she drops your sword and walks into the darkness")
              time.sleep(textspeed)
              maxhp += 10
              playerhealth += 19
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("you attempt stab the blade, but is blocked by a hand from the darkness")
              time.sleep(textspeed)
              print('"how disappointing, this is how you act after all ive done for you"')
              time.sleep(textspeed)
              print("she holds you up with mysterious force")
              time.sleep(textspeed)
              print('"see you soon',playername,'"')
              time.sleep(textspeed)
              deathscreen("mili (^w^)")

          if target == "princess":
            if vrep >= 5:
              shortrandom = random.randint(6,10)
            else:
              shortrandom = random.randint(vrep, 7)
              
            if shortrandom >= 7:
              print("you ready your blade")
              time.sleep(textspeed)
              print("one stab into her chest... she falls back into her chair")
              time.sleep(textspeed)
              print('"Thank you."')
              time.sleep(textspeed)
              print("she passes out on the table left in a pool of blood")
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("she flicks your sword away and lands a counter kick, dropping you to the floor")
              time.sleep(textspeed)
              print('"Speak."')
              time.sleep(textspeed)
              playerhealth -= 5
              if playerhealth <= 0:
                deathscreen("the princess (obtain 50 or more reputation)")

          if target == "giver":
            if vrep >= 5:
              shortrandom = random.randint(6,10)
            else:
              shortrandom = random.randint(vrep, 7)
              
            if shortrandom >= 7:
              print("you ready your blade")
              time.sleep(textspeed)
              print("one stab shatters the mirror")
              time.sleep(textspeed)
              print("you are left in the room, nothing changed")
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("you lunge the blade into the mirror, and you follow your blade, falling through the mirror")
              time.sleep(textspeed)
              print("you find yourself in a area of endless white fog")
              time.sleep(textspeed)
              print("stupid of you to do that huh")
              time.sleep(textspeed)
              deathscreen("the giver (obtain 50 or more reputation)")

          if target == "wise":
            if vrep >= 3:
              shortrandom = random.randint(4,8)
            else:
              shortrandom = random.randint(vrep, 5)
              
            if shortrandom >= 5:
              print("you ready your blade")
              time.sleep(textspeed)
              print("one stab penetrates the tree's core")
              time.sleep(textspeed)
              print('"owie :cc" wise says while sheding a tear')
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("you stab into the tree, but your sword bounces off, sending you and your sword onto the ground")
              time.sleep(textspeed)
              print("wise stares at you blankly")
              time.sleep(textspeed)
              print('"what did you do that for?"')
              time.sleep(textspeed)
              playerhealth -= 5
              if playerhealth <= 0:
                deathscreen("wise the tree (obtain 30 or more reputation)")
            
          if target == "noah":
            if vrep >= 3:
              print("you ready your blade")
              time.sleep(textspeed)
              print("noah runs away but trips on a rock")
              time.sleep(textspeed)
              print('"aye bruh chill..."')
              time.sleep(textspeed)
              print("he is a easy target")
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("noah grabs the front of the blade and throws you and your sword onto the ground")
              time.sleep(textspeed)
              print('"bum"')
              time.sleep(textspeed)
              playerhealth -= 5
              if playerhealth <= 0:
                deathscreen("noah (obtain 30 or more reputation)") 

          if target == "evan":
            if vrep >= 3:
              print("you ready your blade")
              time.sleep(textspeed)
              print("noah runs away but trips on a rock")
              time.sleep(textspeed)
              print('"aye bruh chill..."')
              time.sleep(textspeed)
              print("he is a easy target")
              time.sleep(textspeed)
              maxhp += 5
              playerhealth += 5
              return True
            else:
              print("you ready your blade")
              time.sleep(textspeed)
              print("noah grabs the front of the blade and throws you and your sword onto the ground")
              time.sleep(textspeed)
              print('"bum"')
              time.sleep(textspeed)
              playerhealth -= 5
              if playerhealth <= 0:
                deathscreen("noah (obtain 30 or more reputation)") 
      
      def vengeanceroll():
        global folkfood
        global momsmeal
        global medibedi
        global ammo
        global vrep
        global playerhunger
        global f1hunger
        global f2hunger
        global f3hunger

        shortrandom = random.randint(1,50)

        if shortrandom == 1:
          shortrandom = random.randint(1,100)
          if debugmode == 1:
            shortrandom = int(input("id?"))

          #common
          if shortrandom <= 50:
            shortrandom = random.randint(1,3)

            #bison (folkfood)
            if shortrandom == 1:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A BISON IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.5 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.5:
                      print("you shot the bison, you got 2 folkfood!")
                      ammo -= 1
                      folkfood += 2
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the bison got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a bison at a distance!")
                  time.sleep(textspeed)
              else:
                print("A BISON IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.5 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.5:
                      print("you stabbed the bison, you got 2 folkfood!")
                      vrep += 1
                      folkfood += 2
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the bison got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)

            #turkey (moms meal)
            elif shortrandom == 2:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A TURKEY IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.5 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.5:
                      print("you shot the turkey, you got 2 moms meals!")
                      ammo -= 1
                      momsmeal += 2
                      time.sleep(textspeed)
                      vrep += 1
                    else:
                      print("you were too slow and the turkey got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a turkey at a distance!")
                  time.sleep(textspeed)
              else:
                print("A TURKEY IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.5 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.5:
                      print("you stabbed the turkey, you got 2 moms meals!")
                      momsmeal += 2
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the turkey got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)
            
            #deer (medibedi)
            elif shortrandom == 3:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A DEER IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.3:
                      print("you shot the deer, you got a medibedi!")
                      ammo -= 1
                      medibedi += 1
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the deer got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a deer at a distance!")
                  time.sleep(textspeed)
              else:
                print("A DEER IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.3:
                      print("you stabbed the deer, you got a medibedi!")
                      medibedi += 1
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the deer got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)

          #rare
          elif shortrandom <= 75:
            shortrandom = random.randint(1,3)

            #bison (folkfood)
            if shortrandom == 1:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A RARE BISON IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.3:
                      print("you shot the bison, you got 5 folkfood!")
                      ammo -= 1
                      folkfood += 5
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the bison got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a bison at a distance!")
                  time.sleep(textspeed)
              else:
                print("A RARE BISON IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.3:
                      print("you stabbed the bison, you got 5 folkfood!")
                      folkfood += 5
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the bison got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)

            #turkey (moms meal)
            elif shortrandom == 2:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A RARE TURKEY IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.3:
                      print("you shot the turkey, you got 5 moms meals!")
                      ammo -= 1
                      momsmeal += 5
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the turkey got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a turkey at a distance!")
                  time.sleep(textspeed)
              else:
                print("A RARE TURKEY IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.3:
                      print("you stabbed the turkey, you got 5 moms meals!")
                      momsmeal += 2
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the turkey got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)
            
            #deer (medibedi)
            elif shortrandom == 3:
              shortrandom = random.randint(1,2)
              if shortrandom == 1:
                print("A SHINING DEER IS SPOTTED IN THE DISTANCE")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  if (folkmusket > 0 or folkrifle > 0) and ammo > 0:
                    if tottime <= 0.3:
                      print("you shot the deer, you got two medibedis!")
                      ammo -= 1
                      medibedi += 2
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the deer got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot shoot this target!")
                    time.sleep(textspeed)
                else:
                  print("you cannot stab a deer at a distance!")
                  time.sleep(textspeed)
              else:
                print("A SHINING DEER IS SPOTTED RUNNING ACROSS THE PATH")
                print("1 to shoot, 2 to stab")
                print("you have 0.3 seconds")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                tottime = endtime - starttime

                if shortinput == "1":
                  print("you cannot shoot a target in front of you!")
                  time.sleep(textspeed)
                else:
                  if folksword > 0 or folkrapier > 0:
                    if tottime <= 0.3:
                      print("you stabbed the deer, you got two medibedis!")
                      medibedi += 2
                      vrep += 1
                      time.sleep(textspeed)
                    else:
                      print("you were too slow and the deer got away! time:", round(tottime, 2))
                      time.sleep(textspeed)
                  else:
                    print("you cannot stab this target!")
                    time.sleep(textspeed)
              
          #epic
          elif shortrandom <= 90:
            shortrandom = random.randint(1,3)

            if shortrandom == 1:
              atks = ""
              for val in range(6):
                shortrandom = random.randint(0,1)
                atks = atks + str(shortrandom)

              print("a fog surrounds your band, you stand guard")
              time.sleep(textspeed)
              shortrandom = random.randint(0,1)
              if folksword > 0 or folkrapier > 0:
                for val in atks:
                  print("\033[H\033[2J", end="")
                  print("...")
                  if debugmode == 1:
                    print(atks)
                  time.sleep((random.randint(10,20))/10)
                  print("\033[H\033[2J", end="")
                  if val == "1":
                    print("enter 1 (0.3 sec)")
                    starttime = time.perf_counter()
                    shortinput = input("")
                    endtime = time.perf_counter()
                    tottime = endtime - starttime 

                    if tottime <= 0.3 and shortinput == "1":
                      print("you block the mysterious massive sword coming torwards you")
                      time.sleep(0.5)
                      print("it retracts its sword")
                      time.sleep(textspeed)              
                    else:
                      print("out of the fog, a giant sword hits your band, striking with immense force...")
                      time.sleep(textspeed)
                      print("rather than the impact striking with a injuring force, you feel your own satiety taken from you")
                      time.sleep(textspeed)
                      playerhunger -= 15
                      f1hunger -= 15
                      f2hunger -= 15
                      f3hunger -= 15
                      
                  if val == "0":
                    print("enter 0 (0.3 sec)")
                    starttime = time.perf_counter()
                    shortinput = input("")
                    endtime = time.perf_counter()
                    tottime = endtime - starttime 

                    if tottime <= 0.3 and shortinput == "0":
                      print("you block the mysterious massive sword coming torwards you")
                      time.sleep(0.5)
                      print("it retracts its sword")
                      time.sleep(textspeed)              
                    else:
                      print("out of the fog, a giant sword hits your band, striking with immense force...")
                      time.sleep(textspeed)
                      print("rather than the impact striking with a injuring force, you feel your own satiety taken from you")
                      time.sleep(textspeed)
                      playerhunger -= 15
                      f1hunger -= 15
                      f2hunger -= 15
                      f3hunger -= 15
                time.sleep(textspeed)
                print("the fog disperses, you are free")
                vrep += 1
                time.sleep(textspeed)
              else:
                print("out of the fog, a sword strikes your camp")
                time.sleep(textspeed)
                print("without proper defense you succumb to the force")
                time.sleep(textspeed)
                deathscreen("the blade (bring a sword...)")

          #legendary
          elif shortrandom <= 99:
            pass

          #mythic
          elif shortrandom == 100:
            pass
            
      def madnessroll():
      
        global timeresult
        global madnesschance
        global eventname
        global madnessresult
        global event
        global f1health
        global playerhealth
        global f2health
        global f3health
        
        if playerstamina <= 0:
          madnesschance = random.randint(1,250)
          if madnesschance == 1:
            madnesschance = random.randint(1,5)
            event = madnesschance - 6
            eventname = madnesslist[madnesschance - 1]
            madnessresult = 1
            return 1
          else: return 0
            
        if f1stamina <= 0 and f1health > 0:
          madnesschance = random.randint(1,250)
          if madnesschance == 1:
            madnesschance = random.randint(1,3)
            if madnesschance == 1:
              print(folk1name, "went mad and stabbed themselves")
              f1health -= 6
              time.sleep(textspeed)
            if madnesschance == 2:
              print(folk1name, "went mad and tripped on a rock")
              f1health -= 2
              time.sleep(textspeed)
            if madnesschance == 1:
              print(folk1name, "went mad and swung their fist at you")
              playerhealth -= 3
              time.sleep(textspeed)
            return 0
          
          else: return 0
      
        if f2stamina <= 0 and f2health > 0:
          madnesschance = random.randint(1,250)
          if madnesschance == 1:
            madnesschance = random.randint(1,3)
            if madnesschance == 1:
              print(folk2name, "went mad and stabbed themselves")
              f2health -= 6
              time.sleep(textspeed)
            if madnesschance == 2:
              print(folk2name, "went mad and tripped on a rock")
              f2health -= 2
              time.sleep(textspeed)
            if madnesschance == 1:
              print(folk2name, "went mad and swung their fist at you")
              playerhealth -= 3
              time.sleep(textspeed)
        
        if f3stamina <= 0 and f3health > 0:
          madnesschance = random.randint(1,250)
          if madnesschance == 1:
            madnesschance = random.randint(1,3)
            if madnesschance == 1:
              print(folk3name, "went mad and stabbed themselves")
              f3health -= 6
              time.sleep(textspeed)
            if madnesschance == 2:
              print(folk3name, "went mad and tripped on a rock")
              f3health -= 2
              time.sleep(textspeed)
            if madnesschance == 1:
              print(folk3name, "went mad and swung their fist at you")
              playerhealth -= 3
              time.sleep(textspeed)
            return 0
          
          else: return 0
        
        else:
          return 0
          
      def diseaseroll():
        global playerdiseasecooldown
        global f1infectionTimer
        global f2infectionTimer
        global f3infectionTimer
        global playerinfectionTimer
        global shortrandom
        global diseaserandom
        global virellosisID
        global nyxoplasiaID
        global umbrythiaID
        global umbrythiaSpread
        global folk1dis
        global folk2dis
        global folk3dis
        global playerdis
        
        dischance = 350
        dischance = dischance - ((difficulty - 1) * 25) 
        if active_expansion // 10 == 2:
          if infs1 == 1:
            dischance += 100
          else:
            dischance = dischance // 2
        if order == 2:
          dischance -= 75
        diseaserandom = random.randint(1,dischance)
        #print(dischance)
        #print(diseaserandom)
        
        
        #infect
        if diseaserandom == 1 and (umbrythiaID == 0 or nyxoplasiaID == 0 or virellosisID == 0):
          diseasecooldown = 144
          shortrandom = random.randint(1,4)
          diseaserandom = random.randint(1,30)
      
          #check for duplicate disease
          while (diseaserandom <= 10 and nyxoplasiaID != 0) or (diseaserandom <= 20 and diseaserandom > 10 and virellosisID != 0) or (diseaserandom >= 21 and umbrythiaID != 0):
            if nyxoplasiaID != 0 and virellosisID != 0 and umbrythiaID != 0:
              break
            diseaserandom = random.randint(1,30)
         
          #check for duplicate on same person
          while (shortrandom == 1 and (playerdis >= 1 or "player" in umbrythiaSpread or playerhealth == 0)) or (shortrandom == 2 and (folk1dis >= 1 or "f1" in umbrythiaSpread or f1health == 0)) or (shortrandom == 3 and (folk2dis >= 1 or "f2" in umbrythiaSpread or f2health)) or (shortrandom == 3 and (folk2dis >= 1 or "f2" in umbrythiaSpread or f3health == 0)):
            if playerdis >= 1 and folk1dis >= 1 and folk2dis >= 1 and folk3dis >= 1:
              break
            shortrandom = random.randint(1,4)

          while active_expansion == 32 or active_expansion == 33:
            print("\033[H\033[2J", end="")
            diseaserandom %= 10
            if diseaserandom <= 6:
              print("(manipulation expansion) a type 1 disease is infecting your band")
            elif diseaserandom <= 9:
              print("(manipulation expansion) a type 2 disease is infecting your band")
            elif diseaserandom == 10:
              print("(manipulation expansion) a type 3 disease is infecting your band")
            print("what disease would you like to be the subject")
            print("(1) nyxoplasia")
            print("(2) virellosis")
            print("(3) umbrythia")
            shortinput = input("")
            try: int(shortinput)
            except ValueError:
              print("this is not a valid input!")
              time.sleep(1)
            if int(shortinput) > 3 and int(shortinput) < 1:
              print("that is not a valid input!")
              time.sleep(1)
            else:
              shortinput = int(shortinput)
              if shortinput == 1 and nyxoplasiaID != 0:
                print("this disease already exists")
                time.sleep(1)
                continue
              if shortinput == 2 and virellosisID != 0:
                print("this disease already exists")
                time.sleep(1)
                continue
              if shortinput == 3 and umbrythiaID != 0:
                print("this disease already exists")
                time.sleep(1)
                continue
              diseaserandom += (shortinput - 1) * 10 
              while True:
                print("\033[H\033[2J", end="")
                print("who would you like to infect!")
                print("(1)", playername)
                print("(2)", folk1name)
                print("(3)", folk2name)
                print("(4)", folk3name)
                shortinput = input("")
                try: int(shortinput)
                except ValueError:
                  print("this is not a valid input!")
                  time.sleep(1)
                if int(shortinput) > 3 and int(shortinput) < 1:
                  print("that is not a valid input!")
                  time.sleep(1)
                else:
                  shortinput = int(shortinput)
                  if shortinput == 1 and playerdis != 0:
                    print(playername, "is already infected!")
                    time.sleep(1)
                    continue
                  if shortinput == 2 and folk1dis != 0:
                    print(folk1name, "is already infected")
                    time.sleep(1)
                    continue
                  if shortinput == 3 and folk2dis != 0:
                    print(folk2name, "is already infected")
                    time.sleep(1)
                    continue
                  if shortinput == 4 and folk3dis != 0:
                    print(folk3name, "is already infected")
                    time.sleep(1)
                    continue
                  else:
                    if shortinput == 1:
                      manuroll(13)
                    shortrandom = shortinput
                    break
              break
                
          
          #give disease to person
          if shortrandom == 1:
            playerdis = 1
            if active_expansion // 10 == 2 and infs1 == 1:
              playerinfectionTimer = random.randint(5,7)
            else:
              playerinfectionTimer = random.randint(9,12)
            if diseaserandom <= 6:
              nyxoplasiaID = 11
              print(playername, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 9:
              nyxoplasiaID = 12
              print(playername, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom == 10:
              nyxoplasiaID = 13
              print(playername, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 16:
              virellosisID = 11
              print(playername, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 19:
              virellosisID = 12
              print(playername, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom == 20:
              virellosisID = 13
              print(playername, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 26:
              umbrythiaID = 11
              umbrythiaSpread.append("player")
              print(playername, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom <= 29:
              umbrythiaID = 12
              umbrythiaSpread.append("player")
              print(playername, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom == 30:
              umbrythiaID = 13
              umbrythiaSpread.append("player")
              print(playername, "got stage", umbrythiaID % 10, "umbrythia")
           
          if shortrandom == 2:
            folk1dis = 1
            if active_expansion // 10 == 2 and infs1 == 1:
              f1infectionTimer = random.randint(5,7)
            else:
              f1infectionTimer = random.randint(9,12)
            
            if diseaserandom <= 6:
              nyxoplasiaID = 21
              print(folk1name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 9:
              nyxoplasiaID = 22
              print(folk1name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom == 10:
              nyxoplasiaID = 23
              print(folk1name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 16:
              virellosisID = 21
              print(folk1name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 19:
              virellosisID = 22
              print(folk1name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom == 20:
              virellosisID = 23
              print(folk1name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 26:
              umbrythiaID = 21
              umbrythiaSpread.append("f1")
              print(folk1name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom <= 29:
              umbrythiaID = 22
              umbrythiaSpread.append("f1")
              print(folk1name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom == 30:
              umbrythiaID = 23
              umbrythiaSpread.append("f1")
              print(folk1name, "got stage", umbrythiaID % 10, "umbrythia")
      
          if shortrandom == 3:
            folk2dis = 1
            if active_expansion // 10 == 2 and infs1 == 1:
              f1infectionTimer = random.randint(5,7)
            else:
              f2infectionTimer = random.randint(9,12)
            if diseaserandom <= 6:
              nyxoplasiaID = 31
              print(folk2name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 9:
              nyxoplasiaID = 32
              print(folk2name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom == 10:
              nyxoplasiaID = 33
              print(folk2name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 16:
              virellosisID = 31
              print(folk2name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 19:
              virellosisID = 32
              print(folk2name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom == 20:
              virellosisID = 33
              print(folk2name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 26:
              umbrythiaID = 31
              umbrythiaSpread.append("f2")
              print(folk2name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom <= 29:
              umbrythiaID = 32
              umbrythiaSpread.append("f2")
              print(folk2name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom == 30:
              umbrythiaID = 33
              umbrythiaSpread.append("f2")
              print(folk2name, "got stage", umbrythiaID % 10, "umbrythia")
      
          if shortrandom == 4:
            folk3dis = 1
            if active_expansion // 10 == 2 and infs1 == 1:
              f3infectionTimer = random.randint(5,7)
            else:
              f3infectionTimer = random.randint(9,12)
            if diseaserandom <= 6:
              nyxoplasiaID = 41
              print(folk3name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 9:
              nyxoplasiaID = 42
              print(folk3name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom == 10:
              nyxoplasiaID = 43
              print(folk3name, "got stage", nyxoplasiaID % 10, "nyxoplasia")
            elif diseaserandom <= 16:
              virellosisID = 41
              print(folk3name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 19:
              virellosisID = 42
              print(folk3name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom == 20:
              virellosisID = 43
              print(folk3name, "got stage", virellosisID % 10, "virellosis")
            elif diseaserandom <= 26:
              umbrythiaID = 41
              umbrythiaSpread.append("f3")
              print(folk3name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom <= 29:
              umbrythiaID = 42
              umbrythiaSpread.append("f3")
              print(folk3name, "got stage", umbrythiaID % 10, "umbrythia")
            elif diseaserandom == 30:
              umbrythiaID = 43
              umbrythiaSpread.append("f3")
              print(folk3name, "got stage", umbrythiaID % 10, "umbrythia")
          if debugmode == 1:
            print(playerinfectionTimer)
            print(f1infectionTimer)
            print(f2infectionTimer)
            print(f3infectionTimer)
          time.sleep(textspeed)
           
      def diseaseeffect():
        global folkfood
        global momsmeal
        global chillmeat
        global playerfoodmultiplier
        global f1foodmultiplier
        global f2foodmultiplier
        global f3foodmultiplier
        global f1health
        global f2health
        global f3health
        global playerhealth
        global playerhunger
        global f1hunger
        global f2hunger
        global f3hunger
        global playerinfectionTimer
        global f1infectionTimer
        global f2infectionTimer
        global f3infectionTimer
        global shortrandom
        global diseaserandom
        global virellosisID
        global nyxoplasiaID
        global umbrythiaID
        global umbrythiaSpread
        global folk1dis
        global folk2dis
        global folk3dis
        global playerdis
        
        if nyxoplasiaID != 0:
          if nyxoplasiaID // 10 == 1 and playerhealth > 0:
            if playerdis < 2:
              playerhealth -= 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and f1health > 0:
                f1health -= 1
              if shortrandom == 2 and f2health > 0:
                f2health -= 1
              if shortrandom == 3 and f3health > 0:
                f3health -= 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth -= 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth -= 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
                serene = 0
                noHealing = 1
            else:
              playerhealth += 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and f1health > 0:
                f1health += 1
              if shortrandom == 2 and f2health > 0:
                f2health += 1
              if shortrandom == 3 and f3health > 0:
                f3health += 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth += 1
                f1health += 1
                f2health += 1
                f3health += 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth += 1
                f1health += 1
                f2health += 1
                f3health += 1
                serene = 144              
          if nyxoplasiaID // 10 == 2 and f1health > 0:
            if folk1dis < 2:
              f1health -= 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and playerhealth > 0:
                playerhealth -= 1
              if shortrandom == 2 and f2health > 0:
                f2health -= 1
              if shortrandom == 3 and f3health > 0:
                f3health -= 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth -= 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth -= 1
                serene = 0
                noHealing = 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
            else:
              f1health += 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and playerhealth > 0:
                playerhealth += 1
              if shortrandom == 2 and f2health > 0:
                f2health += 1
              if shortrandom == 3 and f3health > 0:
                f3health += 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth += 1
                f1health += 1
                f2health += 1
                f3health += 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth += 1
                serene = 144
                f1health += 1
                f2health += 1
                f3health += 1
          if nyxoplasiaID // 10 == 3 and f2health > 0:
            if folk2dis < 2:
              f2health -= 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and playerhealth > 0:
                playerhealth -= 1
              if shortrandom == 2 and f1health > 0:
                f1health -= 1
              if shortrandom == 3 and f3health > 0:
                f3health -= 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth -= 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth -= 1
                serene = 0
                noHealing = 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
            else:
              f2health += 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and playerhealth > 0:
                playerhealth += 1
              if shortrandom == 2 and f1health > 0:
                f1health += 1
              if shortrandom == 3 and f3health > 0:
                f3health += 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth += 1
                f1health += 1
                f2health += 1
                f3health += 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth += 1
                serene = 144
                f1health += 1
                f2health += 1
                f3health += 1        
          if nyxoplasiaID // 10 == 4 and f3health > 0:
            if folk3dis < 2:
              f3health -= 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and f1health > 0:
                playerhealth -= 1
              if shortrandom == 2 and f2health > 0:
                f2health -= 1
              if shortrandom == 3 and playerhealth > 0:
                playerhealth -= 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth -= 1
                f1health -= 1
                f2health -= 1
                f3health -= 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth -= 1
                serene = 0
                noHealing = 1
                f1health -= 1
                f2health -= 1
                f3health -= 1     
            else:
              f3health += 1
              shortrandom = random.randint(1,3)
              if shortrandom == 1 and f1health > 0:
                playerhealth += 1
              if shortrandom == 2 and f2health > 0:
                f2health += 1
              if shortrandom == 3 and playerhealth > 0:
                playerhealth += 1
                  
              if nyxoplasiaID % 10 == 2:
                playerhealth += 1
                f1health += 1
                f2health += 1
                f3health += 1
          
              if nyxoplasiaID % 10 == 3:
                playerhealth += 1
                serene = 144
                f1health += 1
                f2health += 1
                f3health += 1     
              
        if virellosisID != 0:
          if virellosisID // 10 == 1 and playerhealth > 0:
            if playerdis < 2:
              if playerhunger > 0: playerhunger -= 20
              
              if virellosisID % 10 == 2:
                if playerhunger > 0: playerhunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
          
              if virellosisID % 10 == 3:
                if playerhunger > 0: playerhunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
                playerfoodgainmultiplier = 0.5
            else:
              if playerhunger > 0: playerhunger += 20
              
              if virellosisID % 10 == 2:
                if playerhunger > 0: playerhunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
          
              if virellosisID % 10 == 3:
                if playerhunger > 0: playerhunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
                playerfoodgainmultiplier += 0.5
        
          if virellosisID // 10 == 2 and f1health > 0:
            if folk1dis < 2:
              if f1hunger > 0: f1hunger -= 20
              
              if virellosisID % 10 == 2:
                if f1hunger > 0: f1hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
          
              if virellosisID % 10 == 3:
                if f1hunger > 0: f1hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
                f1foodgainmultiplier = 0.5
            else:
              if f1hunger > 0: f1hunger += 20
              
              if virellosisID % 10 == 2:
                if f1hunger > 0: f1hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
          
              if virellosisID % 10 == 3:
                if f1hunger > 0: f1hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
                f1foodgainmultiplier += 1.5
              
          if virellosisID // 10 == 3 and f2health > 0:
            if folk2dis < 2:
              if f2hunger > 0: f2hunger -= 20
              
              if virellosisID % 10 == 2:
                if f2hunger > 0: f2hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
          
              if virellosisID % 10 == 3:
                if f2hunger > 0: f2hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
                f2foodgainmultiplier = 0.5
            else:
              if f2hunger > 0: f2hunger += 20
              
              if virellosisID % 10 == 2:
                if f2hunger > 0: f2hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
          
              if virellosisID % 10 == 3:
                if f2hunger > 0: f2hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
                f2foodgainmultiplier += 0.5
                
          if virellosisID // 10 == 4 and f3health > 0:
            if folk3dis < 2: 
              if f3hunger > 0: f3hunger -= 20
              
              if virellosisID % 10 == 2:
                if f3hunger > 0: f3hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
          
              if virellosisID % 10 == 3:
                if f3hunger > 0: f3hunger -= 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood -= 1
                  elif momsmeal > 0: momsmeal -= 1
                  elif chillmeat > 0: chillmeat -= 1
                f3foodgainmultiplier = 0.5
            else:
              if f3hunger > 0: f3hunger += 20
              
              if virellosisID % 10 == 2:
                if f3hunger > 0: f3hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood < 3: folkfood += 1
                  elif momsmeal < 3: momsmeal += 1
                  elif chillmeat < 3: chillmeat += 1
          
              if virellosisID % 10 == 3:
                if f3hunger > 0: f3hunger += 20
                shortrandom = random.randint(1,2)
                if shortrandom == 2:
                  if folkfood > 0: folkfood += 1
                  elif momsmeal > 0: momsmeal += 1
                  elif chillmeat > 0: chillmeat += 1
                f3foodgainmultiplier += 0.5
              
        if umbrythiaID != 0 or len(umbrythiaSpread) > 0:
          if (umbrythiaID // 10 == 1 or "player" in umbrythiaSpread) and playerhealth > 0:
            if playerdis < 2:
              playerhealth -= 1
              
              if umbrythiaID % 10 == 2:
                playerhunger-= 20
                playerhealth -= 1
                
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 1:
                playerhunger-= 20
                playerhealth -= 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    folk1dis = 1
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 1
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 1
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
            else:
              playerhealth += 1
              
              if umbrythiaID % 10 == 2:
                playerhunger += 20
                playerhealth += 1
                
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 1:
                playerhunger += 20
                playerhealth += 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    folk1dis = 2
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 2
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 2
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
        
          if (umbrythiaID // 10 == 2 or "f1" in umbrythiaSpread) and f1health > 0:
            if folk1dis < 2:
              f1health -= 1
              
              if umbrythiaID % 10 == 2:
                f1hunger -= 20
                f1health -= 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 2:
                f1hunger-= 20
                f1health -= 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    umbrythiaSpread.append("player")
                    playerdis = 1
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 1
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 1
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
            else:
              f1health += 1
              
              if umbrythiaID % 10 == 2:
                f1hunger += 20
                f1health += 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 2:
                f1hunger += 20
                f1health += 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    umbrythiaSpread.append("player")
                    playerdis = 2
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 2
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 2
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
        
          if (umbrythiaID // 10 == 3 or "f2" in umbrythiaSpread) and f2health > 0:
            if folk2dis < 2: 
              f2health -= 1
              
              if umbrythiaID % 10 == 2:
                f2hunger-= 20
                f2health -= 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 3:
                f2hunger -= 20
                f2health -= 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    umbrythiaSpread.append("player")
                    playerdis = 1
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                    folk1dis = 1
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 1
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
            else:
              f2health += 1
              
              if umbrythiaID % 10 == 2:
                f2hunger += 20
                f2health += 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 3:
                f2hunger += 20
                f2health += 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    umbrythiaSpread.append("player")
                    playerdis = 2
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                    folk1dis = 2
                  if shortrandom == 3 and folk3dis == 0 and not("f3" in umbrythiaSpread):
                    folk3dis = 2
                    umbrythiaSpread.append("f3")
                    f3infectionTimer = random.randint(2,4)
              
        
          if (umbrythiaID // 10 == 4 or "f3" in umbrythiaSpread) and f3health > 0:
            if folk3dis < 2:
              f3health -= 1
              
              if umbrythiaID % 10 == 2:
                f3hunger-= 20
                f3health -= 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 4:
                f3hunger-= 20
                f3health -= 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    playerdis = 1
                    umbrythiaSpread.append("player")
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    folk1dis = 1
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 1
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
              else:
                f3health += 1
              
              if umbrythiaID % 10 == 2:
                f3hunger += 20
                f3health += 1
              if umbrythiaID % 10 == 3 and umbrythiaID // 10 == 4:
                f3hunger += 20
                f3health += 1
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1 and playerdis == 0 and not("player" in umbrythiaSpread):
                    playerdis = 2
                    umbrythiaSpread.append("player")
                    playerinfectionTimer = random.randint(2,4)
                  if shortrandom == 2 and folk1dis == 0 and not("f1" in umbrythiaSpread):
                    folk1dis = 2
                    umbrythiaSpread.append("f1")
                    f1infectionTimer = random.randint(2,4)
                  if shortrandom == 3 and folk2dis == 0 and not("f2" in umbrythiaSpread):
                    folk2dis = 2
                    umbrythiaSpread.append("f2")
                    f2infectionTimer = random.randint(2,4)
                
      
        if playerhealth <= 0:
          deathscreen("disease (get a cure or suck it up)")
        
        #remove?
        if playerinfectionTimer > 0:
          if sleepmode != 0:
            playerinfectionTimer -= 2
          else:
            playerinfectionTimer -= 1
          
          if playerinfectionTimer <= 0:
            print(playername, "is feeling better")
            time.sleep(textspeed)
            playerdis = 0
            if nyxoplasiaID // 10 <= 1:
              nyxoplasiaID = 0
              noHealing = 0
            elif virellosisID // 10 <= 1:
              virellosisID = 0
            elif umbrythiaID // 10 <= 1:
              umbrythiaID = 0
              if "player" in umbrythiaSpread:
                umbrythiaSpread.pop("player")
        
        if f1infectionTimer > 0:
          if sleepmode != 0:
            f1infectionTimer -= 2
          else: 
            f1infectionTimer -= 1
          
          if f1infectionTimer <= 0:
            print(folk1name, "is feeling better")
            time.sleep(textspeed)
            folk1dis = 0
            if nyxoplasiaID // 10 == 2:
              nyxoplasiaID = 0
              noHealing = 0
            elif virellosisID // 10 == 2:
              virellosisID = 0
            elif umbrythiaID // 10 == 2:
              umbrythiaID = 0
              if "f1" in umbrythiaSpread:
                umbrythiaSpread.remove("f1")
      
        if f2infectionTimer > 0:
          if sleepmode != 0:
            f2infectionTimer -= 2
          else:
            f2infectionTimer -= 1
          if f2infectionTimer <= 0:
            folk2dis = 0
            print(folk2name, "is feeling better")
            time.sleep(textspeed)
            if nyxoplasiaID // 10 == 3:
              nyxoplasiaID = 0
              noHealing = 0
            elif virellosisID // 10 == 3:
              virellosisID = 0
            elif umbrythiaID // 10 == 3:
              umbrythiaID = 0
              if "f2" in umbrythiaSpread:
                umbrythiaSpread.remove("f2")
        
        if f3infectionTimer > 0:
          if sleepmode != 0:
            f3infectionTimer -= 2
          else: 
            f3infectionTimer -= 1
          if f3infectionTimer <= 0:
            folk3dis = 0
            print(folk3name, "is feeling better")
            time.sleep(textspeed)
            if nyxoplasiaID // 10 == 4:
              nyxoplasiaID = 0
              noHealing = 0
            elif virellosisID // 10 == 4:
              virellosisID = 0
            elif umbrythiaID // 10 == 4:
              umbrythiaID = 0
              if "f3" in umbrythiaSpread:
                umbrythiaSpread.remove("f3")
      
      def passtime():
        global score
        global sleepmode
        global folkfood
        global momsmeal
        global rosavale
        global slyphora
        global wyrmrose
        global velisara
        global luneblossom
        global tickspeed
        global fcstage
        global diseasecooldown
        global playerstamina
        global f1stamina
        global f2stamina
        global f3stamina
        global distance
        global distancemultiplier
        global playerfoodmultiplier
        global f1foodmultiplier
        global f2foodmultiplier
        global f3foodmultiplier
        global f1health
        global f2health
        global f3health
        global playerhealth
        global playerhunger
        global f1hunger
        global f2hunger
        global f3hunger
        global daynum
        global timehr
        global eventresult
        global tickamm
        global savedticknum
        global timesec
        global serene 
        global folkcount
        global morn
        global even
        global isday
        global manueventcd
        global manuord1
        global manuord2
        global manuord3
        global manuord1ID
        global manuord2ID
        global manuord3ID

      
        fixnum()

        if nuke == 1:
          deathscreen("u blew up smh")
        

        if active_expansion // 10 == 3 and int(timehr) == 0:
          manuord1 = manuords[random.randint(0, len(manuords) - 1)]
          manuord2 = manuords[random.randint(0, len(manuords) - 1)]
          manuord3 = manuords[random.randint(0, len(manuords) - 1)]

          manuord1ID = manuords.index(manuord1)
          manuord2ID = manuords.index(manuord2)
          manuord3ID = manuords.index(manuord3)
        
        folkcount = 0
        
        if f1health != 0:
          folkcount += 1
        if f2health != 0:
          folkcount += 1
        if f3health != 0:
          folkcount += 1
        playerfoodmultiplier = 1
        f1foodmultiplier = 1
        f2foodmultiplier = 1
        f3foodmultiplier = 1
        playerfoodmultiplier *= random.uniform(0.5,1.3)
        f1foodmultiplier *= random.uniform(0.5,1.3)
        f2foodmultiplier *= random.uniform(0.5,1.3)
        f3foodmultiplier *= random.uniform(0.5,1.3)
        distancemultiplier = 1
        distancemultiplier *= random.uniform(0.7, 1.5)
        
        if fcstage <= 1.75:
          distancemultiplier *= 0.9    
        elif fcstage <= 2.75:
          distancemultiplier *= 0.8
        elif fcstage <= 3.75:
          distancemultiplier *= 0.6
          if fcplayer != 0:
            playerhealth -= 1
          if fcfolk1 != 0:
            f1health -= 1
            f2health -= 1
            f3health -= 1
        elif fcstage <= 4.75:
          if fcplayer != 0:
            playerhealth -= 1
          if fcfolk1 != 0:
            f1health -= 1
            f2health -= 1
            f3health -= 1
          distancemultiplier *= 0.5
      
        if order == 0:
          distancemultiplier *= 0.8
      
        if order == 2: 
          distancemultiplier *= 1.3

        
        
        if debugmode == 1:
          print(savedticknum)
          print(tickamm)
          print(playerfoodmultiplier)
          print(f1foodmultiplier)
          print(f2foodmultiplier)
          print(f3foodmultiplier)
          time.sleep(1)
        if savedticknum != 0:
          tickamm = savedticknum
          savedticknum = 0
        else:
          tickamm = 0
          
        timehr = int(timehr) 
        timsec = int(timesec)
        while tickamm < 72 or timehr == 6 or timehr == 12 or timehr == 18 or timehr == 0:
          print(isday)
          print(morn)
          print(even)
          if int(timehr) >= morn and int(timehr) < even:
            isday = 1
            daychange = 1
          else:
            isday = 0
            daychange = 1

          if active_expansion == 12 or active_expansion == 13:
            if isday == 1 and daychange == 1:
              distancemultiplier *= 1.3
              daychange = 0
            elif daychange == 1: 
              playerfoodmultiplier *= 0.7
              f1foodmultiplier *= 0.7
              f2foodmultiplier *= 0.7
              f3foodmultiplier *= 0.7
              daychange = 0
            
          if timesec == 60:
            timesec = "0"
            timehr = int(timehr)
            timehr += 1
          
          if int(timesec) < 10:
            timesec = str(timesec)
            timesec = "0" + timesec
          
          if int(timehr) < 10:
            timehr = int(timehr)
            timehr = str(timehr)
            timehr = "0" + timehr
      
      
            
            
          print("\033[H\033[2J", end="")
          
          if fcplayer == 1 or fcfolk1 == 1:
            print(f"{color.bpink}day:", daynum)
            print(timehr, ":", timesec)
          elif isday == 1:
            print(f"{color.byellow}day:", daynum)
            print(timehr, ":", timesec)
          else:
            print(f"{color.blue}day:", daynum)
            print(timehr, ":", timesec)
          print("distance remaining:", math.ceil(distance))
          
          if fcstage != 0:
            if fcstage <= 1.75:
              print("the floral curse overwhelms your thoughts, slowing you down")
            elif fcstage <= 2.75:
              print("the floral curse brings up small branches at your feet, slowing you down further")
            elif fcstage <= 3.75:
              print("the branches turn into thorns and hold back your steps, damaging and restraining you")
            elif fcstage <= 4.75:
              print("the thorns build up, damaging you further, turning your movement into a resistance against the thorns holding you still")
            elif fcstage >= 5:
              print("the thorns bloom")
      
          if playerhunger <= 25:
            print(playername, "is starving")
          if f1hunger <= 25:
            print(folk1name, "is starving")
          if f2hunger <= 25:
            print(folk2name, "is starving")
          if f3hunger <= 25:
            print(folk3name, "is starving")
          
          if debugmode == 1:
            print(score)
            print(tickamm)
            print(playerhunger)
            print(f1hunger)
            print(f2hunger)
            print(f3hunger)
          if sleepmode == 0 and fcstage != 5:
            if madnessroll() == 0:
              eventresult = eventroll()
              if active_expansion // 10 == 4:
                vengeanceroll()
              if diseasecooldown == 0:
                diseaseroll()
          if sleepmode == 2 and fcstage != 5:
            restevent()
            
      
          if order == 0 and sleepmode == 0:
            shortrandom = random.randint(1,150)
            if shortrandom == 1:
              shortrandom = random.randint(1,5)
              if shortrandom == 1:
                shortrandom = random.randint(1,5)
                if shortrandom == 1:
                  rosavale += 1
                  print("(pace bonus) you got a rosavale!")
                if shortrandom == 2:
                  slyphora += 1
                  print("(pace bonus) you got a slyphora!")
                if shortrandom == 3:
                  wyrmrose += 1
                  print("(pace bonus) you got a wyrmrose!")
                if shortrandom == 4:
                  velisara += 1
                  print("(pace bonus) you got a velisara!")
                if shortrandom == 5:
                  luneblossom += 1
                  manuroll(17)
                  print("(pace bonus) you got a luneblossom!")
                time.sleep(textspeed)
              elif shortrandom == 2 or shortrandom == 3:
                print("(pace bonus) you found folkfood")
                time.sleep(textspeed)
                folkfood += 1 
              else:
                print("(pace bonus) you found moms thankgiving meal")
                time.sleep(textspeed)
                momsmeal += 1
          if serene != 0:
            serene -= 1
          if diseasecooldown != 0: 
            diseasecooldown -= 1
          if manueventcd != 0: 
            manueventcd -= 1
          
          if eventresult == 1 or madnessresult == 1: 
            return 1
          
          if fcstage >= 5:
            tickspeed += 0.01
          time.sleep(tickspeed)
          timesec = int(timesec)
          timesec += 5
          if sleepmode == 1:
            if playerstamina < 100:
              playerstamina += 1
            else:
              playerstamina = 100
            if f1stamina < 100:
              f1stamina += 1
            else:
              f1stamina = 100
            if f2stamina < 100:
              f2stamina += 1
            else:
              f2stamina = 100
            if f3stamina < 100:
              f3stamina += 1
            else:
              f3stamina = 100
      
          if sleepmode == 2:
            if playerstamina < 100:
              playerstamina += 0.25
            else:
              playerstamina = 100
            if f1stamina < 100:
              f1stamina += 0.25
            else:
              f1stamina = 100
            if f2stamina < 100:
              f2stamina += 0.25
            else:
              f2stamina = 100
            if f3stamina < 100:
              f3stamina += 0.25
            else:
              f3stamina = 100
              
          if serene == 0:
            if playerhunger > 0:
              playerhunger -= random.uniform(0,0.5) * playerfoodmultiplier
            if f1health > 0 and f1hunger > 0:
              f1hunger -= random.uniform(0,0.5) * f1foodmultiplier
            if f2health > 0 and f2hunger > 0:
              f2hunger -= random.uniform(0,0.5) * f2foodmultiplier
            if f3health > 0 and f3hunger > 0:
              f3hunger -= random.uniform(0,0.5) * f3foodmultiplier
            
          if sleepmode == 0:
            if playerstamina > 0 and playerhealth != 0:
              playerstamina -= 0.3 + ((3 - folkcount) * 0.1)
              if order == 2:
                playerstamina -= 0.1
              if order == 0:
                playerstamina += 0.1
              if (active_expansion == 22 or active_expansion == 23) and isday == 0:
                playerstamina += 0.2
            if f1stamina > 0 and f1health != 0:
              f1stamina -= 0.3 + ((3 - folkcount) * 0.1)
              if order == 2:
                f1stamina -= 0.1
              if order == 0:
                f1stamina += 0.1
              if (active_expansion == 22 or active_expansion == 23) and isday == 0:
                f1stamina += 0.2
            if f2stamina > 0 and f2health != 0:
              f2stamina -= 0.3 + ((3 - folkcount) * 0.1)
              if order == 2:
                f2stamina -= 0.1
              if order == 0:
                f2stamina += 0.1
              if (active_expansion == 22 or active_expansion == 23) and isday == 0:
                f2stamina += 0.2
            if f3stamina > 0 and f3health != 0:
              f3stamina -= 0.3 + ((3 - folkcount) * 0.1)
              if order == 2:
                f3stamina -= 0.1
              if order == 0:
                f3stamina += 0.1
              if (active_expansion == 22 or active_expansion == 23) and isday == 0:
                f3stamina += 0.2
          
          
      
          
          
          tickamm += 1
          if sleepmode == 0:
            distance -= (random.uniform(0.5, 1.5) * distancemultiplier)
            if distance < 0:
              return "DONE"
        if timesec == 60:
          timesec = "0"
          timehr = int(timehr)
          timehr += 1
        
        if int(timesec) < 10:
          timesec = str(timesec)
          timesec = "0" + timesec
      
        if int(timehr) == 24:
          timehr = 0
          daynum += 1
        
        if int(timehr) < 10:
          timehr = str(timehr)
          timehr = "0" + timehr
          
        if playerhunger <= 0 and serene == 0:
          playerhealth -= 2
          if playerhealth <= 0:
            deathscreen("starvation (eat food...)")
        hungpunish = 2 + (1*(difficulty-1))
        if f1hunger <= 0 and serene == 0:
          f1health -= hungpunish
          score -= 2
        if f2hunger <= 0 and serene == 0:
          f2health -= hungpunish
          score -= 2
        if f3hunger <= 0 and serene == 0:
          f3health -= hungpunish
          score -= 2
        if debugmode == 1:
          print("returning 0")
          time.sleep(2)
        if fcstage == 5:
          if fcplayer == 0:
            print("\033[H\033[2J", end="")
            print("the thorns engulf your folks")
            time.sleep(textspeed)
            print("in a instant, they disappear, with a red flower blossoming in their place")
            f1health = 0
            f2health = 0
            f3health = 0
          else:
            print("\033[H\033[2J", end="")
            print("the thorns engulf you")
            time.sleep(textspeed)
            playerhealth = 0
            deathscreen("floral curse (use rosacura)")
        diseaseeffect()
        if sleepmode != 0:
          sleepmode = 0
        if int(timehr) == 6:
          print(f"{color.byellow}")
  
        score += 10
  
        return 0
        
      def daystart(day):
        global happydino
        global deadtree
        global deaddino
        global baybakidead
        global event
        global eventname
        global daynum
        global textspeed
        
        if debugmode == 1:
          textspeed = 1
          daynum = input("day?")
          daynum = int(daynum)
          event = input("event?")
          event = int(event)
          if event == -1:
            event = random.randint(0,18)
        else:
          event = random.randint(0,18)
          
        while happydino ==  1 and event == 11:
          event = random.randint(0,18)
        while (event == 11 or event == 2 or event == 4) and deaddino == 1:
          event = random.randint(0,18)
        while event == 5 and deadtree == 1:
          event = random.randint(0,18)
        while event == 17 and NOmountain == 1:
          event = random.randint(0,18)
        while event == 18 and baybakidead == 1:
          event = random.randint(0,18)
        eventname = eventlist[event]
        
      def eventtext(event):
        if event == -5:
          print("\033[H\033[2J", end="")
          print("you are driving through the valley gracefully")
          time.sleep(textspeed)
          print("you notice a temple in the side of the hill")
          time.sleep(textspeed)
          print("you step into the temple: completely dark and silent")
          time.sleep(textspeed)
          print("the door slams behind you and a familiar voice is heard")
          time.sleep(textspeed)
          print('"hello', playername, '. do you remember me?"')
          time.sleep(textspeed)
          print('"ofc you dont. does mili ring a bell?"')
          time.sleep(textspeed)
          print('"welcome to my real store, my true passion"')
          print("")
          print("(1) check store")
          print("(2) leave")
      
        if event == -4:
          print("\033[H\033[2J", end="")
          print("the day was silent... night has fallen...")
          time.sleep(textspeed)
          print("...")
          time.sleep(textspeed)
          print("you wake up to a noise...")
          time.sleep(textspeed)
          print("a black figure remains infront of you with glaring red eyes...")
          time.sleep(textspeed)
          print("it approaches you")
          print("")
          print("(1) use folkmusket")
          print("(2) accept")
      
        if event == -3:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you hear a nearby roar in the trees...")
          time.sleep(textspeed)
          print("a spinosaurus comes out of the trees...")
          time.sleep(textspeed)
          print("I AM SPENCER THE SPINO, I AM HUNGRY, FEED ME")
          print("")
          print("(1) feed food")
          print("(2) feed folk")
          print("(3) run")
      
        if event == -2:
          print("\033[H\033[2J", end="")
          print("you turn in a forest, and arrive on a endless, flat field of pink glowing flowers...")
          time.sleep(textspeed)
          print("you stop in the field, relieving you of all stress...")
          time.sleep(textspeed)
          print("it is time to go")
          print("(1)take flower")
          print("(2)leave")
      
        if event == -1:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you hear a nearby loud snore...")
          time.sleep(textspeed)
          print("you notice spencer the spino sleeping gracefully")
          print("")
          print("(1) move on")
          print("(2) jump spencer")
          
        if event == 0:
          print("\033[H\033[2J", end="")   
          print("you come across a blocky character with a strange hat...")
          time.sleep(textspeed + 1)
          print("YOU FOUND A LUCKY DROID KILL IT FAST")
          print("")
          print("(1) kill")
          
        if event == 1:
          print("\033[H\033[2J", end="")
          print("you turn in a forest, and arrive on a endless, flat field of pink glowing flowers...")
          time.sleep(textspeed)
          print("you stop in the field, relieving you of all stress...")
          time.sleep(textspeed)
          print("it is time to go")
          print("(1)take flower")
          print("(2)leave")
          
        if event == 2:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you hear a nearby roar in the trees...")
          time.sleep(textspeed)
          print("a spinosaurus comes out of the trees...")
          time.sleep(textspeed)
          print("hi, im spencer the spino, do u want a gift")
          print("(1) take gift")
          print("(2) no no i insist")
          
        if event == 3:
          print("\033[H\033[2J", end="")
          print("walking through the endless valley, you and your folks feel a sudden sense of serenity...")
          time.sleep(textspeed)
          print("you look around... you are in a large empty field with rolling hills as far as you can see...")
          time.sleep(textspeed)
          print("you and your folks are not affected by hunger and health for today")
          print("")
          print("(1) move on ")
          
        if event == 4:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you hear a nearby loud snore...")
          time.sleep(textspeed)
          print("you notice spencer the spino sleeping gracefully")
          print("")
          print("(1) move on")
          print("(2) jump spencer")
          
        if event == 5:
          print("\033[H\033[2J", end="")
          print("in the forest, the nearby trees start to change appearance...")
          time.sleep(textspeed)
          print("a clearing with a large tree with a face is ahead...")
          time.sleep(textspeed)
          print("greetings, im tree the tree, people call me wise")
          time.sleep(textspeed)
          print("do you want to know your future?")
          print("")
          print("(1) okay...")
          print("(2) leave")
          
        if event == 6:
          print("\033[H\033[2J", end="")
          print("yo im noah wsg")
          print("")
          print("(1) wsg")
      
        if event == 7:
          print("\033[H\033[2J", end="")
          print("yo im evan wsg")
          print("")
          print("(1) wsg")
      
        if event == 8:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you stop at a river...")
          time.sleep(textspeed)
          print("folks say its shallow")
          print("")
          print("folkmobile: drive through mode")
          print("folkmobile: float mode")
        
        if event == 9:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you stop at a river...")
          time.sleep(textspeed)
          print("folks say its deep")
          print("")
          print("(1) folkmobile: drive through mode")
          print("(2) folkmobile: float mode")
      
        if event == 10:
          print("\033[H\033[2J", end="")
          print("you come to a screeching stop, as a mysterious wodden hut appears in front of you...")
          time.sleep(textspeed)
          print("you walk into the hut, leaving your folks and the folkmobile behind...")
          time.sleep(textspeed)
          print("you arrive on a mirror, infront of a wall full of skulls...")
          print("")
          print("(1) call for it")
          print("(2) leave")
      
        if event == 11:
          print("\033[H\033[2J", end="")
          print("moving along the trail, you hear a nearby roar in the trees...")
          time.sleep(textspeed)
          print("a spinosaurus comes out of the trees...")
          time.sleep(textspeed)
          print("I AM SPENCER THE SPINO, I AM HUNGRY, FEED ME")
          print("")
          print("(1) feed food")
          print("(2) feed folk")
          print("(3) run")
      
        if event == 12:
          print("\033[H\033[2J", end="")
          print("the day was silent... night has fallen...")
          time.sleep(textspeed)
          print("...")
          time.sleep(textspeed)
          print("you wake up to a noise...")
          time.sleep(textspeed)
          print("a black figure remains infront of you with glaring red eyes...")
          time.sleep(textspeed)
          print("it approaches you")
          print("")
          print("(1) use folkmusket")
          print("(2) accept")
        
        if event == 13:
          print("\033[H\033[2J", end="")
          print("you are driving through the valley gracefully")
          time.sleep(textspeed)
          print("you notice a temple in the side of the hill")
          time.sleep(textspeed)
          print("you step into the temple: completely dark and silent")
          time.sleep(textspeed)
          print("the door slams behind you and a familiar voice is heard")
          time.sleep(textspeed)
          print('"hello', playername, '. do you remember me?"')
          time.sleep(textspeed)
          print('"ofc you dont. does mili ring a bell?"')
          time.sleep(textspeed)
          print('"welcome to my real store, my true passion"')
          print("")
          print("(1) check store")
          print("(2) leave")
          
        if event == 14:
          print("\033[H\033[2J", end="")
          print("the day was silent... night has fallen...")
          time.sleep(textspeed)
          print("...")
          time.sleep(textspeed)
          print("the night is still and peaceful")
          time.sleep(textspeed)
          print("everything is fine")
          print("")
          print("(1) next")
        
        if event == 15:
          print("\033[H\033[2J", end="")
          print("you turn in a forest, and arrive on a endless, flat field of red glowing flowers...")
          time.sleep(textspeed)
          print("you stop in the field, relieving you of all stress, but evoking a unremarkable dread..")
          time.sleep(textspeed)
          print("it is time to go")
          print("")
          print("(1) leave")
           
        if event == 16:
          print("\033[H\033[2J", end="")
          print("you unexpectingly come across a strange desk in the valley...")
          time.sleep(textspeed)
          print("a force suddenly sits you at the desk in a instant")
          time.sleep(textspeed)
          print("everything around you goes dark, and a dark figure with red glowing eyes appears at the other end of the desk")
          time.sleep(textspeed)
          print("it gives you a paper with three math questions...")
          print("")
          print("(1) begin")
      
        if event == 17:
          print("\033[H\033[2J", end="")
          print("looking ahead you see a large mountain")
          time.sleep(textspeed)
          print("it reaches the sides of the valley")
          time.sleep(textspeed)
          print("you must got through it, or around it")
          print("")
          print("(1) through the mountain")
          print("(2) above the mountain")
      
        if event == 18:
          print("\033[H\033[2J", end="")
          print("you and your folks come across a table, with five empty chairs")
          time.sleep(textspeed)
          print("a irresistable force sits you and your folks in chairs")
          time.sleep(textspeed)
          print("everything around you gets dark, only the table is illuminated")
          time.sleep(textspeed)
          print("a figure walks out of the dark, in fashionable attire")
          time.sleep(textspeed)
          print('"welcome travelers. no time for introductions"')
          time.sleep(textspeed)
          print("he pulls out a revolver, loads one bullet, and spins it in the middle of table")
          time.sleep(textspeed)
          print("my name is baybaki, come play a little game of russian roulette...")
          time.sleep(textspeed+2)
      
        if event == 19:
          print("\033[H\033[2J", end="")
          print("the nearby forestry turns purple tinted; you arrive at a area surrounded by large rocks")
          time.sleep(textspeed)
          print("the walls have mysterious inscriptions; the top covered in purple tree leaves")
          time.sleep(textspeed)
          print("a river flows through the middle, unknown start, unknow end")
          time.sleep(textspeed)
          print("a plethora of objects flow through")
          time.sleep(textspeed)
          print("the grass growing on rock seems to have the same strange effect of objects")
          time.sleep(textspeed)
          print("(1) reach into grass")
          time.sleep(0.5)
          print("(2) reach into water")
          
      # the giver questions 
      def questionone():
        print("\033[H\033[2J", end="")
        print('"what is the name of the weapon dealer in the folk chamber?"')
        time.sleep(1)
        print("(1) millie")
        time.sleep(0.5)
        print("(2) mila")
        time.sleep(0.5)
        print("(3) mili")
        time.sleep(0.5)
        print("(4) milli")
      
      def questiontwo():
        print("\033[H\033[2J", end="")
        print('"what is the name of the black figure that interupts your sleep?"')
        time.sleep(1)
        print("(1) the scary black figure that interupts your sleep")
        time.sleep(0.5)
        print("(2) stan")
        time.sleep(0.5)
        print("(3) entity")
        time.sleep(0.5)
        print("(4) greg")
      
      def questionthree():
        print("\033[H\033[2J", end="")
        print('"what does spencer the spino give you if he is feeling generous?"')
        time.sleep(1)
        print("(1) folkmusket")
        time.sleep(0.5)
        print("(2) folkfood")
        time.sleep(0.5)
        print("(3) moms thankgiving meal")
        time.sleep(0.5)
        print("(4) antidote")
      
      def questionfour():
        print("\033[H\033[2J", end="")
        print('"who am i')
        time.sleep(1)
        print("(1) the pig")
        time.sleep(0.5)
        print("(2) the giver")
        time.sleep(0.5)
        print("(3) the housekeeper")
        time.sleep(0.5)
        print("(4) the tester") 
      
      def questionfive():
        print("\033[H\033[2J", end="")
        print('"what is the rare item the mythical tree gives?"')
        time.sleep(1)
        print("(1) the folknix")
        time.sleep(0.5)
        print("(2) the super nuke")
        time.sleep(0.5)
        print("(3) folk plane")
        time.sleep(0.5)
        print("(4) son")
      
      def mountaintext(txtnum):
        global terminus
        global smt
        global showprincess
        
        if txtnum == 1:
          print("\033[H\033[2J", end="")
          print("you use a pickaxe and work at a broken rock you notice in a cliff")
          time.sleep(textspeed)
          print("the broken rock reveals a cave, with two ways to venture down")
          time.sleep(textspeed)
          print("(1) move left")
          print("(2) move right")
      
        if txtnum == 2:
          print("\033[H\033[2J", end="")
          print("you move along the cave, and the dim illuminated cave begins to get brighter")
          time.sleep(textspeed)
          print("you turn the last corner and the valley appears ahead of you")
          time.sleep(textspeed)
          print("you continue on your journey, and wonder how much worse that experience could have been")
          time.sleep(textspeed)
      
        if txtnum == 3:
          print("\033[H\033[2J", end="")
          print("you move along the cave, and the dim illuminated cave begins to get darker")
          time.sleep(textspeed)
          print("you come across a large open area in the cave, illuminated by a strange green light")
          time.sleep(textspeed)
          print("there are three branches off this point")
          time.sleep(textspeed)
          print("(1) go left")
          print("(2) go right")
          print("(3) go middle")
      
        if txtnum == 4:
          print("\033[H\033[2J", end="")
          print("you move along the cave, a foul stench growing")
          time.sleep(textspeed)
          print("you hear hissing, and turn a corner to two blinding blue lights")
          time.sleep(textspeed)
          print("your vision clears, and a serpent the size of the entire cave stands before you")
          time.sleep(textspeed)
          print("you are frozen, struck by the serpents dazzeling eyes")
          time.sleep(textspeed)
          print("it approaches")
          time.sleep(textspeed)
          print("the average garden snake has never looked so harmless")
          time.sleep(textspeed)
      
        if txtnum == 5:
          print("\033[H\033[2J", end="")
          print("you move along the cave, the illuminated light constantly changing color")
          time.sleep(textspeed)
          print("you come to another opening, with four large pillars")
          time.sleep(textspeed)
          print("in the middle, a empty pedestal")
          time.sleep(textspeed)
          print("along the outside of the pillars, a white feathered dragon flies along the cavern walls")
          time.sleep(textspeed)
          print("it notices you")
          time.sleep(textspeed)
          print('"hello,', playername, ', i am serminut the feathered dragon"')
          time.sleep(textspeed)
          print('"place it in the pedestal, or your purpose is meaningless to me"')
          time.sleep(textspeed)
          print("(1) accept your fate")
          if terminus >= 1:
            print("(2) use terminus")
        
        if txtnum == 6:
          print("\033[H\033[2J", end="")
          if smt == 0:
            print("you go above the mountain, starting on a trail up the snowy heights")
            time.sleep(textspeed)
            print("after a while of adventuring through the snow and rocks, you come up on a split in the trail")
            time.sleep(textspeed)
          print("three paths:")
          time.sleep(textspeed)
          print("(1) a path the leads to a red corrupt tree, with several red rocks surrounding ")
          time.sleep(0.5)
          print("(2) the same path with no change in the environment")
          time.sleep(0.5)
          print("(3) a path leading into a large cavern enterence, covered in ice and snow ")
          print("WARNING: for the remainder of the event, text inputs may be time based")
          smt = 1
          
          
        if txtnum == 7:
          print("\033[H\033[2J", end="")
          print("you move torwards the tree, a large deafening crash as you move")
          time.sleep(textspeed)
          print("looking back, a large pile of snow and ice has cut your way back")
          time.sleep(textspeed)
          if showprincess == 2:
            print("seems like fate was inevitable")
            time.sleep(textspeed)
          print("the tree infront of you is pale and dead, with a red glow pulsing")
          time.sleep(textspeed)
          print("it emits a powerful, resisting feeling")
          time.sleep(textspeed)
          print("red boulders surround the tree, seemingly being connected to the tree with light")
          time.sleep(textspeed)
          print("(1) investigate the boulders")
          time.sleep(0.5)
          print("(2) investigate the tree")
          time.sleep(0.5)
          print("(3) move forward on the trail")
      
        if txtnum == 8:
          print("\033[H\033[2J", end="")
          print("you move torwards the boulders, starting to see your reflection through the rock")
          time.sleep(textspeed)
          print("you touch the rock, feeling a warm conforting feeling contrasting from the frigid temperatures")
          time.sleep(textspeed)
          print("you pick it up the heavy boulder from the ground, barely having enough strength to carry it")
          time.sleep(textspeed)
          print("(1) investigate the tree")
      
        if txtnum == 9:
          print("\033[H\033[2J", end="")
          print("you move torwards the tree with the boulder in your arms")
          time.sleep(textspeed)
          print("the tree forces the boulder out of your arms, taking it into the core")
          time.sleep(textspeed)
          print("the tree accepts the rock, and does nothing in return")
          time.sleep(textspeed)
          print("suddenly, the tree strikes you with a strange force")
          time.sleep(textspeed)
          print("a portion of your blood is infused in the tree")
          time.sleep(textspeed)
          print("the freezing temperature suddenly feels much less freezing")
          time.sleep(textspeed)
          print("(1) move through the trail")
      
        if txtnum == 10:
          print("\033[H\033[2J", end="")
          print("you approach the tree, requiring increasing effort")
          time.sleep(textspeed)
          print("your legs give out and you fall on the ground")
          time.sleep(textspeed)
          print("the freezing cold suddenly turns into burning hot")
          time.sleep(textspeed)
          print("the dominant tree doesn't accept you, you burn alive")
          time.sleep(textspeed)
      
        if txtnum == 11:
          print("\033[H\033[2J", end="")
          print("you move along, unbothered by the red rocks and tree")
          time.sleep(textspeed)
          print("the trail continues with seemingly no end")
          time.sleep(textspeed)
          print("the freezing temperature feels more freezing, and starts to stab your body")
          time.sleep(textspeed)
          print("you cant make it any longer, you succumb to the cold")
          time.sleep(textspeed)
      
        if txtnum == 12:
          print("\033[H\033[2J", end="")
          print("you move along; the freezing temperatures mean nothing")
          time.sleep(textspeed)
          print("the strenuous trail ends at a open frozen lake, with a mysterious white fog in all directions")
          time.sleep(textspeed)
          print("you know the end is past this lake, you must push on")
          time.sleep(textspeed)
          print("(1) move through")
          #ADD DRAGON TOOTH
      
        if txtnum == 13:
          print("\033[H\033[2J", end="")
          print("the white fog turns out to be a powerful bizzard, and the power gained from the tree seems less effective against this environment")
          time.sleep(textspeed + 1)
          print("being slightly bearable, you make progress past the blizzard")
          time.sleep(textspeed)
          print("the conditions seemingly get worse")
          time.sleep(textspeed)
          print("(1) push through")
      
        if txtnum == 14:
          print("\033[H\033[2J", end="")
          print("you can, you do")
          time.sleep(textspeed)
          print("you make it through the mysterious blizzard, with the rest of the valley greeting you on the other side...")
          time.sleep(textspeed)
      
        if txtnum == 15:
          print("\033[H\033[2J", end="")
          print("you cant, you dont")
          time.sleep(textspeed)
          print("the conditions completly take over your mind, and you collapse on the ice")
          time.sleep(textspeed)
      
        if txtnum == 16:
          print("\033[H\033[2J", end="")
          print("you decide to take the same trail, the safe route, the cautious route")
          time.sleep(textspeed)
          print("you are nearing the end of your endurance through the conditions when you see a village")
          time.sleep(textspeed)
          print("the people look panicked")
          time.sleep(textspeed)
          print('"a nearby sign says, "KINGDOM OF SAL VINDAGNYR"...')
          time.sleep(textspeed+2)
          
        if txtnum == 17: 
          print("\033[H\033[2J", end="")
          print("what to do?")
          time.sleep(0.5)
          print("(1) visit a nearby shop")
          time.sleep(0.5)
          if showprincess == 0:
            print("(2) visit a nearby crowd")
            time.sleep(0.5)
            print("(3) follow the trail forward")
            time.sleep(0.5)
            print("(4) go back")
          else:
            print("(2) follow the trail forward")
            time.sleep(0.5)
            print("(3) go back")
      
        if txtnum == 18:
          print("\033[H\033[2J", end="")
          print("you walk up to the shop vendor looking distraught and hopeless")
          time.sleep(textspeed)
          print('"what c-"')
          time.sleep(textspeed)
          print("he notices your foreign appearence and straightens up")
          time.sleep(textspeed+2)
       
        if txtnum == 18.5:
          print("\033[H\033[2J", end="")
          print('"hello, can i help you with anything?"')
          time.sleep(textspeed)
          print("(1) visit shop")
          time.sleep(0.5)
          print("(2) ask about situation")
          if showprincess == 0:
            time.sleep(0.5)
            print("(3) ask about crowd")
            time.sleep(0.5)
            print("(4) leave")
          else:
            time.sleep(0.5)
            print("(3) leave")
        
        if txtnum == 19:
          print("\033[H\033[2J", end="")
          print('"okay..."')
          time.sleep(0.5)
          print("(1) strange tooth: 5 george")
          time.sleep(0.5)
          print("(2) chilled meat: 2 george ")
          time.sleep(0.5)
          print("(3) ammo: 1 george")
          time.sleep(0.5)
          print("(4) pickaxe: 4 george")
          time.sleep(0.5)
          print("(5) nevermind")
      
        if txtnum == 20:
          print("\033[H\033[2J", end="")
          print('"the higher ups think we are too greedy and we are about to be punished"')
          time.sleep(textspeed)
          print('"everyone is planning evacuation, but i know its helpless"')
          time.sleep(textspeed)
          print('"our punishment will happen at the top of the mountain and cause a avalanche to destory our kingdom"')
          time.sleep(textspeed)
          print('"you know what they say..."')
          time.sleep(textspeed)
          print('"only fate will not deceive you, unless you can first deceive fate itself"')
          time.sleep(0.5)
          print("(1) back")
      
        if txtnum == 21:
          print("\033[H\033[2J", end="")
          print('"that crowd over there is likely seeking answers from our princess; the current leader"')
          time.sleep(textspeed)
          print('"shes confident is keeping her status, and letting people know that she will save the kingdom"')
          time.sleep(textspeed)
          print('"but even she knows how helpless we are"')
          time.sleep(textspeed)
          print("(1) back")
      
        if txtnum == 22:
          print("\033[H\033[2J", end="")
          print("you approach a crowd, all surrounding one person on a throne")
          time.sleep(textspeed)
          print("she looks around the crowd, with tears barely showing in her eyes")
          time.sleep(textspeed)
          print("she notices you and calls you into a room behind her")
          time.sleep(textspeed)
          print("before you have time to question anything, you are suddenly in a dark room illuminated by two torches to the side")
          time.sleep(textspeed)
          print("the woman from before steps out of the dark in a white fur coat and a white glistening crown")
          time.sleep(textspeed)
          print("(1) next")
      
        if txtnum == 23:
          print("\033[H\033[2J", end="")
          print('"Hello,', playername, '. What brings you to our falling kingdom?"')
          time.sleep(textspeed)
          print("(1) i need answers!")
          time.sleep(0.5)
          print("(2) to fix your reign")
          time.sleep(0.5)
          print("(3) a answer from the gods")
      
        if txtnum == 24:
          print("\033[H\033[2J", end="")
          print('"You come to our denouement and you ask questions?"')
          time.sleep(textspeed)
          print("(1) yup!")
          time.sleep(0.5)
          print("(2) kidding (back)")
      
        if txtnum == 25:
          print("\033[H\033[2J", end="")
          print('"What do I need to do?"')
          time.sleep(textspeed)
          print("(1) your bloodlust")
          time.sleep(0.5)
          print("(2) your greed")
          time.sleep(0.5)
          print("(3) your ego")
      
        if txtnum == 26:
          print("\033[H\033[2J", end="")
          print('"I supposed I deserve punishment then..."')
          time.sleep(textspeed)
          print("sitting in the room very suddenly turns to sitting on a rock in the village center")
          time.sleep(textspeed)
          print("seems like she accepted the fate")
          time.sleep(textspeed)
      
        if txtnum == 27:
          print("\033[H\033[2J", end="")
          print('"Intresting. In the gods favor, I suppose I can let off some of our conquests"')
          time.sleep(textspeed)
          print('"Thank you"')
          time.sleep(textspeed)
          print("sitting in the room very suddenly turns to sitting on a rock in the village center")
          time.sleep(textspeed)
          print("maybe fate has been changed?")
          time.sleep(textspeed)
      
        if txtnum == 28:
          print("\033[H\033[2J", end="")
          print("sitting in the room very suddenly turns to sitting on a rock in the village center")
          time.sleep(textspeed)
          print("you feel guilty")
          time.sleep(textspeed)
      
        if txtnum == 29: 
          print("\033[H\033[2J", end="")
          print("you take the trail onward, moving past vindagnyr")
          time.sleep(textspeed)
          print("you move down the mountain, with the base in sight")
          time.sleep(textspeed)
          print("suddenly a crash comes from behind you...")
          time.sleep(textspeed)
          print("a uncontrollable torrent of snow rushes behind you")
          time.sleep(textspeed)
          print("you're helpless")
          time.sleep(textspeed)
          print("perhaps this was fate")
          time.sleep(textspeed)
          
        if txtnum == 30: 
          print("\033[H\033[2J", end="")
          print("you take the trail onward, moving past vindagnyr")
          time.sleep(textspeed)
          print("you move down the mountain, with the base in sight")
          time.sleep(textspeed)
          print("you complete the trail, you make it past the mountain")
          time.sleep(textspeed)
          print("perhaps fate has been decieved")
          time.sleep(textspeed)
      
        if txtnum == 31:
          print("\033[H\033[2J", end="")
          print("unexpectingly, a crash comes from the mountain, and a torrent of rocks fall down from the nearby cliff")
          time.sleep(textspeed)
          print("with the rocks come a avalanche")
          time.sleep(textspeed)
          print("the people of the town are stationary, staring blankly at the event")
          time.sleep(textspeed)
          print("you, with the rest of the people suffer the punishment from the gods")
          time.sleep(textspeed)
          print("perhaps time wasnt in your favor")
      
        if txtnum == 32:
          print("\033[H\033[2J", end="")
          print("you make your way into the cave, opening to overwhelmingly large open area")
          time.sleep(textspeed)
          print("you venture farther into the hollow mountain, the walls covered in illuminated ice and stone")
          time.sleep(textspeed)
          print("(1) follow the path upwards, into a opening at the top of the cave")
          time.sleep(textspeed)
          print("(2) follow the path downwards, into the bottom of the cave")
      
        if txtnum == 33:
          print("\033[H\033[2J", end="")
          print("you go up the path, a rock path acting as a bridge to the ceiling, the opening illuminated by sunlight")
          time.sleep(textspeed)
          print("when you reach the top, a few more turns leads you to the peak of the mountain...")
          time.sleep(textspeed)
          print("you are surrounded by towereing rock pillars rather than standing at the tallest point")
          time.sleep(textspeed)
          print("(1) move further up")
      
        if txtnum == 34:
          print("\033[H\033[2J", end="")
          print("you traverse up the path, around pillars, up to the tallest point")
          time.sleep(textspeed)
          print("a crash comes from above, a large meteor rushing torwards you")
          time.sleep(textspeed)
          print("(1) strike rock")
          print("(2) shoot rock")
          print("(3) pray")
          print("(4) run")
      
        if txtnum == 35:
          print("\033[H\033[2J", end="")
          print("you traverse up the path, around pillars, up to the tallest point")
          time.sleep(textspeed)
          print("you reach the tallest pillar, and sit down")
          time.sleep(textspeed)
          print("you can see the valley, the surrounding mountain range lasting as far as the eye can see")
          time.sleep(textspeed)
          print("what makes this mountain different?")
          time.sleep(0.5)
          print("how come this mountain obstructs the path?")
          time.sleep(textspeed)
          print("you come back to reality and you are back on the main path of the valley, down the mountain")
          time.sleep(textspeed)
          print("everyone feels better")
          time.sleep(textspeed)
      
      
        if txtnum == 36:
          print("\033[H\033[2J", end="")
          print("the rock completely shatters, the pieces landing at the base of the top of the mountain")
          time.sleep(textspeed)
          print("the sheer moving force of the rock stikes you, sending you off the mountain")
          time.sleep(textspeed)
          print("\033[H\033[2J", end="")
          print("...")
          time.sleep(textspeed)
          print("\033[H\033[2J", end="")
          print("you are woken on a large patch of grass, in a temperate climate, by", folk1name)
          time.sleep(textspeed)
          print("you are okay, you are back on track")
          time.sleep(textspeed)
          print("you even have a piece of the meteor, could be valuable")
          time.sleep(textspeed)
      
        if txtnum == 37:
          print("\033[H\033[2J", end="")
          print("you go down the path, moving along the sides of cavern walls")
          time.sleep(textspeed)
          print("you reach the bottom, a frozen lake emitting a especially frigid chill")
          time.sleep(textspeed)
          print("you cannot withstand this feeling much longer")
          time.sleep(textspeed)
          print("glistening rocks also catch your eye, holding a unrecognizable item within")
          time.sleep(textspeed)
          print("(1) mine rock")
          time.sleep(0.5)
          print("(2) go back up the path")
      
        if txtnum == 38:
          print("\033[H\033[2J", end="")
          print("you mine the rock, revealing a strange tooth. could be useful...")
          print("(1) go back up the path")
      
        if txtnum == 39:
          print("\033[H\033[2J", end="")
          print("you took too long, the frozen lake isnt normal")
          time.sleep(textspeed)
          print("you are frozen dead")
          time.sleep(textspeed)
      
        if txtnum == 40:
          print("\033[H\033[2J", end="")
          print("you stumble across a strange object sticking above the snow")
          time.sleep(textspeed)
          print("you pick up the object; shape like a tooth...")
          time.sleep(textspeed)   
          
      def milishop():
        print("\033[H\033[2J", end="")
        print("all items cost 5 health")
        print("(1) GLUTTONY")
        print("(2) WRATH")
        print("(3) PRIDE")
        print("(4) GREED")
        print("(5) LUST")
        print("(6) ENVY")
        print("(7) SLOTH")
        print("")
        print("(8) leave")
        print("enter choice")

      def manuroll(id):
        if debugmode == 1:
          print("order completed")
        global manuord1ID
        global manuord2ID
        global manuord3ID
        if manuord1ID == id:
          manuord1ID += 1000
        if manuord2ID == id:
          manuord2ID += 1000
        if manuord3ID == id:
          manuord3ID += 1000

      
      
      """
      print(event)
      print(midday)
      print(eventname)
      """
      
      
      while distance > 0:
        if savecontinue == 0:
          if savedticknum == 0:
            playerprevioushealth = playerhealth
            f1previoushealth = f1health
            f2previoushealth = f2health
            f3previoushealth = f3health
      
          if fcplayer == 1 or fcfolk1 == 1:
            fcstage += 0.25
          timeresult = passtime()
          
        else:
          timeresult = 0
          savecontinue = 0
          continue
        if playerhealth <= 0:
          deathscreen("null")
        if sleepmode == 1:
          sleepmode = 0
          
        if timeresult == 1:
          print(f"{color.white}")
          eventtext(event)
          print("")
          print("day =", daynum)
          print("event =", eventname)
          print("")
          print("v enter choice value below v")
      
          #MILIMADNESS//////////////////////////
          while event == -5:
            shortinput = input("")
            if shortinput == "1":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("you walked into a thorny bush. ow")
              time.sleep(textspeed)
              print("you lose 3 hp")
              score -= 2
              playerhealth -= 3
              if playerhealth <= 0:
                deathscreen("running into a thorny bush (maintain sanity or predict madness events)")
              time.sleep(textspeed)
            else:
              manuroll(12)
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("your thoughts are stronger than your consciousness")
              score += 2
              time.sleep(textspeed)
            event = -10
            madnessresult = 0
      
          #STANMADNESS//////////////////////////////
          while event == -4:
            shortinput = input("")
            if shortinput == "1":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              shortrandom = random.randint(1,3)
              while (shortrandom == 1 and f1health == 0) or (shortrandom == 2 and f2health == 0) or (shortrandom == 3 and f3health == 0):
                shortrandom = random.randint(1,3)
              if shortrandom == 1:
                print("you fire your gun instinctivly, hitting", folk1name)
                f1health = 0
              if shortrandom == 2:
                print("you fire your gun instinctivly, hitting", folk2name)
                f2health = 0
              if shortrandom == 3:
                print("you fire your gun instinctivly, hitting", folk3name)
                f3health = 0
              time.sleep(textspeed)
              print("they are dead")
              score -= 2
              time.sleep(textspeed)
              event = -10
              madnessresult = 0
            else:
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("your thoughts are stronger than your consciousness")
              manuroll(12)
              time.sleep(textspeed)
              event = -10
              madnessresult = 0
      
          #ANGRYSPINOMADNESS//////////////////////////////////
          while event == -3:
            shortinput = input("")
            if shortinput == "1":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("here you are holding food in the air")
              time.sleep(textspeed)
              print("your folks laugh at you")
              time.sleep(textspeed)
            if shortinput == "2":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              shortrandom = random.randint(1,3)
              if f1health == 0 and f2health == 0 and f3health == 0:
                  print("you monster")
                  time.sleep(textspeed)
                  print("you try to feed a thought your dead folk")
                  time.sleep(textspeed)
                  print("what is wrong with you")
                  time.sleep(textspeed)
                  score -= 2
                  event = -10
                  madnessresult = 0
                  break
              while (shortrandom == 1 and f1health == 0) or (shortrandom == 2 and f2health == 0) or (shortrandom == 3 and f3health == 0):
                shortrandom = random.randint(1,3)
              if shortrandom == 1:
                print("you, holding", folk1name, ", release in utter shock, dropping", folk1name, "on the ground")
                time.sleep(textspeed)
                f1health -= 2
              if shortrandom == 2:
                print("you, holding", folk2name, ", release in utter shock, dropping", folk2name, "on the ground")
                time.sleep(textspeed)
                f2health -= 2
              if shortrandom == 3:
                print("you, holding", folk3name, ", release in utter shock, dropping", folk3name, "on the ground")
                time.sleep(textspeed)
                f3health -= 2
              print("they are hurt and unhappy")
              time.sleep(textspeed)
              print("what good leader you are...")
              time.sleep(textspeed)
              score -= 2
            if shortinput == "3":
              manuroll(12)
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("you stop running")
              time.sleep(textspeed)
              print("as stupid as you look, you went distance")
              distance -= 50
              score += 2
              time.sleep(textspeed)
            event = -10
            madnessresult = 0
      
          #FLOWERFIELDMADNESS ///////////////////////////////////////
          while event == -2:
            shortinput = input("")
            if shortinput == "1":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("you reach down into flowers, they look less fun")
              time.sleep(textspeed)
              print("you feel cursed")
              fcplayer = 1
              manuroll(10)
              score -= 2
              time.sleep(textspeed)
            if shortinput == "2":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("it was all a lie")
              manuroll(12)
              time.sleep(textspeed)
              score += 2
              print("your thoughts are stronger than your consciousness")
              time.sleep(textspeed)
            event = -10
            madnessresult = 0
            
          #SPINOMADNESS ///////////////////////////////////////
          while event == -1:
            shortinput = input("")
            if shortinput == "1":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("you move along, failing to address the angry armed intruder")
              time.sleep(textspeed)
              print("your folks are unable to stop the inevitable, a shot into your chest")
              playerhealth = 0
              score -= 2
              deathscreen("going mad and failing to recognize the threat (manage your stamina by sleeping)")
              time.sleep(textspeed)
            if shortinput == "2":
              print("\033[H\033[2J", end="")
              print("you snap back to reality")
              time.sleep(textspeed)
              print("your blade penetrated straight through a intruder")
              time.sleep(textspeed)
              print("your folks are amazed")
              manuroll(12)
              time.sleep(textspeed)
      
            event = -10
            madnessresult = 0
              
          #LUCKYDROID //////////////////////////////////
          while event == 0:
            starttime = time.perf_counter()
            shortinput = input("")
            if shortinput == "1":
              end_time = time.perf_counter()
              inputtime = end_time - starttime
              print ("you killed the droid in", inputtime, "seconds")
              if inputtime <= 1:
                print("wow! you gained 50 george")
                george += 50
              if inputtime <= 2 and inputtime >= 1:
                print ("good! you gained 20 george")
                george += 20
                manuroll(2)
              if inputtime >= 2:
                print ("slow! you gained 10 george")
                george += 10
            time.sleep(textspeed)
            midday = 2
            event = -10
            shortinput = 0
      
          #FLOWERFIELD /////////////////////////////////
          while event == 1:
            shortinput = input("")
            if shortinput == "1":
              shortrandom = random.randint(1,5)
              if shortrandom == 1:
                rosavale += 1
                print("you pick a rosavale")
              if shortrandom == 2:
                slyphora += 1
                print("you pick a slyphora")
              if shortrandom == 3:
                wyrmrose += 1
                print("you pick a wyrmrose")
              if shortrandom == 4:
                velisara += 1
                print("you pick a velisara")
              if shortrandom == 5:
                luneblossom += 1
                manuroll(17)
                print("you pick a luneblossom")
  
              time.sleep(textspeed)
              
            if shortinput == "2":
              manuroll(11)
              print("you leave the field")
              time.sleep(textspeed)
      
            midday = 2
            event = -10
            shortinput = 0
          
          #NICESPINO ////////////////////////////////
          while event == 2:
            shortinput = input("")
            if shortinput == "1":
              print("you take the gift from spencer")
              time.sleep(textspeed)
              print("you got moms thanksgiving dinner!")
              momsmeal+=1
              time.sleep(textspeed)
            if shortinput == "2":
              manuroll(5)
              print("wow, you are too nice")
              time.sleep(textspeed)
              happydino = 1
            midday = 2
            event = -10
            shortinput = 0
            
          #SERENITY /////////////////////////////////
          while event == 3:
            shortinput = input("")
            if shortinput == "1":
              serene = 288
              midday = 2
              event = -10
              shortinput = 0
      
          #SPINO /////////////////////////////////
          while event == 4:
            shortinput = input("")
            if shortinput == "1":
              print("bye bye")
              time.sleep(textspeed)
              midday = 2
              event = -10
              shortinput = 0
            if shortinput == "2":
              print("your bloodlust takes over and you unsheathe your folksword")
              time.sleep(textspeed)
              print('"what is happening"')
              time.sleep(textspeed)
              print("you stab spencer")
              shortrandom = random.randint(1,20)
              if shortrandom == 20:
                time.sleep(textspeed)
                print("spencer is killed??")
                deaddino = 1
                time.sleep(textspeed)
                midday = 2
                event = -10
                shortinput = 0
              else:
                time.sleep(textspeed)
                print("spencer roars and completely devoures your entire band")
                playerhealth = 0
                deathscreen("attempted to kill a sleeping spinosaurus (just dont?)")
                midday = 2
                event = -10
                time.sleep(textspeed)
                    
          #MYTHICAL TREE///////////////////////////////
          while event == 5:
            shortinput = input("")
            if shortinput == "2":
              print('"okay bye :c"')
              time.sleep(textspeed)
              midday = 2
              event = -10
              shortinput = 0
            elif shortinput == "1":
              print('"let me see"')
              time.sleep(textspeed)
              shortrandom = random.randint(0,100)
              #print(shortrandom)
              if shortrandom <= 5:
                print('"yeah i think you deserve a folknix"')
                time.sleep(textspeed)
                folknix += 1
                manuroll(18)
                print('"use it wisely"')
                time.sleep(textspeed)
                shortinput = 0
                
              if shortrandom > 75:
                print("you deserve nothing, pain will follow on your journey")
                time.sleep(textspeed)
                
                if playerhealth != 0:
                  playerhealth -= 7
                  if playerhealth <= 0:
                    deathscreen("wise the tree (unlucky)")
                
                if f1health != 0:
                  f1health -= 7
                
                if f2health != 0:
                  f2health -= 7
      
                if f3health != 0:
                  f3health -= 7
      
                print('"have fun..."')
                time.sleep(textspeed)
              
              if shortrandom <= 75 and shortrandom >= 5:
                print('"you are good, you should get food and ammunition for your journey"')
                time.sleep(textspeed)
                momsmeal += 2
                ammo += 5
                print('"i believe in you!"')
                time.sleep(textspeed)
      
            midday = 2
            event = -10
            shortinput = 0
                
          #NOAH ///////////////////////////////////
          while event == 6:
            shortinput = input("")
            if shortinput == "1":
              print("noah joins your team")
              noah = 1
              if evan == 1:
                time.sleep(textspeed)
                print("something is happening")
                shortrandom = random.randint(1,2)
                time.sleep(textspeed)
                if shortrandom == 1:
                  print("noah and evan fuse... wow!")
                  evah = 1
                  manuroll(9)
                  time.sleep(textspeed)
                  print("use evah to replace a folk if they are dead!")
                  time.sleep(textspeed)
                if shortrandom == 2:
                  time.sleep(textspeed)
                  print("noah has died, leaving you with just evan")
                  noah = 0
                  time.sleep(textspeed)
              time.sleep(textspeed)
              midday = 2
              event = -10
              shortinput = 0
      
          #EVAN //////////////////////////////////////
          while event == 7:
            shortinput = input("")
            if shortinput == "1":
              print("evan joins your team")
              evan = 1
              if noah == 1:
                time.sleep(textspeed)
                print("something is happening")
                shortrandom = random.randint(1,2)
                time.sleep(textspeed)
                if shortrandom == 1:
                  print("noah and evan fuse... wow!")
                  evah = 1
                  manuroll(9)
                  time.sleep(textspeed)
                  print("use evah to replace a folk if they are dead!")
                  time.sleep(textspeed)
                if shortrandom == 2:
                  time.sleep(textspeed)
                  print("noah has died, leaving you with just evan")
                  time.sleep(textspeed)
                  
              time.sleep(textspeed)
              midday = 2
              event = -10
              shortinput = 0
         
          #SHALLOW RIVER ////////////////////////////////
          while event == 8:
            shortinput = input("")
           
            #floating
            if shortinput == "2":
              print("you attempt to float through the river")
              time.sleep(textspeed)
              print("the river is too shallow, you suffer massive damage")
              time.sleep(textspeed)
              print("would you like to use spare parts to magiclly save you?")
              print("(1) yes")
              shortinput2 = input("")
              if shortinput2 == "1":
                if parts >= 1:
                  print("you are saved, you make it to the other side")
                  parts -= 1
                  time.sleep(textspeed)
                else:
                  print("you do not have any spare parts")
                  time.sleep(textspeed)
                  print("your folkmobile explodes and ALL the rubble falls on you")
                  time.sleep(textspeed)
                  playerhealth = 0
                  deathscreen("attempting to float through a shallow river (recognize what folks say about the river depth)")
                  daynum = -1
              midday = 2
              event = -10
              shortinput = 0
             
            #driving  
            if shortinput == "1":
              print("you attempt to drive across the river")
              time.sleep(textspeed)
              shortrandom = random.randint(1,5)
              if shortrandom == 1:
                print("you slam into a rock and suffer major damage")
                time.sleep(textspeed)
                print("would you like to use spare parts to magiclly save you?")
                print("(1) yes")
                shortinput2 = input("")
                if shortinput2 == "1":
                  if parts >= 1:
                    print("you are saved, you make it to the other side")
                    parts -= 1
                    time.sleep(textspeed)
                  else:
                    print("you do not have any spare parts")
                    time.sleep(textspeed)
                    playerhealth = 0
                    deathscreen("hitting a rock and not having spare parts (buy spare parts at the shop at the start)")
                    daynum = -1
              else:
                print("you make it across flawlessly!")
                time.sleep(textspeed)
                
      
              
              midday = 2
              event = -10
              shortinput = 0
            midday = 2
            event = -10
            shortinput = 0
      
          #DEEP RIVER ///////////////////////////////
          while event == 9:
            shortinput = input("")
      
            #driving
            if shortinput == "1":
              print("you attempt to drive through the river")
              time.sleep(textspeed)
              print("the river is too deep, you sink under")
              time.sleep(textspeed)
              print("would you like to use spare parts to magiclly save you?")
              print("(1) yes")
              shortinput2 = input("")
              if shortinput2 == "1":
                if parts >= 1:
                  print("you are saved, you make it to the other side")
                  parts -= 1
                  time.sleep(textspeed)
                else:
                  print("you do not have any spare parts")
                  time.sleep(textspeed)
                  playerhealth = 0
                  deathscreen("attempting to drive through a deep river (recognize what folks say about the river depth)")
                  daynum = -1
              midday = 2
              event = -10
              shortinput = 0
             
            #floating  
            if shortinput == "2":
              print("you attempt to float across the river")
              time.sleep(textspeed)
              shortrandom = random.randint(1,5)
              if shortrandom == 1:
                print("you hit a rock and suffer major damage")
                time.sleep(textspeed)
                print("would you like to use spare parts to magiclly save you?")
                print("(1) yes")
                shortinput2 = input("")
                if shortinput2 == "1":
                  if parts >= 1:
                    print("you are saved, you make it to the other side")
                    parts -= 1
                    time.sleep(textspeed)
                  else:
                    print("you do not have any spare parts")
                    time.sleep(textspeed)
                    playerhealth = 0
                    deathscreen("hitting a rock and not having any spare parts (buy spare parts from the starter shops)")
                    daynum = -1
              else:
                print("you make it across flawlessly!")
                time.sleep(textspeed)
                
      
              
              midday = 2
              event = -10
              shortinput = 0
      
          #GIVER ////////////////////////////////////
          while event == 10:
            shortinput = input("")
            if shortinput == "1":
              print("a pig appears")
              time.sleep(textspeed)
              print("\033[H\033[2J", end="")
              print('"welcome to my domain"')
              time.sleep(textspeed)
              print('"my game is simple, i ask questions, you answer"')
              time.sleep(textspeed)
              print('"you will then ask a favor, and i shall answer"')
              time.sleep(textspeed)
              print('"***i advise against being too greedy***"')
              time.sleep(textspeed)
              print('"lets begin"')
              time.sleep(textspeed)
              givergame = "1"
              
              while givergame == "1":
                correctanswergiver = 0
                shortrandom = random.randint(1,5)
          
                if shortrandom == 1:
                  questionone()
                  shortinput2 = input("")
                  if shortinput2 == "3":
                    correctanswergiver = 1
                  else:
                    manuroll(8)
                if shortrandom == 2:
                  questiontwo()
                  shortinput2 = input("")
                  if shortinput2 == "2":
                    correctanswergiver = 1
                  else:
                    manuroll(8)
                if shortrandom == 3:
                  questionthree()
                  shortinput2 = input("")
                  if shortinput2 == "3":
                    correctanswergiver = 1
                  else:
                    manuroll(8)
                if shortrandom == 4:
                  questionfour()
                  shortinput2 = input("")
                  if shortinput2 == "2":
                    correctanswergiver = 1
                  else:
                    manuroll(8)
                if shortrandom == 5:
                  questionfive()
                  shortinput2 = input("")
                  if shortinput2 == "1":
                    correctanswergiver = 1
                  else:
                    manuroll(8)
                  
                print("\033[H\033[2J", end="")
                print('"do you know the consequences of a incorrect answer?"')
                time.sleep(textspeed)
                print('"it is time for me to answer"')
                time.sleep(textspeed)
                print('"what favor benifits your journey the most?"')
                time.sleep(0.5)
                print("(1) a special item capable of reaching wonders")
                time.sleep(0.5)
                print("(2) tools to make my encounters favorable")
                time.sleep(0.5)
                print("(3) a wish nearing unlimited strength")
                giverwantinput = input("")
                
                if correctanswergiver == 1:
                  if giverwantinput == "1":
                    terminus = 2
                    
                  if giverwantinput == "2":
                    folkcorpbeacon += 2
                
                  if giverwantinput == "3":
                    f1health = 20
                    f2health = 20
                    f3health = 20
                    playerhealth = 0
                
                else:
                  if giverwantinput == "1":
                    terminus = 1
                    
                  if giverwantinput == "2":
                    folkcorpbeacon += 1
                    if folkcorpbeacon %2 == 0:
                      folkcorpbeacon += 1
                    
                
                  if giverwantinput == "3":
                    f1health = 2
                    f2health = 2
                    f3health = 2
                    playerhealth = 2
                
                print('"given"')
                time.sleep(textspeed)
                giveriteration += 1
                print('"would you like to go for round', giveriteration + 1, '?"')
                print("(1) yes")
                print("(2) no")
                givergame = input("")
                if givergame == "1":
                  if giveriteration == 4:
                    print('"leave..."')
                    time.sleep(textspeed)
                    break
                  print("noted")
                  time.sleep(textspeed)
                else:
                  givergame = 0
                  break
                
                print(giveriteration)
                time.sleep(textspeed)
                
              
          
            if shortinput == "2":
              print("you leave the house scaredy cat")
              time.sleep(textspeed)
            if giveriteration == 4:
              print("\033[H\033[2J", end="")
              print("you leave the house... something feels off")
              time.sleep(textspeed)
              print("everything around you is white, you cant escape the house's yard")
              time.sleep(textspeed)
              print('"this is what happens to the ones who cant control greed"')
              time.sleep(textspeed)
              print('"have fun"')
              quit()
            midday = 2
            event = -10
            shortinput = 0
      
          #ANGRYSPINO ////////////////////////////////
          while event == 11:
            shortinput = input("")
            while shortinput == "1":
              if folkfood >= 1:
                print("you feed spencer folkfood")
                time.sleep(textspeed)
                print('"YOU MAY GO"')
                break
              elif momsmeal >= 1:
                print("you feed spencer moms thanksgiving diner")
                time.sleep(textspeed)
                print('"YOU MAY GO"')
                break
              else:
                print('"YOU DO NOT HAVE FOOD"')
                time.sleep(textspeed)
                print('"YOU WILL BE MY FOOD"')
                time.sleep(textspeed)
                playerhealth = 0
                deathscreen("attempting to feed spencer food without having food (have food or feed folk)")
                break
                
            while shortinput == "2":
              if f1health > 0:
                print("you feed spencer", folk1name)
                f1health = 0
                time.sleep(textspeed)
                print('"YOU MAY GO"')
                break
              elif f2health > 0:
                print("you feed spencer", folk2name)
                f2health = 0
                time.sleep(textspeed)
                print('"YOU MAY GO"')
                break
              elif f3health > 0:
                print("you feed spencer", folk3name)
                f3health = 0
                time.sleep(textspeed)
                print('"YOU MAY GO"')
                
                break
              else:
                print('"you dont have any friends do you?"')
                time.sleep(textspeed)
                print('"you will be my perfect meal"')
                time.sleep(textspeed)
                playerhealth = 0
                deathscreen("attempting to feed spencer folks without having folks (have folks or feed food?)")
                break
              if shortinput == "3":
                print("you attempt to escape the situation")
                time.sleep(textspeed)
                shortrandom = random.randint(1,4)
                if shortrandom == 1:
                  print("you get away safely!")
                else:
                  print("spencer catches up")
                  time.sleep(textspeed)
                  print("the last thing you feel is the teeth on your skin")
                  time.sleep(textspeed)
                  playerhealth = 0
                  deathscreen("attempting to run away from a spinosaurus (good thinking)")
                  
              
              
                
            time.sleep(textspeed)
            midday = 2
            event = -10
            shortinput = 0
      
          #STAN /////////////////////////////////
          
          while event == 12:
            manuroll(6)
            starttime = time.perf_counter()
            shortinput = input("")
            if shortinput == "1":
              if folkmusket >= 1:
                print("you draw your folkmusket")
                time.sleep(textspeed)
                for i in range(int(math.ceil(daynum / 2))):
                  if ammo <= 0:
                    print("*click* you gun doesnt seem to have ammo")
                    time.sleep(textspeed)
                    print("the figure doesnt relent")
                    time.sleep(textspeed)
                    print("darkness")
                    playerhealth = 0
                    deathscreen("stan (have a gun with ammo at hand)")
                    time.sleep(textspeed)
                    break
                  if ammo >= 1:
                    print("*gunshot*")
                    time.sleep(textspeed)
                    ammo -= 1 
                    
      
                if playerhealth == 0:
                  break
                endtime = time.perf_counter()
                inputtime = endtime - starttime
                if inputtime >= 20:
                  print("the relentless creature has already approached")
                  time.sleep(textspeed)
                  print("darkness")
                  playerhealth = 0
                  deathscreen("stan (react faster)")
                  daynum = -1
                  time.sleep(textspeed)
                  break
                  
                print("the figure is drawn back into the night through black fog")
                time.sleep(textspeed)
                print("the night is silent once again")
                time.sleep(textspeed)
      
              else:
                print("you dont have a gun")
                time.sleep(textspeed)
                shortinput = "2"
            if shortinput == "2":
              print("the figure doesnt relent")
              time.sleep(textspeed)
              print("darkness")
              playerhealth = 0
              deathscreen("stan (have a gun with ammo at hand)")
              daynum = -1
              time.sleep(textspeed)
              break
          
                  
            midday = 2
            event = -10
            shortinput = 0
            
      
         
      #/////// end of event wave 1 ///////////
      
      
          
          #MILI'S STORE /////////////////
          while event == 13:
            milishopbuy = 0
            shortinput = input("")
            while shortinput == "1":
              if playerhealth == 0:
                deathscreen("sacrificing too much of yourself to mili (buy less from her)")
              milishop()
              shortintinput = input("")
              if shortintinput == "1":
                print("\033[H\033[2J", end="")
                print('"gluttony, the pure desire for food"')
                print("gives you plenty of food!")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  gluttonyitem = 1
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
              
              if shortintinput == "2":
                print("\033[H\033[2J", end="")
                print('"wrath, the pure desire for kill"')
                print("kills every possible living character in your adventure! (will not work on certain characters)")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  wrathitem = 1
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
      
              if shortintinput == "3":
                print("\033[H\033[2J", end="")
                print('"pride, the pure desire for ego"')
                print("heals you for 10 hp!")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  prideitem = 1
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
      
              if shortintinput == "4":
                print("\033[H\033[2J", end="")
                print('"greed, the pure desire for wealth"')
                print("gives you random amounts of george!")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
                  greeditem = 1
                  
              if shortintinput == "5":
                print("\033[H\033[2J", end="")
                print('"lust, my favorite."')
                print("will enter you in mili's trial")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
                  lustitem = 1
      
              if shortintinput == "6":
                print("\033[H\033[2J", end="")
                print('"envy, the pure desire for status"')
                print("heals you for 20 hp!")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
                  envyitem = 1
      
              if shortintinput == "7":
                print("\033[H\033[2J", end="")
                print('"sloth, the pure desire for ease"')
                print("gives you the serene effect for the next day")
                print("every item has its concenquences")
                print("are you willing to gamble with the immoral oppurtunity")
                print("press 1 to buy, 0 to go back")
                shortinput2 = input("")
                if shortinput2 == "1":
                  print("thank you servant...")
                  playerhealth -= 5
                  shortintinput = 0
                  shortinput2 = 0
                  milishopbuy = 1
                  slothitem = 1
      
              if shortintinput == "8":
                if milishopbuy != 1:
                  print('"you think i will let you leave without buying anything?"')
                  time.sleep(textspeed)
                  playerhealth -= 3
                  if playerhealth <= 0:
                    deathscreen("mili's stab (dont leave without buying something)")
                  print("she stabs you with a knife, and disapears into the darkness")
                  time.sleep(textspeed)
                  print("you are left to process the past expericnce you just encountered")
                else:
                  print('"thank you loyal servant"')
                  time.sleep(textspeed)
                  print("she opens the door behind you")
                  time.sleep(textspeed)
                  print('"good bye c;"')
                time.sleep(textspeed)
                midday = 2
                event = -10
                shortinput = 0
                
            if shortinput == "2":
              print('"you think i will let you leave without buying anything?"')
              time.sleep(textspeed)
              playerhealth -= 3
              if playerhealth <= 0:
                  deathscreen("mili's stab (dont leave without buying something)")
              print("she stabs you with a knife, and disapears into the darkness")
              time.sleep(textspeed)
              print("you are left to process the past expericnce you just encountered")
              midday = 2
              event = -10
              shortinput 
      
          #CHILLNIGHT/////////////////////////
          while event == 14:
            shortinput = input("")
            if shortinput == "1":
              midday = 2
              event = -10
              shortinput = 0
              
          #FLOWERFIELD ///////////////////
          while event == 15:
            shortinput = input("")
            if shortinput == "1":
              fcfolk1 = 1
              fcfolk2 = 1
              fcfolk3 = 1
              fcplayer = 1
              manuroll(10)
              fcstage = 1
              midday = 2
              event = -10
              shortinput = 0
              
          #MATHTEST///////////////////////////
          while event == 16:
            wronganswer = 0
            shortinput = input("")
            if shortinput == "1":
              for i in range(3):
                mtnum1 = random.randint(1,20)
                mtnum2 = random.randint(1,20)
                mtnum3 = random.randint(1,20)     
                mtoplist = [
                  "+",
                  "-",
                  "*",
                  "/"
                ]
                mtop1 = random.randint(0,2)
                mtop1 = mtoplist[mtop1]
                mtop2 = random.randint(0,2)
                mtop2 = mtoplist[mtop2]
                
                print("\033[H\033[2J", end="")
                print(mtnum1, mtop1, mtnum2, mtop2, mtnum3, "?")
                mtq = f"{mtnum1} {mtop1} {mtnum2} {mtop2} {mtnum3}"
                mtans = eval(mtq)
                #print(mtans)
                print("enter answer (you have 15 seconds)")
                starttime = time.perf_counter()
                shortinput = input("")
                endtime = time.perf_counter()
                inputtime = endtime - starttime
                if inputtime > 15:
                  playerhealth -= 3
                  print("you were too slow")
                  time.sleep(textspeed)
                  print("you are stabbed by a unknown force into your back")
                  time.sleep(textspeed)
                  incorrectanswer += 1
                elif str(mtans) == shortinput:
                  print("correct!")
                  time.sleep(textspeed)
                else:
                  print("incorrect...")
                  playerhealth -= 3
                  time.sleep(textspeed)
                  print("you are stabbed by a unknown force into your back")
                  time.sleep(textspeed)
              if playerhealth <= 0:
                deathscreen("the entities spike (answer the questions correctly and in time)")
              print("the darkness suddenly dissapates around you,")
              midday = 2
              event = -10
              shortinput = 0
            else: 
              shortinput = ""
              manuroll(1)
              
          #MOUNTAIN///////////////////////////  YESSSSSSSSSSSSSSSSSSSSSSSSSS FINALLYYYYYYYYY
          while event == 17:
            
            shortinput2 = input("")
            
            #through
            if shortinput2 == "1":
              if pickaxe >= 1:
                mountaintext(1)
                shortinput = input("")
                shortrandom = random.randint(1,2)
                #escape
                if shortrandom == 1:
                  mountaintext(2)
                  midday = 2
                  event = -10
                  shortinput = 0
                  break
      
                #split cave
                if shortrandom == 2: 
                  mountaintext(3)
                  shortinput = input("")
                  shortrandom = random.randint(1,3)
      
                  #escape
                  if shortrandom == 1:
                    mountaintext(2)
                    midday = 2
                    event = -10
                    shortinput = 0
                    break
                  #agent s
                  if shortrandom == 2:
                    mountaintext(4)
                    playerhealth = 0
                    deathscreen("killed by the gem serpent (unlucky)")
                    midday = 2
                    event = -10
                    shortinput = 0
                    break
                  #feathered serpent
                  if shortrandom == 3:
                    mountaintext(5)
                    shortinput = input("")
                    if shortinput == 2 and terminus >= 1:
                      terminus = 0
                      print('"thank you for my artifact"')
                      time.sleep(textspeed)
                      print("PLAYER WIN TEXT")
                      """
                      PLAYERWIN
                      """
      
                    else:
                      print('"why do you even show your face here"')
                      time.sleep(textspeed)
                      print('"nor do i care about your answer"')
                      time.sleep(textspeed)
                      print('"leave"')
                      time.sleep(textspeed)
                      print("before you get the chance to leave the area, everything goes dark in a instant")
                      playerhealth = 0
                      deathscreen("feathered dragon (obtain wish from the giver)")
                      midday = 2
                      event = -10
                      shortinput = 0
                      break
              else:
                print("you dont have a pickaxe to go through the mountain")
                time.sleep(textspeed)
                shortinput = 0
            
            #above      
            while shortinput2 == "2":
              mountaintext(6)
              shortinput = input("")
      
              #PATH 1: TREE + LAKE (NO BACK)
              if shortinput == "1":
             
                mountaintext(7)
                shortinput = input("")
      
                #BOULDER 
                if shortinput == "1":
                  mountaintext(8)
                  shortinput = input("")
                  if shortinput == "1":
                    mountaintext(9)
                    playerhealth -= 1
                    if playerhealth <= 0:
                      deathscreen("blood infusion with a tree (dont approach the tree with 1 health)")
                    shortinput = input("")
                    if shortinput == "1":
                      if showprincess == 2:
                        mountaintext(40)
                        tooth += 1
                        
                      mountaintext(12)
                      shortinput = input("")
                      if shortinput == "1":
                        mountaintext(13)
                        shortrandom = random.randint(1,3)
                        shortinput = input("")
                        if shortrandom == 1 or shortrandom == 2:
                          mountaintext(14)
                          shortrandom = 0
                          shortinput = 0
                          shortinput2 = 0
                          midday = 2
                          event = -10
                        else:
                          mountaintext(15)
                          shortrandom = 0
                          shortinput = 0
                          shortinput2 = 0
                          playerhealth = 0
                          deathscreen("the blizzard (unlucky)")
                          midday = 2
                          event = -10
                             
                #TREE
                elif shortinput == "2":
                  mountaintext(10)
                  playerhealth = 0
                  deathscreen("observing the crimson tree first (observe rocks)")
                  break
      
                #TRAIL
                elif shortinput == "3":
                  mountaintext(11)
                  playerhealth = 0
                  deathscreen("hypothermia (obtain the blessing from the rocks)")
                  break
      
              #PATH 2: VINDAGNYR
              if shortinput == "2":
                mountaintext(16)
                if dontresettime == 0:
                  starttime = time.perf_counter()
                  dontresettime = 1
              while shortinput == "2":
                mountaintext(17)
                shortinput3 = input("")
                endtime = time.perf_counter()
               
                if endtime - starttime >= 30 and showprincess <= 1:
                  mountaintext(31)
                  shortinput3 = 0
                  midday = 2
                  event = -10
                  shortinput = 0
                  shortinput2 = 0
                  playerhealth = 0
                  deathscreen("the heavenly punishment (leave the town in time, or change fate with the princess/crowd)")
                  
                if shortinput3 == "1":
                  mountaintext(18)
      
                #talk to shop person
                while shortinput3 == "1":
                  mountaintext(18.5)
                  shortinput5 = input("")
      
                  #store 
                  while shortinput5 == "1":
                    mountaintext(19)
                    shortinput4 = input("")
      
                    #strange tooth
                    if shortinput4 == "1":
                      if tooth <= 1:
                        print("are you sure you want to purchase a strange tooth?...\n (1) yes (2) no")
                        shortinput4 = input("")
                        if shortinput4 == "1":
                          if george >= 5:
                            george -= 5
                            print("you bought a strange tooth")
                            tooth += 1
                            time.sleep(textspeed)
                            shortinput4 = 0
                          else:
                            print("you do not have enough george")
                            time.sleep(textspeed)
                            shortinput4 = 0
                        else:
                          shortinput4 = 0
                      else:
                        print("you already bought a strange tooth")
                        shortinput4 = 0
      
                    #chilled meat
                    if shortinput4 == "2":
                      print("chilled meat is the local specialty (functions the same as folkfood)")
                      print("may be used in other specific event")
                      print("how much chilled meat do you want (type a number)")
                      print("george balance:", george)
                      shortinput4 = input()
                      shortinput4 = int(shortinput4)
                      george = george - shortinput4 * 2
                      if george < 0:
                        print("\033[H\033[2J", end="")
                        print("you dont have enough money for this")
                        george = george + shortinput4 * 2
                        time.sleep(textspeed)
                        shortinput4 = 0
                      else:
                        print("\033[H\033[2J", end="")
                        chillmeat = chillmeat + shortinput4
                        print("you bought", shortinput4, "chilled meat")
                        time.sleep(textspeed)
                        shortinput4 = 0
      
                    #ammo
                    if shortinput4 == "3":
                      print("how much ammo do you want (type a number)")
                      print("george balance:", george)
                      shortinput4 = input()
                      shortinput4 = int(shortinput4)
                      george = george - shortinput4
                      if george < 0:
                        print("\033[H\033[2J", end="")
                        print("you dont have enough money for this")
                        george = george + shortinput4 
                        shortinput4 = 0
                        time.sleep(textspeed)
                      else:
                        print("\033[H\033[2J", end="")
                        ammo = ammo + shortinput4
                        print("you bought", shortinput4, "ammo")
                        shortinput4 = 0
                        time.sleep(textspeed)
                          
                    #pickaxe
                    if shortinput4 == "4":
                      print("how many pickaxes do you want (type a number)")
                      print("george balance:", george)
                      shortinput4 = input()
                      shortinput4 = int(shortinput4)
                      george = george - shortinput4 * 4
                      if george < 0:
                        print("\033[H\033[2J", end="")
                        print("you dont have enough money for this")
                        george = george + shortinput4 * 4 
                        shortinput4 = 0
                        time.sleep(textspeed)
                      else:
                        print("\033[H\033[2J", end="")
                        pickaxe = pickaxe + shortinput4
                        print("you bought", shortinput4, "pickaxe")
                        shortinput4 = 0
                        time.sleep(textspeed)
      
                    #nvm
                    if shortinput4 == "5":
                      shortinput5 = 0
                      
      
                  #situation
                  if shortinput5 == "2":
                    mountaintext(20)
                    time.sleep(textspeed)
                    shortinput4 = input()
                    
      
                  #crowd
                  elif shortinput5 == "3" and showprincess == 0:
                    mountaintext(21)
                    time.sleep(textspeed)
                    shortinput4 = input()
                    
      
                  #back
                  elif  shortinput5 == "3" and showprincess >= 1:
                    shortinput3 = 0
      
                  elif shortinput5 == "4":
                    shortinput3 = 0
      
                #talk to princess
                if shortinput3 == "2" and showprincess == 0:
                  mountaintext(22)
                  shortinput4 = input("")
                  while shortinput3 == "2":
                    mountaintext(23)
                    shortinput4 = input("")
        
                    #goofball talk
                    if shortinput4 == "1":
                      mountaintext(24)
                      shortinput5 = input("")
                      
                      if shortinput5 == "1":
                        print("Useless...")
                        time.sleep(textspeed)
                        shortinput4 = 0 
                        shortinput3 = 0
                        showprincess = 1
                        mountaintext(28)
                      else:
                        shortinput4 = 0
        
                    #fix reign
                    if shortinput4 == "2":
                      shortrandom = random.randint(1,4)
                      mountaintext(25)
                      shortinput5 = input("")
                      if shortrandom == 1 and shortinput5 == "2":
                        mountaintext(27)
                        shortinput4 = "0"
                        shortinput3 = "0"
                        showprincess = 2
                     
                      else:
                        mountaintext(26)
                        showprincess = 1
                        shortinput3 = "0"
                        shortinput4 = "0"
      
                    #answer from the gods
                    if shortinput4 == "3":
                      mountaintext(25)
                      shortinput5 = input("")
                      if shortinput5 == "2":
                        mountaintext(27)
                        shortinput4 = "0"
                        shortinput3 = "0"
                        showprincess = 2
                     
                      else:
                        mountaintext(26)
                        showprincess = 1
                        shortinput3 = "0"
                        shortinput4 = "0"
                elif shortinput3 == "2" and showprincess > 0:
                  shortinput3 = 3
      
                #trail
                if (shortinput3 == "3" and showprincess == 0) or shortinput3 == 3:
                  if showprincess == 2:
                    mountaintext(30)
                    time.sleep(textspeed)
                    shortinput3 = 0
                    midday = 2
                    event = -10
                    shortinput = 0
                    shortinput2 = 0
                 
                  else:
                    mountaintext(29)
                    shortinput3 = 0
                    midday = 2
                    event = -10
                    shortinput = 0
                    shortinput2 = 0
                    playerhealth = 0
                    deathscreen("avalanche from the heavenly punishment (talk to princess/crowd)")
                
                elif shortinput3 == "3" and showprincess >= 1: 
                  shortinput = 0
      
                if shortinput3 == "4" and showprincess == 0:
                  shortinput = 0
                    
              #PATH 3: MOUNTAIN
              if shortinput == "3":
                mountaintext(32)
                shortinput2 = input("")
               
                if shortinput2 == "1":
                  mountaintext(33)
                  shortinput2 = input("")
      
                  #no punishment
                  if showprincess == 2:
                    mountaintext(35)
                    playerhealth += 5
                    f1health += 5
                    f2health += 5
                    f3health += 5
                    midday = 2
                    manuroll(7)
                    event = -10
                    shortinput2 = 0
      
                  else:
                    mountaintext(34)
                    starttime = time.perf_counter()
                    shortinput2 = input("")
                    endtime = time.perf_counter()
      
                    if endtime - starttime >= 10:
                      print("\033[H\033[2J", end="")
                      print("you dont have time, the rock is already in lethal range")
                      time.sleep(textspeed)
                      print("a unstoppable force will not wait for a futile response")
                      time.sleep(textspeed)
                      shortinput = 0
                      shortinput2 = 0
                      playerhealth = 0
                      deathscreen("the heavenly punishment (input faster)")
                      midday = 2
                      event = -10
      
                    #use sword
                    elif shortinput2 == "1":
                      if folkrapier >= 1:
                        print("\033[H\033[2J", end="")
                        print("you brace, holding the folk rapier at ready")
                        time.sleep(textspeed)
                        print("one slice...")
                        time.sleep(textspeed)
                        mountaintext(36)
                        meteor += 1
                        shortinput2 = 0
                        midday = 2
                        event = -10
                        manuroll(7)
                      
                      elif folksword >= 1:
                        print("\033[H\033[2J", end="")
                        print("you brace, holding the folk sword at ready")
                        time.sleep(textspeed)
                        print("one slice is not powerful enough")
                        time.sleep(textspeed)
                        print("a unstoppable force will not wait for a futile response")
                        playerhealth = 0
                        deathscreen("the heavenly punishment (use folk rapier)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
      
                      else:
                        print("\033[H\033[2J", end="")
                        print("you brace, holding your fists at ready")
                        time.sleep(textspeed)
                        print("one punch is not powerful enough")
                        time.sleep(textspeed)
                        print("a unstoppable force will not wait for a futile response")
                        playerhealth = 0
                        deathscreen("the heavenly punishment (use folk rapier)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
      
                    #use gun
                    elif shortinput2 == "2":
                      if folkrifle >= 1 and ammo >= 1:
                        print("\033[H\033[2J", end="")
                        print("you brace, aiming the folk rifle steady")
                        time.sleep(textspeed)
                        print("one shot...")
                        time.sleep(textspeed)
                        mountaintext(36)
                        manuroll(7)
                        meteor += 1
                        shortinput2 = 0
                        midday = 2
                        event = -10
                      
                      elif folkmusket >= 1 and ammo >= 1:
                        print("\033[H\033[2J", end="")
                        print("you brace, aiming the folkmusket steady")
                        time.sleep(textspeed)
                        print("one shot is not powerful enough")
                        time.sleep(textspeed)
                        print("a unstoppable force will not wait for a futile response")
                        playerhealth = 0
                        deathscreen("the heavenly punishment (use folk rifle)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
                     
                      else:
                        print("\033[H\033[2J", end="")
                        print("you brace, attempting to blow the rock up with your mind")
                        time.sleep(textspeed)
                        print("one thought is not powerful enough")
                        time.sleep(textspeed)
                        print("a unstoppable force will not wait for a futile response")
                        playerhealth = 0
                        deathscreen("the heavenly punishment (use folk rifle)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
      
                    #pray
                    elif shortinput2 == "3":
                      shortrandom = random.randint(1,4)
                      
                      if shortrandom == 1:
                        print("\033[H\033[2J", end="")
                        print("you pray, hopeing for any support")
                        time.sleep(textspeed)
                        print("...")
                        time.sleep(textspeed)
                        mountaintext(36)
                        specialinventory["(meteor) meteoric rock"] = 0
                        specialinventory["(meteor) meteoric rock"] += 1
                        shortinput2 = 0
                        midday = 2
                        event = -10
      
                      else:
                        print("\033[H\033[2J", end="")
                        print("you pray, hopeing for any support")
                        time.sleep(textspeed)
                        print("...")
                        time.sleep(textspeed)
                        print("nothing happens")
                        time.sleep(textspeed)
                        print("a unstoppable force will not wait for a futile response")
                        playerhealth = 0
                        deathscreen("the heavenly punishment (use weapons to destroy the rock)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
                        
                    #run
                    else:
                      print("you run??")
                      time.sleep(textspeed)
                      print("the rock doesnt stop?")
                      time.sleep(textspeed)
                      print("what did you expect??")
                      playerhealth = 0
                      deathscreen("the heavenly punishment (being a idiot))")
                      shortinput2 = 0
                      midday = 2
                      event = -10
      
                if shortinput2 == "2":
                  mountaintext(37)
                  starttime2 = time.perf_counter()
                  shortinput2 = input("")
                  if shortinput2 == "1":
                    
                    if pickaxe >= 1:
                      mountaintext(38)
                      shortinput2 = input("")
                      endtime2 = time.perf_counter()
                      if endtime2 - starttime2 == 10:
                        mountaintext(39)
                        playerhealth = 0
                        deathscreen("freezing near the lake (input faster)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
                      else:
                        tooth += 1
                        shortinput2 = "2"
                    
                    else:
                      print("you do not have a pickaxe")
                      shortinput2 = input("")
                      endtime2 = time.perf_counter()
                      if endtime2 - starttime2 >= 10:
                        mountaintext(39)
                        playerhealth = 0
                        deathscreen("freezing near the lake (input faster)")
                        shortinput2 = 0
                        midday = 2
                        event = -10
                      else:
                        shortinput2 = "2"             
                      
          
            if playerhealth == 0:
              midday = 2
              event = -10
              shortinput = 0
              break
      
          #BAYBAKI//////////////////////////////
          while event == 18:
            print("\033[H\033[2J", end="")
            spungun = 0
             #decide start
            rrturn = random.randint(1,5)
            bulletlocation = random.randint(1,6)
            rrgameactive = 1
           
            while rrgameactive == 1:
              if rrturn == 1:
                print("\033[H\033[2J", end="")
                print("the gun is given to you")
                time.sleep(textspeed)
                print("(1) spin gun and shoot")
                time.sleep(textspeed)
                print("(2) shoot")
                shortinput = input("")
        
                if shortinput == 1:
                  spungun = 1
                  bulletlocation = random.randint(1,6)
                  print("you spin the gun")
                  time.sleep(textspeed)
                  
                print("you put the gun to your head")
                time.sleep(textspeed)
                print("\033[H\033[2J", end="")
                print("...")
                time.sleep(textspeed)
               
                if bulletlocation == 1:
                  playerhealth = 0
                  deathscreen("roulette (shot yourself)")
                  rrgameactive = 0
                  event = -10
                  midday = 2
                else:
                  print("...click...")
                  time.sleep(textspeed)
                  bulletlocation -= 1
                  rrturn += 1
                  
              elif rrturn == 2:
                print("\033[H\033[2J", end="")
                print("the gun is given to", folk1name)
                
                shortrandom = random.randint(0,1)
                if shortrandom == 1:
                  time.sleep(textspeed)
                  bulletlocation = random.randint(1,6)
                  print("they spin the gun")
                time.sleep(textspeed)
                print("they put the gun to their head")
                time.sleep(textspeed)
                print("\033[H\033[2J", end="")
                print("...")
                time.sleep(textspeed)
               
                if bulletlocation == 1:
                  f1health = 0
                  print("the gun fires, killing", folk1name)
                  time.sleep(textspeed)
                  print('"good work, ill be on my way"')
                  time.sleep(textspeed)
                  print("baybaki disappears with the chairs, the table, and your dead folk")
                  time.sleep(textspeed)
                  rrgameactive = 0
                  event = -10
                  midday = 2
                else:
                  print("...click...")
                  time.sleep(textspeed)
                  bulletlocation -= 1
                  rrturn += 1
                  
              elif rrturn == 3:
                print("\033[H\033[2J", end="")
                print("the gun is given to", folk2name)
                
                shortrandom = random.randint(0,1)
                if shortrandom == 1:
                  time.sleep(textspeed)
                  bulletlocation = random.randint(1,6)
                  print("they spin the gun")
                time.sleep(textspeed)
                print("they put the gun to their head")
                time.sleep(textspeed)
                print("\033[H\033[2J", end="")
                print("...")
                time.sleep(textspeed)
               
                if bulletlocation == 1:
                  f2health = 0
                  print("the gun fires, killing", folk2name)
                  time.sleep(textspeed)
                  print('"good work, ill be on my way"')
                  time.sleep(textspeed)
                  print("baybaki disappears with the chairs, the table, and your dead folk")
                  time.sleep(textspeed)
                  rrgameactive = 0
                  event = -10
                  midday = 2
                else:
                  print("...click...")
                  time.sleep(textspeed)
                  bulletlocation -= 1
                  rrturn += 1
              
              elif rrturn == 4:
                print("\033[H\033[2J", end="")
                print("the gun is given to", folk3name)
                
                shortrandom = random.randint(0,1)
                if shortrandom == 1:
                  time.sleep(textspeed)
                  bulletlocation = random.randint(1,6)
                  print("they spin the gun")
                time.sleep(textspeed) 
                print("they put the gun to their head")
                time.sleep(textspeed)
                print("\033[H\033[2J", end="")
                print("...")
                time.sleep(textspeed)
               
                if bulletlocation == 1:
                  f3health = 0
                  print("the gun fires, killing", folk3name)
                  time.sleep(textspeed)
                  print('"good work, ill be on my way"')
                  time.sleep(textspeed)
                  print("baybaki disappears with the chairs, the table, and your dead folk")
                  time.sleep(textspeed)
                  rrgameactive = 0
                  event = -10
                  midday = 2
                else:
                  print("...click...")
                  time.sleep(textspeed)
                  bulletlocation -= 1
                  rrturn += 1
              
              elif rrturn == 5:
                print("\033[H\033[2J", end="")
                print("the gun is given to baybaki")
                
                shortrandom = random.randint(0,1)
                if shortrandom == 1:
                  time.sleep(textspeed)
                  bulletlocation = random.randint(1,6)
                  print("he spins the gun")
                
                time.sleep(textspeed)
                print("he puts the gun to his head")
                time.sleep(textspeed)
                print("\033[H\033[2J", end="")
                print("...")
                time.sleep(textspeed)
               
                if bulletlocation == 1:
                  print("the gun fires, killing baybaki")
                  time.sleep(textspeed)
                  print("you watch as everything disappears")
                  time.sleep(textspeed)
                  baybakidead = 1
                  rrgameactive = 0
                  event = -10
                  midday = 2
                else:
                  print("...click...")
                  time.sleep(textspeed)
                  bulletlocation -= 1
                  rrturn = 1

            manuroll(3)
      
          #ENCHANTED WOODS
          while event == 19:
            shortinput = input("")
            if shortinput == "1":
              print("")
              shortrandom = random.randint(1,20)
              if debugmode == 1:
                shortrandom = input("1-20 roll id?")
              print("\033[H\033[2J", end="")
              print("you feel into the grass, feeling through the strange pool of objects")
              time.sleep(textspeed)
              print("you feel something...")

              
              
              if shortrandom == 19:
                print("you pull it out...")
                time.sleep(textspeed)
                print(f"wow! you got a {color.red}folk rapier{color.white}!")
                folkrapier += 1
      
              if shortrandom == 20:
                print("you pull it out...")
                time.sleep(textspeed)
                print(f"wow! you got a {color.red}folk rifle{color.white}!")
                folkrifle += 1     
      
          
          if playerhealth > 0:
            print("\033[H\033[2J", end="")
            print("END OF EVENT:", eventname)
            print("press 1 to go next")
            shortinput = input("")
            timeresult = 0    
            savedticknum = tickamm 

        elif timeresult == "DONE":
          print("\033[H\033[2J", end="")
          print("you make it to a sea, the sides of the valley a cliff to the shore")
          time.sleep(textspeed)
          print("there is nowhere to go, you move torwards the water regardless")
          time.sleep(textspeed)
          print(f"{color.red}as you touch the water, you fall through everything, entering void below the valley...")
          time.sleep(textspeed)
          print("\033[H\033[2J", end="")
          print(f"{color.bblue}you passed", simulation)
          print("")
          save = open("savedata.csv", "w")
          save.close()
          
          print("lincoln gain:", ((score // 10) * ((difficulty) * 0.5)))
          lincoln += ((score // 10) * ((difficulty) * 0.5))
          print("")
          print("total lincoln:", lincoln)
          print("press anything to continue")
          shortinput = input("")
          
          file = open("fv.dat", "w")
          file.write(str(lincoln))
          file.close()
      
          runactive = 0
          raise endrun  
          
        else:
          if playerprevioushealth == playerhealth and playerhunger > 50:
            if playerhealth < 10:
              playerhealth += 1
            score += 2
          if f1previoushealth == f1health and f1hunger > 50 and f1health > 0:
            if f1health < 10:
              f1health += 1
            score += 2
          if f2previoushealth == f2health and f2hunger > 50 and f1health > 0:
            if f2health < 10:
              f2health += 1
            score += 2
          if f3previoushealth == f3health and f3hunger > 50 and f1health > 0:
            if f3health < 10:
              f3health += 1
            score += 2
          
          shortinput = 0
      
          if lustactive == 1:
            if f1health <= 0 and lustfolk1 == 0:
              maxhp += 5
              playerhealth += 5
              lustfolk1 = 1
            if f2health <= 0 and lustfolk2 == 0:
              maxhp += 5
              playerhealth += 5
              lustfolk2 = 1
            if f3health <= 0 and lustfolk3 == 0:
              maxhp += 5
              playerhealth += 5
              lustfolk3 = 1
              
          savegame()
          
          while shortinput != "1":
            if playerhealth > maxhp:
              playerhealth = maxhp
            print(f"{color.white}\033[H\033[2J", end="")
            print(timehr, ":", timesec)
            print(f"distance left:", math.ceil(distance))
            print("(1) move forward")
            print("(2) status")
            print("(3) inventory")
            print("(4) actions")
            if active_expansion != 0:
              print("(5) expansion")
              
            shortinput = input("")

            if shortinput == "vrep" and debugmode == 1:
              vrep += 100
  
            if shortinput == ":3" and debugmode == 1:
              score = 1000000
              deathscreen(":3")

            if shortinput == "spinvcheck" and debugmode == 1:
              tooth = 1
              terminus = 1
              rosavale = 1
              wyrmrose = 1
              slyphora = 1
              velisara = 1
              luneblossom = 1
              gluttonyitem = 1
              wrathitem = 1
              prideitem = 1
              greeditem = 1
              lustitem = 1
              envyitem = 1
              slothitem = 1
              folknix = 1
              folkcorpbeacon = 2
              meteor = 1

            if shortinput == "discheck" and debugmode == 1:
              distance = 10
              
            while shortinput == "var":
              print("\033[H\033[2J", end="")
              print(active_expansion)
              print(playerinfectionTimer)
              print(f1infectionTimer)
              print(f2infectionTimer)
              print(f3infectionTimer)
              shortinput = input("")
              
            while shortinput == "2":
              fixnum()
              charstatus()
              shortinput2 = input("")
              if shortinput2 == "0":
                shortinput = 0       
              
            while shortinput == "3":
              if playerhunger > 100 and glutton == 0:
                playerhunger = 100
              if f1hunger > 100:
                f1hunger = 100
              if f2hunger > 100:
                f2hunger = 100
              if f3hunger > 100:
                f3hunger = 100
              gameinventory()
              shortintinput = input("")
          
              #folkfood
              while shortintinput == "1":
                print("\033[H\033[2J", end="")
                print("how much folk food do you want to feed? (type none to go back)")
          
                #ask user input on food
                shortinput2 = input("")
                if shortinput2 == "none":
                  break
                  
                shortinput2 = int(shortinput2)
          
                #check if player has entered food
                if shortinput2 > folkfood:
                  print("you dont have that much folk food!")
                  time.sleep(1.5)
                else:
                  print("who do you want to feed?")
                  print("1: yourself (", math.ceil(playerhunger), ")")
                  if f1health > 0:
                    print("2:", folk1name, "(", math.ceil(f1hunger), ")")
                  if f2health > 0:
                    print("3:", folk2name, "(", math.ceil(f2hunger), ")")
                  if f3health > 0:
                    print("4:", folk3name, "(", math.ceil(f3hunger), ")")
                  shortinput3 = input("")
                  
                  if shortinput3 == "1" and f1health > 0:
                    if playerhunger == 100:
                      print("that character already has full hunger")
                      time.sleep(textspeed)
                    else:
                      for num in range(shortinput2):
                        folkfood -= 1
                        playerhunger += 50 * playerfoodgainmultiplier
                        if playerhunger > 100:
                          playerhunger = 100
                          shortintinput = 0
                          break
                          
                  if shortinput3 == "2" and f2health > 0:
                    if f1hunger == 100:
                      print("that character already has full hunger")
                      time.sleep(textspeed)
                    else:
                      for num in range(shortinput2):
                        folkfood -= 1
                        f1hunger += 50 * f1foodgainmultiplier
                        if f1hunger > 100:
                          f1hunger = 100
                          shortintinput = 0
                          break
                 
                  if shortinput3 == "3" and f3health > 0:
                    if f2hunger == 100:
                      print("that character already has full hunger")
                      time.sleep(textspeed)
                    else:
                      for num in range(shortinput2):
                        folkfood -= 1
                        f2hunger += 50 * f2foodgainmultiplier
                        if f2hunger > 100:
                          f2hunger = 100
                          shortintinput = 0
                          break
      
                  if shortinput3 == "4":
                    if f3hunger == 100:
                      print("that character already has full hunger")
                      time.sleep(textspeed)
                    else:
                      for num in range(shortinput2):
                        folkfood -= 1
                        f3hunger += 50 * f3foodgainmultiplier
                        if f3hunger > 100:
                          f3hunger = 100
                          shortintinput = 0
                          break
                    
              #thanksgivingmeal
              while shortintinput == "2":
                print("\033[H\033[2J", end="")
                print("how many moms thanksgiving meals do you want to feed?")
                print("this feeds 20 to each person")
          
                #ask user input on food
                shortinput2 = input("")
                shortinput2 = int(shortinput2)
          
                #check if player has entered food
                if shortinput2 > momsmeal:
                  print("you dont have that many of moms thanksgiving meals!")
                  time.sleep(1.5)
                else:
                  if playerhunger == 100 and f1hunger == 100 and f2hunger == 100 and f3hunger == 100:
                    print("everyone is fully fed!")
                    time.sleep(textspeed)
                    shortintinput = 0
                  else:
                    for i in range(shortinput2):
                      if playerhunger == 100 and f1hunger == 100 and f2hunger == 100 and f3hunger == 100:
                        break
                      if playerhunger != 100:
                        playerhunger += (20 * playerfoodgainmultiplier)
                      if f1hunger != 100:
                        f1hunger += (20 * f1foodgainmultiplier)         
                      if f2hunger != 100:
                        f2hunger += (20 * f2foodgainmultiplier)        
                      if f3hunger != 100:
                        f3hunger += (20 * f3foodgainmultiplier)  
                      momsmeal -= 1
                    shortintinput = 0
      
              #medibedi
              while shortintinput == "3":
                if medibedi == 0:
                  print("you dont have any medibedis")
                  time.sleep(1.5)
                  break
                print("\033[H\033[2J", end="")
                print("who do you want to heal? (none to go back)")
                print("this adds 5 health to one person (cannot go above 10)")
                print("1: yourself (", playerhealth, ")")
                print("2:", folk1name, "(", f1health, ")")
                print("3:", folk2name, "(", f2health, ")")
                print("4:", folk3name, "(", f3health, ")")
                shortinput3 = input("")
                
                if shortinput3 == "none":
                  break
      
                if shortinput3 == "1" and playerhealth > 10:
                  print(playername, "already has 10 or more health")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "2" and f1health > 10:
                  print(folk1name, "already has 10 or more health")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "3" and f2health > 10:
                  print(folk2name, "already has 10 or more health")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "4" and f3health > 10:
                  print(folk3name, "already has 10 or more health")
                  time.sleep(1.5)
                  continue
      
                if shortinput3 == "1" and playerhealth == 0:
                  print(playername, "is dead!")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "2" and f1health == 0:
                  print(folk1name, "is dead")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "3" and f2health == 0:
                  print(folk2name, "is dead")
                  time.sleep(1.5)
                  continue
                if shortinput3 == "4" and f3health == 0:
                  print(folk3name, "is dead")
                  time.sleep(1.5)
                  continue
                
                if nyxoplasiaID % 10 == 3:
                  print("a unknown aura radiates off your severe nyxoplasic folk, preventing the healing effects")
                  time.sleep(textspeed)
                  continue
      
                if shortinput3 == "1":
                  if playerhealth + 5 >= 10:
                    playerhealth = 10
                  else:
                    playerhealth += 5
                  print(playername, "was healed!")
                  medibedi -= 1
                  time.sleep(textspeed)
                  break
                
                if shortinput3 == "2":
                  if f1health + 5 >= 10:
                    f1health = 10
                  else:
                    f1health += 5
                  print(folk1name, "was healed!")
                  medibedi -= 1
                  time.sleep(textspeed)
                  break
      
                if shortinput3 == "3":
                  if f2health + 5 >= 10:
                    f2health = 10
                  else:
                    f2health += 5
                  print(folk2name, "was healed!")
                  medibedi -= 1
                  time.sleep(textspeed)
                  break
      
                if shortinput3 == "4":
                  if f3health + 5 >= 10:
                    f3health = 10
                  else:
                    f3health += 5
                  print(folk3name, "was healed!")
                  medibedi -= 1
                  time.sleep(textspeed)
                  break
               
              #special inventory
              while shortintinput == "9":
                print("\033[H\033[2J", end="")
                specialinventory()
                print("press 0 to go back")
                shortinput2 = input()
        
                #back
                while shortinput2 == "0":
                  shortintinput = ""
                  shortinput2 = ""
        
                #folknix
                while shortinput2 == "folknix":
                  print("\033[H\033[2J", end="")
                  print("FOLKNIX")
                  print("the folknix revives a dead folk")
                  print("cannot be used on yourself")
                  print("do you want to use this item")
                  print("(1) yes (0) no")
                  shortinput3 = input("")
                  if shortinput3 == "1":
                    if folknix >= 1:
                      if f1health == 0:
                        f1health = 10
                        f1hunger = 100
                        f1stamina = 100
                        print ("you revived", folk1name)
                        folknix -= 1
                        time.sleep(textspeed)
                        shortinput2 = ""
                      elif f2health == 0:
                        f2health = 10
                        f2hunger = 100
                        f2stamina = 100
                        print ("you revived", folk2name)
                        folknix -= 1
                        time.sleep(textspeed)
                        shortinput2 = ""
                      elif f3health == 0:
                        f3health = 10
                        f3hunger = 100
                        f3stamina = 100
                        print ("you revived", folk3name)
                        folknix -= 1
                        time.sleep(textspeed)
                        shortinput2 = ""
                      else:
                        print("you dont have dead folks!")
                        time.sleep(textsleep)
                        shortinput2 = ""
                    else:
                      print("you dont have folknixes")
                      time.sleep(textspeed)
                      shortinput2 = ""
                  else: 
                    shortinput2 = ""
        
                #terminus
                while shortinput2 == "term":
                  print("\033[H\033[2J", end="")
                  print("TERMINUS")
                  print("info - ???")
                  print("you will know when its time")
                  print("press 0 to go back")
                  shortinput3 = input("")
                  if shortinput3 == "0":
                    shortinput2 = ""
        
                #beacon
                while shortinput2 == "beacon":
                  print("\033[H\033[2J", end="")
                  print("FOLK CORP BEACON")
                  print("gives plenty of useful resources on use")
                  print('"do you know the concenquences of a incorrect answer"')
                  print("do you want to use this item")
                  print("(1) yes (0) no")
                  shortinput3 = input("")
                  if shortinput3 == "1":
                    if folkcorpbeacon >= 1:
                      print("you hear beeping")
                      time.sleep(textspeed)
                      if folkcorpbeacon %2 == 1:
                        print("the remote explodes, killing you instantly")
                        time.sleep(textspeed)
                        print("dont get greedy - pig")
                        time.sleep(textspeed)
                        playerhealth = 0
                        deathscreen("folk corp beacon (answer giver's question correctly)")
                        shortintinput = 0
                        shortinput = 0
                        break
                        
                      if folkcorpbeacon %2 == 0:
                        print("\033[H\033[2J", end="")
                        print("BEACON LOOT:")
                        momsmeal_beacon = random.randint(0,3)
                        folkfood_beacon = random.randint(0,5)
                        ammo_beacon = random.randint(0,10)
                        folkmusket_beacon = random.randint(0,1)
                        folksword_beacon = random.randint(0,1)
                        beacon_random = random.randint(0,20)
            
                        print("moms thanksgiving dinner:", momsmeal_beacon)
                        print("folkfood:", folkfood_beacon)
                        print("ammo:", ammo_beacon)
                        print("folkmusket:", folkmusket_beacon)
                        print("folksword:", folksword_beacon)
                        folkfood = folkfood + folkfood_beacon
                        momsmeal = momsmeal + momsmeal_beacon
                        ammo = ammo + ammo_beacon
                        folkmusket = folkmusket + folkmusket_beacon
                        folksword = folksword + folksword_beacon
                        
                        
                        if beacon_random == 1: 
                          folknix += 1
                          manuroll(18)
                          print("folknix: 1 (5%)")
                        if beacon_random > 1 and beacon_random <= 3:
                          shortrandom = random.randint(1,5)
                          if shortrandom == 1:
                            rosavale += 1
                            print("rosavale: 1 (10%) ")
                          if shortrandom == 2:
                            slyphora += 1
                            print("slyphora: 1 (10%) ")
                          if shortrandom == 3:
                            wyrmrose += 1
                            print("wyrmrose: 1 (10%) ")
                          if shortrandom == 4:
                            velisara += 1
                            print("velisara: 1 (10%) ")
                          if shortrandom == 5:
                            luneblossom += 1
                            manuroll(17)
                            print("luneblossom: 1 (10%) ")
                        time.sleep(textspeed + 2)
                        folkcorpbeacon -= 0
                        shortinput2 = ""
                    else: 
                      print("you dont have any beacons")
                      time.sleep(textspeed)
                      shortinput2 = ""
                    
                #flower
                while shortinput2 == "flower":
                  flowerbag()
                  shortinput = input("")

                  if shortinput == "0":
                    shortinput2 = 0

                  while shortinput == "1":
                    print("\033[H\033[2J", end="")
                    if antidote > 0:
                      if s1 != 0 and s2 != 0 and s3 != 0:
                        print("you dont have any empty slots!")
                        shortinput = 0
                        time.sleep(textspeed)
                      else:
                        if rosavale > 0 or wyrmrose > 0 or slyphora > 0 or velisara > 0 or luneblossom > 0: 
                          print("which slot would you like to use? (1 or 2 or 3)")
                          print("0 to go back")
                          shortinput3 = input("")
                          
                          if shortinput3 == "1" and s1 != 0:
                            print("this slot is taken!")
                            time.sleep(textspeed)
                          elif shortinput3 == "1":
                            cookingscreen = 1
                            useantidote = 0
                            while cookingscreen == 1:
                              print("\033[H\033[2J", end="")
                              print("what would you like to add to the antidote?")
                              if rosavale > 0:
                                print(f"{color.bpink}(rosa) rosavale:", rosavale)
                                print("")
                              if slyphora > 0:
                                print(f"{color.yellow}(sly) slyphora:", slyphora)
                                print("")
                              if wyrmrose > 0:
                                print(f"{color.pink}(wyrm) wyrmrose:", wyrmrose)
                                print("")
                              if velisara > 0:
                                print(f"{color.green}(veli) velisara:", velisara)
                                print("")
                              if luneblossom > 0:
                                print(f"{color.bblue}(lune) luneblossom:", luneblossom)
                                print("")
  
                              print(f"{color.white}")
                              shortinput4 = input("")
                              if shortinput4 == "rosa":
                                if rosavale > 0:
                                  print(f"added{color.bpink} rosavale {color.white}to antidote 1!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  rosavale -= 1
                                  s1 = 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "sly":
                                if slyphora > 0:
                                  print(f"added{color.yellow} slyphora {color.white}to antidote 1!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s1 = 2
                                  slyphora -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "wyrm":
                                if wyrmrose > 0:
                                  print(f"added{color.pink} wyrmrose {color.white}to antidote 1!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s1 = 3
                                  wyrmrose -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "veli":
                                if velisara > 0:
                                  print(f"added{color.green} velisara {color.white}to antidote 1!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s1 = 4
                                  velisara -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "lune":
                                if luneblossom > 0:
                                  print(f"added{color.bblue} luneblossom {color.white}to antidote 1!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s1 = 5
                                  luneblossom -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                            shortinput = 0
  
                          if shortinput3 == "2" and s2 != 0:
                            print("this slot is taken!")
                            time.sleep(textspeed)
                          elif shortinput3 == "2":
                            cookingscreen = 1
                            useantidote = 0
                            while cookingscreen == 1:
                              print("\033[H\033[2J", end="")
                              print("what would you like to add to the antidote?")
                              if rosavale > 0:
                                print(f"{color.bpink}(rosa) rosavale:", rosavale)
                                print("")
                              if slyphora > 0:
                                print(f"{color.yellow}(sly) slyphora:", slyphora)
                                print("")
                              if wyrmrose > 0:
                                print(f"{color.pink}(wyrm) wyrmrose:", wyrmrose)
                                print("")
                              if velisara > 0:
                                print(f"{color.green}(veli) velisara:", velisara)
                                print("")
                              if luneblossom > 0:
                                print(f"{color.bblue}(lune) luneblossom:", luneblossom)
                                print("")
  
                              print(f"{color.white}")
                              shortinput4 = input("")
                              if shortinput4 == "rosa":
                                if rosavale > 0:
                                  print(f"added{color.bpink} rosavale {color.white}to antidote 2!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  rosavale -= 1
                                  s2 = 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "sly":
                                if slyphora > 0:
                                  print(f"added{color.yellow} slyphora {color.white}to antidote 2!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s2 = 2
                                  slyphora -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "wyrm":
                                if wyrmrose > 0:
                                  print(f"added{color.pink} wyrmrose {color.white}to antidote 2!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s2 = 3
                                  wyrmrose -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "veli":
                                if velisara > 0:
                                  print(f"added{color.green} velisara {color.white}to antidote 2!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s2 = 4
                                  velisara -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "lune":
                                if luneblossom > 0:
                                  print(f"added{color.bblue} luneblossom {color.white}to antidote 2!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s2 = 5
                                  luneblossom -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                            shortinput = 0
  
                          if shortinput3 == "3" and s3 != 0:
                            print("this slot is taken!")
                            time.sleep(textspeed)
                          elif shortinput3 == "3":
                            cookingscreen = 1
                            useantidote = 0
                            while cookingscreen == 1:
                              print("\033[H\033[2J", end="")
                              print("what would you like to add to the antidote?")
                              if rosavale > 0:
                                print(f"{color.bpink}(rosa) rosavale:", rosavale)
                                print("")
                              if slyphora > 0:
                                print(f"{color.yellow}(sly) slyphora:", slyphora)
                                print("")
                              if wyrmrose > 0:
                                print(f"{color.pink}(wyrm) wyrmrose:", wyrmrose)
                                print("")
                              if velisara > 0:
                                print(f"{color.green}(veli) velisara:", velisara)
                                print("")
                              if luneblossom > 0:
                                print(f"{color.bblue}(lune) luneblossom:", luneblossom)
                                print("")
  
                              print(f"{color.white}")
                              shortinput4 = input("")
                              if shortinput4 == "rosa":
                                if rosavale > 0:
                                  print(f"added{color.bpink} rosavale {color.white}to antidote 3!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s3 = 1
                                  rosavale -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "sly":
                                if slyphora > 0:
                                  print(f"added{color.yellow} slyphora {color.white}to antidote 3!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s3 = 2
                                  slyphora -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "wyrm":
                                if wyrmrose > 0:
                                  print(f"added{color.pink} wyrmrose {color.white}to antidote 3!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s3 = 3
                                  wyrmrose -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                                  
                              if shortinput4 == "veli":
                                if velisara > 0:
                                  print(f"added{color.green} velisara {color.white}to antidote 3!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s3 = 4
                                  velisara -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
  
                              if shortinput4 == "lune":
                                if luneblossom > 0:
                                  print(f"added{color.bblue} luneblossom {color.white}to antidote 3!")
                                  if useantidote == 0:
                                    antidote -= 1
                                    useantidote = 1
                                  s3 = 5
                                  luneblossom -= 1
                                  cookingscreen = 0
                                else:
                                  print("you dont have this flower!")
                                  time.sleep(textspeed)
                            shortinput = 0                               

                          if shortinput3 == "0":
                            break
                        else:
                          print("you dont have any flowers")
                          time.sleep(textspeed)
                          shortinput = 0
                    else:
                      print("you do not have any antidotes")
                      time.sleep(textspeed)
                      shortinput = 0
                   
                  while shortinput == "rosa":
                    print("\033[H\033[2J", end="")
                    print("ROSACURA")
                    print("cure for the floral curse")
                    if fcfolk1 == 1 or fcplayer == 1 or fcfolk2 == 1 or fcfolk3 == 1:
                      print("press 1 to cure")
                    print("press 0 to go back")
                    shortinput3 = input("")
                    if shortinput3 == "0":
                      shortinput = ""
                    if shortinput3 == "1" and fcfolk1 == 1 or fcplayer == 1 or fcfolk2 == 1 or fcfolk3 == 1:
                      if s1 == 1 or s2 == 1 or s3 == 1:
                        if s1 == 1:
                          print("\033[H\033[2J", end="")
                          print("everyone huddles near the antidote")
                          time.sleep(textspeed)
                          print("one injection into your body speads to the whole band")
                          time.sleep(textspeed)
                          print("the curse is cured!")
                          fcplayer = 0
                          fcfolk1 = 0
                          fcfolk2 = 0
                          fcfolk3 = 0
                          fcstage = 0
                          s1 = 0
                        if s2 == 1:
                          print("\033[H\033[2J", end="")
                          print("everyone huddles near the antidote")
                          time.sleep(textspeed)
                          print("one injection into your body speads to the whole band")
                          time.sleep(textspeed)
                          print("the curse is cured!")
                          fcplayer = 0
                          fcfolk1 = 0
                          fcfolk2 = 0
                          fcfolk3 = 0
                          fcstage = 0
                          s2 = 0
                        if s3 == 1:
                          print("\033[H\033[2J", end="")
                          print("everyone huddles near the antidote")
                          time.sleep(textspeed)
                          print("one injection into your body speads to the whole band")
                          time.sleep(textspeed)
                          print("the curse is cured!")
                          fcplayer = 0
                          fcfolk1 = 0
                          fcfolk2 = 0
                          fcfolk3 = 0
                          fcstage = 0
                          s3 = 0
    
                      else:
                        print("you dont have any applicable antidotes")
                    elif shortinput3 == "1": print("nobody has the floral curse")
                    time.sleep(textspeed)
                    shortinput0 = ""

                  while shortinput == "sly":
                    print("\033[H\033[2J", end="")
                    print("SLYCURA")
                    print("cure for nyxoplasia")
                    if nyxoplasiaID != 0:
                      print("press 1 to cure")
                    elif active_expansion == 23:
                      print("press 1 to reverse inject")
                    print("press 0 to go back")
                    shortinput3 = input("")
                    if shortinput3 == "0":
                      shortinput = ""
                    if shortinput3 == "1" and nyxoplasiaID != 0:
                      if s1 == 2 or s2 == 2 or s3 == 2:
                        manuroll(14)
                        if nyxoplasiaID // 10 == 1:
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 2:
                            s1 = 0
                          elif s2 == 2:
                            s2 = 0
                          elif s3 == 2:
                            s3 = 0
                        if nyxoplasiaID // 10 == 2:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk1name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 2:
                            s1 = 0
                          elif s2 == 2:
                            s2 = 0
                          elif s3 == 2:
                            s3 = 0
                        if nyxoplasiaID // 10 == 3:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk2name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 2:
                            s1 = 0
                          elif s2 == 2:
                            s2 = 0
                          elif s3 == 2:
                            s3 = 0
                        if nyxoplasiaID // 10 == 4:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk3name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk3dis = 0
                          f1infectionTimer = 0
                          if s1 == 2:
                            s1 = 0
                          elif s2 == 2:
                            s2 = 0
                          elif s3 == 2:
                            s3 = 0
    
                      else:
                        print("you dont have any applicable antidotes")
                    elif shortinput3 == "2" and (active_expansion == 23 or debugmode == 1):
                      if playerdis == 0 or folk1dis == 0 or folk2dis == 0 or folk3dis == 0:
                        while True:
                          print("\033[H\033[2J", end="")
                          print("who would you like to inject")
                          print("")
                          if playerdis == 0:
                            print("(1)", playername)
                          if folk1dis == 0:
                            print("(2)", folk1name)
                          if folk2dis == 0:
                            print("(3)", folk2name)
                          if folk3dis == 0:
                            print("(4)", folk3name)

                          shortinput4 = input("")
                          if shortinput4 == "1" and playerdis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject yourself, releasing a shocking jolt throughout your body")
                            time.sleep(textspeed)
                            print("you cant tell how you feel, you are in a state of delirium")
                            time.sleep(textspeed)
                            playerdis = 2
                            nyxoplasiaID = 12
                            playerinfectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "2" and folk1dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk1name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk1name = 2
                            nyxoplasiaID = 22
                            f1infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk2dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk2name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk2name = 2
                            nyxoplasiaID = 32
                            f2infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk3dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk3name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk3name = 2
                            nyxoplasiaID = 42
                            f3infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                      else:
                        print("everyone is sick...")
                        time.sleep(1)
                        shortinput = ""
                    elif shortinput3 == "1": 
                      print("nobody has nyxoplasia")
                      time.sleep(textspeed)
                      shortinput = ""

                  while shortinput == "wyrm":
                    print("\033[H\033[2J", end="")
                    print("WYRMCURA")
                    print("cure for umbrythia")
                    if umbrythiaID != 0:
                      print("press 1 to cure")
                    print("press 0 to go back")
                    shortinput3 = input("")
                    if shortinput3 == "0":
                      shortinput = ""
                    if shortinput3 == "1" and umbrythiaID != 0:
                      if s1 == 3 or s2 == 3 or s3 == 3:
                        manuroll(15)
                        if umbrythiaID // 10 == 1:
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 3:
                            s1 = 0
                          elif s2 == 3:
                            s2 = 0
                          elif s3 == 3:
                            s3 = 0
                        if umbrythiaID // 10 == 2:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk1name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 3:
                            s1 = 0
                          elif s2 == 3:
                            s2 = 0
                          elif s3 == 3:
                            s3 = 0
                        if umbrythiaID // 10 == 3:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk2name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 3:
                            s1 = 0
                          elif s2 == 3:
                            s2 = 0
                          elif s3 == 3:
                            s3 = 0
                        if umbrythiaID // 10 == 4:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk3name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk3dis = 0
                          f3infectionTimer = 0
                          if s1 == 3:
                            s1 = 0
                          elif s2 == 3:
                            s2 = 0
                          elif s3 == 3:
                            s3 = 0
    
                      else:
                        print("you dont have any applicable antidotes")
                    elif shortinput3 == "2" and (active_expansion == 23 or debugmode == 1):
                      if playerdis == 0 or folk1dis == 0 or folk2dis == 0 or folk3dis == 0:
                        while True:
                          print("\033[H\033[2J", end="")
                          print("who would you like to inject")
                          print("")
                          if playerdis == 0:
                            print("(1)", playername)
                          if folk1dis == 0:
                            print("(2)", folk1name)
                          if folk2dis == 0:
                            print("(3)", folk2name)
                          if folk3dis == 0:
                            print("(4)", folk3name)

                          shortinput4 = input("")
                          if shortinput4 == "1" and playerdis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject yourself, releasing a shocking jolt throughout your body")
                            time.sleep(textspeed)
                            print("you cant tell how you feel, you are in a state of delirium")
                            time.sleep(textspeed)
                            playerdis = 2
                            umbrythiaID = 12
                            playerinfectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "2" and folk1dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk1name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk1name = 2
                            umbrythiaID = 22
                            f1infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk2dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk2name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk2name = 2
                            umbrythiaID = 32
                            f2infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk3dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk3name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk3name = 2
                            umbrythiaID = 42
                            f3infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                    elif shortinput3 == "1": print("nobody has umbrythia")
                    time.sleep(textspeed)
                    shortinput = ""

                  while shortinput == "veli":
                    print("\033[H\033[2J", end="")
                    print("VELICURA")
                    print("cure for virellosis")
                    if virellosisID != 0:
                      print("press 1 to cure")
                    print("press 0 to go back")
                    shortinput3 = input("")
                    if shortinput3 == "0":
                      shortinput = ""
                    if shortinput3 == "1" and virellosisID != 0:
                      if s1 == 4 or s2 == 4 or s3 == 4:
                        manuroll(15)
                        if virellosisID // 10 == 1:
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 4:
                            s1 = 0
                          elif s2 == 4:
                            s2 = 0
                          elif s3 == 4:
                            s3 = 0
                        if virellosisID // 10 == 2:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk1name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 4:
                            s1 = 0
                          elif s2 == 4:
                            s2 = 0
                          elif s3 == 4:
                            s3 = 0
                        if virellosisID // 10 == 3:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk2name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 4:
                            s1 = 0
                          elif s2 == 4:
                            s2 = 0
                          elif s3 == 4:
                            s3 = 0
                        if virellosisID // 10 == 4:
                          print("\033[H\033[2J", end="")
                          print("you inject", folk3name, "with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears their mind, they take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk3dis = 0
                          f3infectionTimer = 0
                          if s1 == 4:
                            s1 = 0
                          elif s2 == 4:
                            s2 = 0
                          elif s3 == 4:
                            s3 = 0
    
                      else:
                        print("you dont have any applicable antidotes")
                    elif shortinput3 == "2" and (active_expansion == 23 or debugmode == 1):
                      if playerdis == 0 or folk1dis == 0 or folk2dis == 0 or folk3dis == 0:
                        while True:
                          print("\033[H\033[2J", end="")
                          print("who would you like to inject")
                          print("")
                          if playerdis == 0:
                            print("(1)", playername)
                          if folk1dis == 0:
                            print("(2)", folk1name)
                          if folk2dis == 0:
                            print("(3)", folk2name)
                          if folk3dis == 0:
                            print("(4)", folk3name)

                          shortinput4 = input("")
                          if shortinput4 == "1" and playerdis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject yourself, releasing a shocking jolt throughout your body")
                            time.sleep(textspeed)
                            print("you cant tell how you feel, you are in a state of delirium")
                            time.sleep(textspeed)
                            playerdis = 2
                            virellosisID = 12
                            playerinfectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "2" and folk1dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk1name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk1name = 2
                            virellosisID = 22
                            f1infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk2dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk2name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk2name = 2
                            virellosisID = 32
                            f2infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                          if shortinput4 == "3" and folk3dis == 0:
                            print("\033[H\033[2J", end="")
                            print("you inject", folk3name)
                            time.sleep(textspeed)
                            print("they are dazed, seemingly unconconsious")
                            time.sleep(textspeed)
                            folk3name = 2
                            virellosisID = 42
                            f3infectionTimer = random.randint(3,5)
                            shortinput = ""
                            if s1 == 2:
                              s1 = 0
                            elif s2 == 2:
                              s2 = 0
                            elif s3 == 2:
                              s3 = 0
                            break
                    elif shortinput3 == "1": print("nobody has virellosis")
                    time.sleep(textspeed)
                    shortinput = ""

                  while shortinput == "lune":
                    print("\033[H\033[2J", end="")
                    print("LUNECURA")
                    print("cure for any disease")
                    if (playerdis >= 1 or folk1dis >= 1 or folk2dis >= 1 or folk3dis >= 1) and (s1 == 5 or s2 == 5 or s3 == 5):
                      print("press 1 to use")
                    print("press 0 to go back")
                    shortinput3 = input("")
                    if shortinput3 == "0":
                      shortinput = ""
                    if shortinput3 == "1" and not (playerdis >= 1 or folk1dis >= 1 or folk2dis >= 1 or folk3dis >= 1):
                      print("nobody has a disease!")
                      time.sleep(textspeed)
                      shortinput = 0
                    if shortinput3 == "1" and not (s1 == 5 or s2 == 5 or s3 == 5):
                      print("you dont have any applicable antidotes")
                      time.sleep(textspeed)
                      shortinput = 0
                    while shortinput3 == "1" and (playerdis >= 1 or folk1dis >= 1 or folk2dis >= 1 or folk3dis >= 1):
                      print("\033[H\033[2J", end="")
                      print("who would like to cure")
                      if playerdis >= 1:
                        print("(1)", playername)
                      if folk1dis >= 1:
                        print("(2)", folk1dis)  
                      if folk2dis >= 1:
                        print("(3)", folk1dis)  
                      if folk3dis >= 1:
                        print("(4)", folk1dis)  
                      print("(0) back")

                      shortinput4 = input("")

                      if shortinput4 == "0":
                        shortinput3 = 0
                        shortinput = 0
                        

                      if shortinput4 == "1" and playerdis >= 1:
                        if nyxoplasiaID // 10 == 1:
                          manuroll(14)
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if virellosisID // 10 == 1:
                          manuroll(15)
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if umbrythiaID // 10 == 1:
                          manuroll(16)
                          print("\033[H\033[2J", end="")
                          print("you inject yourself with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          playerdis = 0
                          playerinfectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        shortinput3 = 0
                      if shortinput4 == "2" and folk1dis >= 1:
                        if nyxoplasiaID // 10 == 2:
                          manuroll(14)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if virellosisID // 10 == 2:
                          manuroll(15)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if umbrythiaID // 10 == 2:
                          manuroll(16)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk1dis = 0
                          f1infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        shortinput3 = 0
                      if shortinput4 == "3" and folk2dis >= 1:
                        if nyxoplasiaID // 10 == 3:
                          manuroll(14)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if virellosisID // 10 == 3:
                          manuroll(15)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if umbrythiaID // 10 == 3:
                          manuroll(16)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk2dis = 0
                          f2infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        shortinput3 = 0
                      if shortinput4 == "4" and folk3dis >= 1:
                        if nyxoplasiaID // 10 == 4:
                          manuroll(14)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          nyxoplasiaID = 0
                          noHealing = 0
                          folk3dis = 0
                          f3infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if virellosisID // 10 == 4:
                          manuroll(15)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          virellosisID = 0
                          folk3dis = 0
                          f3infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        if umbrythiaID // 10 == 4:
                          manuroll(16)
                          print("\033[H\033[2J", end="")
                          print("you inject them with the antidote")
                          time.sleep(textspeed)
                          print("the injection clears your mind, you take a deep breath in relief")
                          time.sleep(textspeed)
                          print("the disease is cured!")
                          umbrythiaID = 0
                          folk3dis = 0
                          f3infectionTimer = 0
                          if s1 == 5:
                            s1 = 0
                          elif s2 == 5:
                            s2 = 0
                          elif s3 == 5:
                            s3 = 0
                        shortinput3 = 0
                    time.sleep(textspeed)
                    shortinput = "" 
                      
                    
                #sins
                while shortinput2 == "sin":
                  sinbag()
                  shortinput = input("")

                  if shortinput == "0":
                    shortinput2 = 0
                    
                  #gluttony
                  while shortinput == "glut":
                    print("\033[H\033[2J", end="")
                    print("GLUTTONY")
                    print("steals other folks food and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if gluttonyitem >= 1:
                        print("glutton overwhelmes your mind")
                        time.sleep(textspeed)
                        print("you steal the food from your folks")
                        time.sleep(textspeed)
                        print("you lose more food now")
                        time.sleep(textspeed)
                        playerhunger += f1hunger + f2hunger + f3hunger
                        f1hunger = 0
                        f2hunger = 0
                        f3hunger = 0
                        playerfoodmultiplier = 1.5
                        score -= 2
                        del specialinventory["(glut) GLUTTONY"]
                        gluttonyitem -= 1
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
          
                  #wrath
                  while shortinput == "wrath":
                    print("\033[H\033[2J", end="")
                    print("WRATH")
                    print("kills every possible character and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if wrathitem >= 1:
                        print("bloodlust overwhelmes your mind")
                        time.sleep(textspeed)
                        print("everything dies")
                        time.sleep(textspeed)
                        shortrandom = random.randint(1,3)
                        if shortrandom == 1:
                          print(folk1name, "has also died")
                          f1health = 0
                       
                        if shortrandom == 2:
                          print(folk2name, "has also died")
                          f2health = 0
            
                        if shortrandom == 3:
                          print(folk3name, "has also died")
                          f3health = 0
            
                        deaddino = 1
                        del specialinventory["(wrath) WRATH"]
                        wrathitem -= 1
                        deadtree = 1
                        score -= 2
                        time.sleep(textspeed)
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
          
                  #pride
                  while shortinput == "pride":
                    print("\033[H\033[2J", end="")
                    print("PRIDE")
                    print("heals you for 10 and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if prideitem >= 1:
                        print("ego overwhelmes your mind")
                        time.sleep(textspeed)
                        print("you must be the best")
                        time.sleep(textspeed)
                        print("you gain 10 hp")
                        playerhealth += 10
                        time.sleep(textspeed)
                        print("every folk has also died")
                        f1health = 0
                        f2health = 0
                        f3health = 0
                        score -= 2
                        del specialinventory["(pride) PRIDE"]
                        prideitem -= 1
                        time.sleep(textspeed)
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
          
                  #greed
                  while shortinput == "greed":
                    print("\033[H\033[2J", end="")
                    print("GREED")
                    print("gives you a random amount of george and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if greeditem >= 1:
                        print("wealth overwhelmes your mind")
                        time.sleep(textspeed)
                        print("you need money")
                        time.sleep(textspeed)
                        print("\033[H\033[2J", end="")
                        for i in range(folkfood):
                          shortrandom = random.randint(0,10)
                          print("you turn folkfood into", shortrandom, "george")
                          folkfood -= 1
                          george += shortrandom
                          time.sleep(0.25)
                        for i in range (momsmeal):
                          shortrandom = random.randint(3,15)
                          print("you turn moms thankgiving dinner into", shortrandom, "george")
                          momsmeal -= 1
                          george += shortrandom
                          time.sleep(0.25)
                        for i in range (folksword):
                          shortrandom = random.randint(10,20)
                          print("you turn folksword into", shortrandom, "george")
                          folksword -= 1
                          george += shortrandom
                          time.sleep(0.25)
                        for i in range (folkmusket):
                            shortrandom = random.randint(15,25)
                            print("you turn moms thankgiving dinner into", shortrandom, "george")
                            folkmusket -= 1
                            george += shortrandom
                            time.sleep(0.25)
                        time.sleep(textspeed)
                        del specialinventory["(greed) GREED"]
                        greeditem -= 1
                        score -= 2
                        time.sleep(textspeed)
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
                    
                  #lust
                  while shortinput == "lust":
                    print("\033[H\033[2J", end="")
                    print("LUST")
                    print("will enter you into mili's trial??")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if lustitem >= 1:
                        manuroll(4)
                        print("desire overwhelmes your mind")
                        time.sleep(textspeed)
                        print("you cant control it")
                        time.sleep(textspeed)
                        print("your max hp is set to one")
                        time.sleep(textspeed)
                        print("each death of your folks grants 5 more max hp and heals you to that amount")
                        time.sleep(textspeed)
                        del specialinventory["(lust) LUST"]
                        playerhealth = 1
                        score -= 2
                        lustactive = 1
                        lustitem -= 1
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
          
                  #envy
                  while shortinput == "envy":
                    print("\033[H\033[2J", end="")
                    print("ENVY")
                    print("will heal you for 20hp and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if envyitem >= 1:
                        print("prestige overwhelmes your mind")
                        time.sleep(textspeed)
                        print("you need status")
                        time.sleep(textspeed)
                        print("you gain 20 hp")
                        time.sleep(textspeed)
                        print("all your folks are applied with the floral curse...")
                        time.sleep(textspeed)
                        del specialinventory["(envy) ENVY"]
                        fcfolk1 = 1
                        fcfolk2 = 1
                        fcfolk3 = 1
                        score -= 2
                        playerhealth += 20
                        maxhp = 20
                        envyitem -= 1
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
          
                  #sloth
                  while shortinput == "sloth":
                    print("\033[H\033[2J", end="")
                    print("SLOTH")
                    print("adds serene for the next day and ???")
                    print("do you want to use this item?")
                    print("(1) yes (0) no")
                    shortinput3 = input("")
                    if shortinput3 == "1":
                      if slothitem >= 1:
                        print("laziness overwhelmes your mind")
                        time.sleep(textspeed)
                        print("everything must be easy")
                        time.sleep(textspeed)
                        print("the next day is serene")
                        time.sleep(textspeed)
                        print("the next day is guaranteed to be negative")
                        time.sleep(textspeed)
                        del specialinventory["(sloth) SLOTH"]
                        serene = 288
                        sloth = 1
                        score -= 2
                        slothitem -= 1
                        shortinput2 = ""
                      else:
                        print("you dont have this item")
                        time.sleep(textspeed)
                        shortinput2 = ""
                    else:
                      shortinput2 = ""
        
                #tooth
                while shortinput2 == "tooth":
                  print("\033[H\033[2J", end="")
                  print("DRAGON TOOTH")
                  print("legends say it can craft a unstoppable blade")
                  print("press 0 to go back")
                  shortinput3 = input("")
                  if shortinput3 == "0":
                    shortinput2 = ""
        
                #meteor
                while shortinput2 == "meteor":
                  print("\033[H\033[2J", end="")
                  print("METEORIC ROCK")
                  print("idk yet")
                  print("press 0 to go back")
                  shortinput3 = input("")
                  if shortinput3 == "0":
                    shortinput2 = ""
                  
        
              #back
              while shortintinput == "0":
                shortinput = 0
                shortintinput = 0
                shortinput2 = 0
      
            while shortinput == "4":
              print("\033[H\033[2J", end="")
              print("(1) edit traveling order")
              print("(2) take a break")
              print("(3) sleep")
              print("(4) back")
              
              shortinput2 = input("")
              while shortinput2 == "1":
                print("\033[H\033[2J", end="")
                print("current pace:", orders[order])
                print("")
                for val in orderlist: print(val)
                print("")
                print("1-3 which pace would you like")
                print("0 to go back")
      
                shortinput3 = input("")        
                if shortinput3 == "0":
                  shortinput2 = 0
                if shortinput3 == "1":
                  order = 0
                if shortinput3 == "2":
                  order = 1
                if shortinput3 == "3":
                  order = 2
      
              if shortinput2 == "2":
                sleepmode = 2
                shortinput = "1"
                break
              
              if shortinput2 == "3":
                if int(timehr) < 20 and int(timehr) > 5 and not active_expansion // 10 == 1:
                  print("you cant sleep during the day!")
                  time.sleep(textspeed)
                  continue
                sleepmode = 1
                shortinput = "1"
                break
      
              if shortinput2 == "4":
                shortinput = 0

            def manurewardroll():
              global folkfood
              global momsmeal
              global antidote
              global distancemultiplier
              global f1foodgainmultiplier
              global f2foodgainmultiplier
              global f3foodgainmultiplier
              global playerfoodgainmultiplier
              global serene
              global medibedi
              global folkrapier
              global folkrifle
              global pickaxe
              global rosavale
              global wrymrose
              global velisara
              global slyphora
              global luneblossom
              global ammo
              
              
              print(f"\033[H\033[2J", end="")
              print("you look up: a box falling with a parachute above you")
              time.sleep(textspeed)
              print("you open the box...")
              time.sleep(textspeed)
        
              shortrandom = random.randint(1,100)
              
              if shortrandom <= 50:
                shortrandom = random.randint(1,20)
                #legendary!
                if shortrandom == 1:
                  shortrandom = random.randint(1,2)
                  if shortrandom == 1:
                    print("you got a folk rapier")
                    time.sleep(textspeed)
                    folkrapier += 1
                  if shortrandom == 2:
                    print("you got a folk rifle")
                    time.sleep(textspeed)
                    folkrifle += 1
                #rare
                if shortrandom > 1 and shortrandom < 5:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1:
                    print("you got a pickaxe")
                    time.sleep(textspeed)
                    pickaxe += 1
                  if shortrandom == 2:
                    print("you got 3 medibedis!")
                    time.sleep(textspeed)
                    medibedi += 3
                  if shortrandom == 3:
                    print("you got 4 folkfood!")
                    time.sleep(textspeed)
                    folkfood += 4
                #uncommon
                if shortrandom > 4 and shortrandom < 11:
                  shortrandom = random.randint(1,3)
                  if shortrandom == 1:
                    shortrandom = random.randint(1,5)
                    if shortrandom == 1:
                      rosavale += 1
                      print("you got a rosavale")
                    if shortrandom == 2:
                      slyphora += 1
                      print("you got a slyphora")
                    if shortrandom == 3:
                      wyrmrose += 1
                      print("you got a wyrmrose")
                    if shortrandom == 4:
                      velisara += 1
                      print("you got a velisara")
                    if shortrandom == 5:
                      luneblossom += 1
                      manuroll(17)
                      print("you got a luneblossom")
                    time.sleep(textspeed)
                  elif shortrandom == 2:
                    print("you got 2 medibedis!")
                    time.sleep(textspeed)
                    medibedi += 2
                  elif shortrandom == 3:
                    print("you got 4 ammo!")
                    time.sleep(textspeed)
                    ammo += 4
                #common
                else:
                  shortrandom = random.randint(1,2)
                  if shortrandom == 1:
                    print("you got two folkfood")
                    time.sleep(textspeed)
                    folkfood += 2
                  if shortrandom == 2:
                    print("you got one moms thankgiving meal")
                    time.sleep(textspeed)
                    momsmeal += 2

              elif shortrandom <= 70:
                manutravel = 0
                print("the box turns into a rocket.. ")
                shortrandom = random.randint(300,1500)
      
                for val in range(shortrandom):
                  distance -= 1
                  manutravel += 1
                  print("you traveled:", manutravel)

                time.sleep(textspeed)

              elif shortrandom <= 90:
                shortrandom = random.randint(1,3)
                if shortrandom == 1:
                  print("you got 7 folkfood")
                  time.sleep(textspeed)
                  folkfood += 7
                if shortrandom == 2:
                  print("you got 5 moms thankigiving meals")
                  time.sleep(textspeed)
                  momsmeal += 5
                if shortrandom == 3:
                  print("you got 3 antidotes")
                  time.sleep(textspeed)
                  antidote += 3
                
              elif shortrandom <= 99:
                shortrandom = random.randint(1,5)
                if shortrandom == 1 or shortrandom == 2:
                  print("BLESSING! everyone gains more food from eating")
                  time.sleep(textspeed)
                  playerfoodgainmultiplier += 0.5
                  f1foodgainmultiplier += 0.5
                  f2foodgainmultiplier += 0.5
                  f3foodgainmultiplier += 0.5
                if shortrandom == 3 or shortrandom == 4:
                  print("BLESSING! gain 2 days worth of serene")
                  time.sleep(textspeed)
                  serene = 576 
                if shortrandom == 5:
                  print("BLESSING! gain serene lasting the length of the whole run")
                  time.sleep(textspeed)
                  serene = 999999

              else: 
                print("BLESSING! move twice as fast")
                distancemultiplier *= 2
                
            while shortinput == "5" and active_expansion != 0:
              print(f"\033[H\033[2J", end="")

              if active_expansion // 10 == 1:
                print(f"{color.white}current expansion: time expansion!")
                if active_expansion % 10 == 1:
                  print(f"{color.bgreen}(stage 1) can sleep during the day / can rest effectivly at night")
                  print(f"{color.red}(stage 2) 30% increased speed during day / decreased hunger (30%) and stamina (50%) loss at night")
                  print(f"{color.red}(stage 3) can change the limits of day and night to an extent")

                if active_expansion % 10 == 2:
                  print(f"{color.bgreen}(stage 1) can sleep during the day / can rest effectivly at night")
                  print(f"{color.bgreen}(stage 2) 30% increased speed during day / decreased hunger (30%) and stamina (50%) loss at night")
                  print(f"{color.red}(stage 3) can change the limits of day and night to an extent")

                if active_expansion % 10 == 3:
                  print(f"{color.bgreen}(stage 1) can sleep during the day / can rest effectivly at night")
                  print(f"{color.bgreen}(stage 2) 30% increased speed during day / decreased hunger (30%) and stamina (50%) loss at night")
                  print(f"{color.bgreen}(stage 3) can change the limits of day and night to an extent")

                print(f"{color.white}")
                if active_expansion % 10 == 3:
                  print("1 to edit day and night limits")
                print("(0) back")

                shortinput2 = input("")
                while shortinput2 == "1" and (active_expansion % 10 == 3 or debugmode == 1):
                  print(f"\033[H\033[2J", end="")
                  print(f"{color.byellow}what time should day *start* (2 - 12)")
                  print("currently:", morn)
                  shortinput3 = input("")

                  try: int(shortinput3)
                  except ValueError:
                    print("that number is not an integer!")
                    time.sleep(1)
                    continue
                  else:
                    shortinput3 = int(shortinput3)
                  if shortinput3 < 2 or shortinput3 > 12:
                    print("that number is not from 2 - 12!")
                    time.sleep(1)
                  else:
                    morn = shortinput3
                    while True:
                      print(f"\033[H\033[2J", end="")
                      print(f"{color.blue}what time should night *start* (12 - 22, must be 6 hours apart from day start)")
                      print("currently:", even)
                      shortinput3 = input("")
    
                      try: int(shortinput3)
                      except ValueError:
                        print("that number is not an integer!")
                        time.sleep(1)
                        continue
                      else:
                        shortinput3 = int(shortinput3)
                      if shortinput3 < 12 or shortinput3 > 22:
                        print("that number is not from 12 - 22!")
                        time.sleep(1)
                        continue


                      differ = shortinput3 - morn
                      differ = min(differ, 24 - differ)

                      if differ <= 6:
                        print("these times are too close together!")
                        time.sleep(1)
                        continue
                      else:
                        even = shortinput3
                        shortinput2 = 0
                        break

                if shortinput2 == "0":
                  shortinput = 0

              if active_expansion // 10 == 2:
                
                print(f"{color.white}current expansion: infection expansion!")
                if active_expansion % 10 == 1:
                  print(f"{color.bgreen}(stage 1) reduced disease time, diseases are less common OR leave disease time unchanged and diseases are very common")
                  print(f"{color.red}(stage 2) unlocks mutations for diseases, reversing the effects (only 1 at a time)")
                  print(f"{color.red}(stage 3) unlocks reverse antidotes, giving mutated diseases without affect the previous cap")

                if active_expansion % 10 == 2:
                  print(f"{color.bgreen}(stage 1) reduced disease time, diseases are less common OR leave disease time unchanged and diseases are very common")
                  print(f"{color.bgreen}(stage 2) unlocks mutations for diseases, reversing the effects (only 1 at a time)")
                  print(f"{color.red}(stage 3) unlocks reverse antidotes, giving mutated diseases without affect the previous cap")

                if active_expansion % 10 == 3:
                  print(f"{color.bgreen}(stage 1) reduced disease time, diseases are less common OR leave disease time unchanged and diseases are very common")
                  print(f"{color.bgreen}(stage 2) unlocks mutations for diseases, reversing the effects (only 1 at a time)")
                  print(f"{color.bgreen}(stage 3) unlocks reverse antidotes, giving mutated diseases without affect the previous cap")
  
                print(f"{color.white}")
                print("")
                print("1 to toggle stage 1 effect")
                if infs1 == 1:
                  print("currently ON")
                else:
                  print("currently OFF")
                print("")
                if active_expansion % 10 >= 2:
                  print("2 to mutate disease")
                print("")
                print("(0) back")

                shortinput2 = input("")
                if shortinput2 == "1":
                  if infs1 == 1:
                    infs1 = 0
                  else:
                    infs1 = 1

                while shortinput2 == "2" and active_expansion % 10 >= 2:
                  if playerdis != 2 and folk1dis != 2 and folk2dis != 2 and folk3dis != 2:
                    if playerdis != 0 or folk1dis != 0 or folk2dis != 0 or folk3dis != 0:
                      print(f"\033[H\033[2J", end="")
                      print("what disease would you like to mutate")
                      print("")
                      if playerdis >= 1 and playerhealth > 0:
                        if nyxoplasiaID // 10 == 1:
                          print("(1)", playername, ": stage", nyxoplasiaID % 10, "nyxoplasia")
                        if virellosisID // 10 == 1:
                          print("(1)", playername, ": stage", virellosisID % 10, "virellosis")
                        if umbrythiaID // 10 == 1:
                          print("(1)", playername, ": stage", umbrythiaID % 10, "umbrythia")
                      if folk1dis >= 1 and f1health > 0:
                        if nyxoplasiaID // 10 == 2:
                          print("(2)", folk1name, ": stage", nyxoplasiaID % 10, "nyxoplasia")
                        if virellosisID // 10 == 2:
                          print("(2)", folk1name, ": stage", virellosisID % 10, "virellosis")
                        if umbrythiaID // 10 == 2:
                          print("(2)", folk1name, ": stage", umbrythiaID % 10, "umbrythia")
                      if folk2dis >= 1 and f2health > 0:
                        if nyxoplasiaID // 10 == 3:
                          print("(3)", folk2name, ": stage", nyxoplasiaID % 10, "nyxoplasia")
                        if virellosisID // 10 == 3:
                          print("(3)", folk2name, ": stage", virellosisID % 10, "virellosis")
                        if umbrythiaID // 10 == 3:
                          print("(3)", folk2name, ": stage", umbrythiaID % 10, "umbrythia")
                      if folk3dis >= 1 and f3health > 0:
                        if nyxoplasiaID // 10 == 4:
                          print("(4)", folk3name, ": stage", nyxoplasiaID % 10, "nyxoplasia")
                        if virellosisID // 10 == 4:
                          print("(4)", folk3name, ": stage", virellosisID % 10, "virellosis")
                        if umbrythiaID // 10 == 4:
                          print("(4)", folk3name, ": stage", umbrythiaID % 10, "umbrythia")

                      print("")
                      shortinput3 = input("")

                      if shortinput3 == "1" and playerdis == 1:
                        playerdis = 2
                        shortinput2 = 0
                      elif shortinput3 == "2" and folk1dis == 1:
                        folk1dis = 2
                        shortinput2 = 0
                      elif shortinput3 == "3" and folk2dis == 1:
                        folk2dis = 2
                        shortinput2 = 0
                      elif shortinput3 == "4" and folk3dis == 1:
                        folk3dis = 2
                        shortinput2 = 0
                      elif shortinput3 != "1" and shortinput3 != "2" and shortinput3 != "3" and shortinput3 != "4":
                        print("that is not a valid option!")
                        time.sleep(1)
                      
                        
                        
                          
                    else:
                      print("there are no diseases to mutate!")
                      time.sleep(1)
                      break
                  else:
                    print("you already mutated a disease!")
                    time.sleep(1)
                    break
                    
                if shortinput2 == "0":
                  shortinput = 0
              
              if active_expansion // 10 == 3:
                print(f"{color.white}current expansion: manipulation expansion!")
                if active_expansion % 10 == 1:
                  print(f"{color.bgreen}(stage 1) can set your own event, on a one day cooldown")
                  print(f"{color.red}(stage 2) can choose your own disease and victim, shortens event cooldown to half a day")
                  print(f"{color.red}(stage 3) orders")

                if active_expansion % 10 == 2:
                  print(f"{color.bgreen}(stage 1) can set your own event, on a one day cooldown")
                  print(f"{color.bgreen}(stage 2) can choose your own disease and victim, shortens event cooldown to half a day")
                  print(f"{color.red}(stage 3) orders")

                if active_expansion % 10 == 3:
                  print(f"{color.bgreen}(stage 1) can set your own event, on a one day cooldown")
                  print(f"{color.bgreen}(stage 2) can choose your own disease and victim, shortens event cooldown to half a day")
                  print(f"{color.bgreen}(stage 3) orders")
  
                print(f"{color.white}")
                if active_expansion % 10 == 3:
                  print("1 to view orders")
                print("(0) back")

                shortinput2 = input("")
                while shortinput2 == "1" and active_expansion % 10 == 3:
                  print(f"\033[H\033[2J", end="")
                  print("you pull out the order sheet...")
                  time.sleep(textspeed)
                  print(f"\033[H\033[2J", end="")
                  print("orders (rewards are randomized, refresh every day)):")
                  if manuord1ID != 999:
                    print(f"{color.red}{manuord1}")
                  if manuord2ID != 999:
                    print(f"{color.blue}{manuord2}")
                  if manuord3ID != 999:
                    print(f"{color.yellow}{manuord3}")
                  print(f"{color.white}")
                  print("0 to go back")

                  if manuord1ID > 1000:
                    print("1 to claim order 1 reward!")

                  if manuord2ID > 1000:
                    print("2 to claim order 2 reward!")

                  if manuord3ID > 1000:
                    print("3 to claim order 3 reward!")
                  
                  
                  shortinput3 = input("")
                  if shortinput3 == "0":
                    shortinput2 = 0
                  if shortinput3 == "1" and manuord1ID > 1000:
                    manurewardroll()
                    manuord1ID = 999
                  if shortinput3 == "2" and manuord2ID > 1000:
                    manurewardroll()
                    manuord2ID = 999
                  if shortinput3 == "3" and manuord3ID > 1000:
                    manurewardroll()
                    manuord3ID = 999

                if shortinput2 == "0":
                  shortinput = 0

              if active_expansion // 10 == 4:
                print(f"{color.white}current expansion: vengeance expansion!")
                if active_expansion % 10 == 1:
                  print(f"{color.bgreen}(stage 1) bob's shop is closed?, must kill wildlife for food...")
                  print(f"{color.red}(stage 2) kill main characters, and bring them back to keep them in there misery: gain 5 maxhp+hp for killing, take 5 for losing")
                  print(f"{color.red}(stage 3) the hitlist")

                if active_expansion % 10 == 2:
                  print(f"{color.bgreen}(stage 1) bob's shop is closed?, must kill wildlife for food...")
                  print(f"{color.bgreen}(stage 2) kill main characters, and bring them back to keep them in there misery: gain 5 maxhp+hp for killing, take 5 for losing")
                  print(f"{color.red}(stage 3) the hitlist")

                if active_expansion % 10 == 3:
                  print(f"{color.bgreen}(stage 1) bob's shop is closed?, must kill wildlife for food...")
                  print(f"{color.bgreen}(stage 2) kill main characters, and bring them back to keep them in there misery: gain 5 maxhp+hp for killing, take 5 for losing")
                  print(f"{color.bgreen}(stage 3) the hitlist")
  
                print(f"{color.white}")
                print("reputation =", vrep)
                if active_expansion % 10 == 3:
                  print("1 to view orders")
                print("(0) back")

                shortinput2 = input("")
                while shortinput2 == "1" and active_expansion % 10 == 3:
                  print(f"\033[H\033[2J", end="")
                  print("you pull out the order sheet...")
                  time.sleep(textspeed)
                  print(f"\033[H\033[2J", end="")
                  print("orders (rewards are randomized, refresh every day)):")
                  if manuord1ID != 999:
                    print(f"{color.red}{manuord1}")
                  if manuord2ID != 999:
                    print(f"{color.blue}{manuord2}")
                  if manuord3ID != 999:
                    print(f"{color.yellow}{manuord3}")
                  print(f"{color.white}")
                  print("0 to go back")

                  if manuord1ID > 1000:
                    print("1 to claim order 1 reward!")

                  if manuord2ID > 1000:
                    print("2 to claim order 2 reward!")

                  if manuord3ID > 1000:
                    print("3 to claim order 3 reward!")
                  
                  
                  shortinput3 = input("")
                  if shortinput3 == "0":
                    shortinput2 = 0
                  if shortinput3 == "1" and manuord1ID > 1000:
                    manurewardroll()
                    manuord1ID = 999
                  if shortinput3 == "2" and manuord2ID > 1000:
                    manurewardroll()
                    manuord2ID = 999
                  if shortinput3 == "3" and manuord3ID > 1000:
                    manurewardroll()
                    manuord3ID = 999

                if shortinput2 == "0":
                  shortinput = 0
              
                    
                  
          if debugmode == 1:
            print("day start 2")

      print("")
  except endrun:
    runactive = 0

