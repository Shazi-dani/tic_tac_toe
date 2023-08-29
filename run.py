# import random module for generating random value for 2nd player

import random

# define a function which will set the board values

def setBoard():
    return ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# global variables
board = setBoard()

currentPlayer = "X"

winner = None

gameRunning = True

# game board printing
"""
define a function for desiging and printing game board
"""


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input


def playerInput(board):

    """
    this function get intergers from 1 to 9
    (which showes 9 places in a game board.)
    as a input and also check validation of input.
    """

    while True:
        print("Enter a number form 1 to 9.")
        print("Each number represent a place on game board")
        print("Number 1 shows you selcet first place on the board")
        global currentPlayer
        try:
            inp = int(input("Select a spot 1-9:\n"))
            if inp >= 1 and inp <= 9 and board[inp-1] == "-":
                board[inp-1] = currentPlayer
                break

            elif inp >= 1 and inp <= 9 and board[inp-1] != "-":
                print(f"Oops player is already in that spot!")
                continue

            elif inp <= 0 or inp >= 10:
                print(f"Invalid number...Input must be 1 to 9")
                continue 

        except ValueError:
            print(f"Invalid data,please try again.\n")
            continue
    


# check for win or tie
"""
Check if player won using the winning combinations or tie.
there is There are a total of 8 ways to arrange the same sign and win the game.
3 in rows,3 in colums and 2 diagonoly.so define 3 different
function for checking all possiblities.
"""


def checkRows(board):
    """
    define a function to check if all the signs are same
    in any row in the board.
    """
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkColumns(board):
    """
    define a function to check all data for the game board
    columns if any column have same data then return true
    """
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[2] != "-":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    """
    define a function to check all data for the game board
    diagonally if any diagonal have same data then return true
    """
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# check for tie a game


def checkIfTie(board):

    """
    define a function which cheks if all the spaces in the game
    board is filled then stop the game and sho a message that
    game is tie
    """
    
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        while True:
            inp = str(input("Do you want to play again, type yes or no:\n"))
            play_again = inp.lower()
            if play_again == "yes":
                gameStart()
                break
            elif play_again == "no":
                exit()
            else:
                print("Your input does not match requirements.\nYou need to either type 'yes' or 'no' please try again")
                print("")
                continue

# check win


def checkIfWin(board):
    """
    this function checks return values from checkRows, checkColumns
    and checkDiag if true then print the winner and ask the player
    "do you want to play agaain" the game
    """
    
    if checkRows(board) or checkColumns(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        while True:
            inp = str(input("Do you want to play again, type yes or no:\n"))
            play_again = inp.lower()
            if play_again == "yes":
                gameStart()
                break
            elif play_again == "no":
                exit()
            else:
                print("Your input does not match requirements.\nYou need to either type 'yes' or 'no' please try again")
                print("")
                continue



# switch the player
def switchPlayer():
    """
    this function is used for switching between 2 players
    """
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# switch to computer
def computer(board):
    """
    this function check if current player is 2nd player then generate
    a random value b/w 0-8 and check if that space is empty then select
    that spot for 2nd player.so no need to enter values for both players.
    then switch the player again
    """
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# check again after switch for win or tie


# run the game
"""
    Run a while loop to collect a valid data from the user
    via the terminal, and run all program functions
"""
def gameStart():
    board = setBoard()
    winner = None
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        switchPlayer()
        computer(board)
        checkIfWin(board)
        checkIfTie(board)


gameStart()