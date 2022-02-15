import random
from enum import Enum

class WumpusState(Enum):
  DEAD = 0
  AWAKE = 1
  ASLEEP = 2

gameState = {
  "alive": True,
  "wumpusState":WumpusState.ASLEEP,
  "wumpusRoom": 1,
  "currentRoom": 1,
  "caveMap": {
    1:[3, 4, 2],
    2:[1, 4, 5, 7],
    3:[1, 4, 9],
    4:[1, 2, 3, 8],
    5:[2],
    6:[7],
    7:[6, 8, 4, 2],
    8:[4, 7,],
    9:[10, 12, 13, 3,],
    10:[9],
    11:[4, 13, 14],
    12:[9, 13],
    13:[12, 9, 11, 14],
    14:[13, 11, 15],
    15:[14, 16],
    16:[],
  }
}

def numOfRooms (state):
  count =0
  for room in state["caveMap"]:
    count += 1
  return count

def safeRandomRoom(state):
  while True:
   room = random.randint(1, numOfRooms(state))
   roomExits = state["caveMap"][room]
   if len(roomExits) > 0:
     break
  return room

def newGame (state) :
  if numOfRooms (state) < 2:
    print ("A game that only has one room is not supported")
    raise SystemExit
  while state["wumpusRoom"] == state["currentRoom"]:
    state["wumpusRoom"] = safeRandomRoom(state)
    state["currentRoom"] = safeRandomRoom(state)
  return

def niceExitList(state):
  currentRoom = state["currentRoom"]
  roomExits = state["caveMap"][currentRoom]
  numExits = len(roomExits)
  if numExits == 0:
    state["alive"] = False
    return "You are trapped! This room has no exits and you have starved"
  if numExits == 1:
    return f"This room's only exit is to room {roomExits[0]}"
  if numExits == 2:
    return f"This room has exits to rooms {roomExits[0]} and {roomExits[1]}"
  niceList = "This room has exits to rooms: "
  for exitNum in range(numExits-1):
    niceList += f"{roomExits[exitNum]}, "
  niceList += f"and {roomExits[-1]}."
  return niceList

def look(state):
  currentRoom = state["currentRoom"]
  print(f"You are in room {currentRoom}")
  if currentRoom == state["wumpusRoom"]:
    if state["wumpusState"] == WumpusState.ASLEEP:
      print("you see a sleeping wumpus")
    else:
      print("you see a wumpus looking back at you")
  print(niceExitList(state))

def move(state):
  currentRoom = state["currentRoom"]
  nextRoom = int(input("where would you like to go? "))
  if nextRoom not in state["caveMap"][currentRoom]:
    print(f"I'm sorry, you cannot get to room {nextRoom} from here.")
    return
  if nextRoom not in state["caveMap"]:
    print(f"Oh no! Room {nextRoom} doesn't even exist!")
    return
  state["currentRoom"] = nextRoom

def encounter(state):
  if state["currentRoom"] == state["wumpusRoom"]:
    if state["wumpusState"]==WumpusState.ASLEEP:
      print("you have woken the wumpus!")
      state["wumpusState"]== WumpusState.AWAKE
    else:
      print("you have been eaten by a wumpus")
      state ["alive"]= False

newGame(gameState)
print("Hunt the Wumpus")
print()
while gameState["alive"]:
  print("hint: The wumpus is in room {wumpusRoom}".format_map(gameState))
  look(gameState)
  encounter(gameState)
  if not gameState["alive"]:
    break
  nextAction = input("\nWhat's next? ")
  if nextAction.lower()[0] == "m":
    move(gameState)
    continue
  if nextAction.lower()[0] == "q":
    break
  print(f"I'm sorry, I don't know how to do '{nextAction}'.")
  print("I know how to quit.")
