#Liabraries

#global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
Winner = None
gameRunning = True      


#game board printing
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    

#take player input
    """
    this function get intergers from 1 to 9 
    (which showes 9 places in a game board.)
    as a input and also check validation of input.

    """
def playerInput(board):
    print("Enter a number form 1 to 9.")
    print("Each number represent a place on game board")
    print("if you eneter 1 number its shows you selcet first place on the board and so on...")
    global currentPlayer
    inp = int(input("Select a spot 1-9: "))
    if inp <= 0 or inp >=10:
         print("Invalid number...Input must be 1 to 9")
    elif inp >= 1 and inp <=9 and board[inp-1] != "-":
         print("Oops player is already in that spot!")
    else:
        board[inp-1] = currentPlayer



#check for win or tie

#switch the player

#check again after switch for win or tie


# run the game
"""
    Run a while loop to collect a valid data from the user
    via the terminal, and run all program functions
"""
while gameRunning:
    printBoard(board)
    playerInput(board)