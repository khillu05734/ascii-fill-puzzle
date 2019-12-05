# COMP 1405 Assignment 5
# Name: John Appleseed
# Student number: 1010XXXXX

# main() is the function executed when the program starts
def main():
    totalMoves = 0
    # Loop through the five level files
    for i in range(1, 6):
        board = readLevel(i) # Read the file for the level and store it in a list
        displayBoard(board)
        complete = 0
        moves = 0
        # Keep asking the user to make a move until the board is in a completed state when checked
        while complete == 0:
            moves = moves + 1
            action = getUserAction(len(board), len(board[0]))
            fill(board, board[int(action[1])][int(action[2])], action[0], action[1], action[2])
            displayBoard(board)
            # Loop through each character to see if it's the last character the user inputted
            complete = 1
            for line in board:
                for char in line:
                    if char != action[0]:
                        complete = 0
        # Level completed
        totalMoves = totalMoves + moves
        print("Level " + str(i) + " Completed in " + str(moves) + " moves!")
    # Congratulate the user once all 5 levels are completed and display the total moves taken
    print("You Win! Thanks for playing!")
    print("Total moves: " + str(totalMoves))
    playAgain = input("Would you like to play again? (y/n): ")
    if (playAgain == "y" or playAgain == "yes"):
        main()
    # The program successfully ends if the answer is not "yes"

# readLevel() takes in a number, reads the text file for that level, and returns a list representation of it
def readLevel(num) -> list:
    # Read the file and convert it to a 2d list (list of lists of strings)
    try:
        with open("levels/ascii_fill_level" + str(num) + ".txt", "r") as file:
            lst = [list(line.strip()) for line in file]
            return(lst)
    except:
        # Display an error if the file cannot be read
        print("Error reading file levels/ascii_fill_level" + str(num) + ".txt")
        exit()

# displayBoard() takes a list and displays it inside a game board template based on the height and width of the list
def displayBoard(lst):
    count = -1
    print("   ", end="")
    for char in lst[0]:
        count = (count + 1) % 10
        print(count, end="")
    print("\n   ---------")
    count = -1
    for line in lst:
        count = count + 1
        print("{0:0=2d}".format(count) + "|", end="")
        for char in line:
            print(char, end="")
        print()

# getUserAction() takes in the height and width of the board and returns a single list of the user's inputs
def getUserAction(h, w) -> list:
    symbol = input("Enter a symbol: ")
    row = input("Select a row [0," + str(h - 1) + "]: ")
    col = input("Select a col [0," + str(w - 1) + "]: ")
    return [symbol, int(row), int(col)]

# fill() checks if the user's symbol, row, and column inputs are valid then recursively replaces neighbouring symbols at the list coordinates with the chosen symbol
def fill(board, strT, strS, intR, intC):
    if (intR < len(board) and intC < len(board[0]) and strT == board[intR][intC] and strT != strS):
        board[intR][intC] = strS # Replace the symbol at the current coordinates
        fill(board, strT, strS, intR + 1, intC) # Search down
        fill(board, strT, strS, intR - 1, intC) # Search up
        fill(board, strT, strS, intR, intC + 1) # Search right
        fill(board, strT, strS, intR, intC - 1) # Search left



main()