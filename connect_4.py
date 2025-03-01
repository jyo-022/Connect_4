import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]  # 6x7 empty board

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print("   ", end=" |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    """Checks if the given player (🔵 or 🔴) has won"""
    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if all(gameBoard[row][col + i] == chip for i in range(4)):
                print("\nGame over!", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical
    for row in range(rows - 3):
        for col in range(cols):
            if all(gameBoard[row + i][col] == chip for i in range(4)):
                print("\nGame over!", chip, "wins! Thank you for playing :)")
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(gameBoard[row - i][col + i] == chip for i in range(4)):
                print("\nGame over!", chip, "wins! Thank you for playing :)")
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(gameBoard[row + i][col + i] == chip for i in range(4)):
                print("\nGame over!", chip, "wins! Thank you for playing :)")
                return True

    return False

def coordinateParser(inputString):
    """Converts column letter to index and finds the lowest available row"""
    colMap = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    
    if inputString[0] in colMap:
        col = colMap[inputString[0]]
        row = getLowestAvailableRow(col)
        if row is not None:
            return [row, col]
    return None  # Invalid or full column

def getLowestAvailableRow(column):
    """Finds the lowest available row in the given column"""
    for row in range(rows - 1, -1, -1):  # Start from bottom row
        if gameBoard[row][column] == "":
            return row
    return None  # Column is full

def isSpaceAvailable(column):
    """Checks if there's space in the given column"""
    return getLowestAvailableRow(column) is not None

def playerMove():
    """Handles the player's move"""
    while True:
        spacePicked = input("\nChoose a column (A-G): ").upper()
        coordinate = coordinateParser(spacePicked)
        if coordinate:
            modifyArray(coordinate, '🔵')
            return
        else:
            print("Invalid move! Try again.")

def cpuMove():
    """Handles the CPU's move"""
    while True:
        cpuColumn = random.choice(possibleLetters)
        cpuCoordinate = coordinateParser(cpuColumn + "0")  # Find lowest row in column
        if cpuCoordinate:
            modifyArray(cpuCoordinate, '🔴')
            print(f"\nComputer placed 🔴 in column {cpuColumn}")
            return

# Game Loop
turnCounter = 0
while True:
    printGameBoard()

    if turnCounter % 2 == 0:
        playerMove()
        winner = checkForWinner('🔵')
    else:
        cpuMove()
        winner = checkForWinner('🔴')

    if winner:
        printGameBoard()
        break

    turnCounter += 1
