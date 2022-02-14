alive = True
currentRoom = 1
caveMap = {
  1:[3, 4, 2],
  2:[1, 4, 5, 7],
  3:[1, 4, 9],
  4:[1, 2, 3, 11, 8, 7],
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

def niceExitList(roomExits):
  global alive
  numExits = len(roomExits)
  if numExits== 0:
    alive = False
    return "you are trapped! This room has no exits and you are starved"
  if numExits == 1:
    return f"this room's only exit is to room {roomExits[0]}"
  if numExits == 2:
    return f"This room has exits to rooms {roomExits[0]} and {roomExits[1]}"

  niceList = "this room has exits to rooms:" 
  for exitNum in range(numExits-1):
    niceList += f"{roomExits[exitNum]}, "
  niceList += f"and {roomExits[-1]}."

  return niceList


def look():
  print(f"you are in room {currentRoom}")
  print(niceExitList(caveMap[currentRoom]))
  
def move():
  global currentRoom
  nextRoom = int(input("where would you like to go?"))
  if nextRoom not in caveMap[currentRoom]:
    print(f"i'm sorry, you cannot get in to room {nextRoom} from here")
    return
    if nextRoom not in caveMap:
      print(f"Oh no! Room {nextRoom} doesnt exist")
      return
  currentRoom = nextRoom

print("hunt the wupus")
print()
while alive:
  look()
  if not alive:
    break
  nextAction = input("\nwhats next? ")
  if nextAction.lower()[0] == "m":
    move()
    print("lets move!")
    continue
  if nextAction.lower()[0] == "q":
    break
  print (f"I'm sorry, I don't know how to do '{nextAction}'.")
  print ("I do know how to quit!")