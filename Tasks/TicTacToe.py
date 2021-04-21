table = ["-","-", "-", "-","-", "-", "-","-", "-"]
currentPlayer = "X"
gameOn = True

def display():
  print(table[0] + " | " + table[1] + " | " + table[2])
  print(table[3] + " | " + table[4] + " | " + table[5])
  print(table[6] + " | " + table[7] + " | " + table[8])

def attempt(inputLoc):
  if inputLoc not in range(1, 10):
    print("There is not such a location")
  elif table[inputLoc-1] == "-":
    table[inputLoc-1] = currentPlayer
    changePlayer()
  else:
    print("You entered to wrong location")

def changePlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  elif currentPlayer == "O":
    currentPlayer = "X"

def checkRows():
  global gameOn
  if table[0] == table[1] == table[2] != "-" or table[3] == table[4] == table[5] != "-" or table[6] == table[7] == table[8] != "-":
    return True
    
def checkColumns():
  global gameOn
  if table[0] == table[3] == table[6] != "-" or table[1] == table[4] == table[7] != "-" or table[2] == table[5] == table[8] != "-":
    print("Sagol")
    return True

def checkDioganals():
  global gameOn
  if table[0] == table[4] == table[8] != "-" or table[2] == table[4] == table[6] != "-":
    print("salam")
    return True

def checkTie():
  global gameOn
  if "-" not in table:
    return True

def checkStatus():
  global gameOn
  if checkColumns() or checkDioganals() or checkRows():
    gameOn = False
    changePlayer()
    display()
    print("\"" + currentPlayer + "\"" + " won the game!")
  elif checkTie():
    gameOn = False
    changePlayer()
    display()
    print("This is tie")

def game():
  display()
  attempt()

while gameOn:
  display()
  attempt(int(input("Where to go: ")))
  checkStatus()