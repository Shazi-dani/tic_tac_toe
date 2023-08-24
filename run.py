#Liabraries

#global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
Winner = None
gameRunning = True      


#game board printing
"""
define a function for desiging and printing game board
"""
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    

#take player input
  
def playerInput(board):
    """
    this function get intergers from 1 to 9 
    (which showes 9 places in a game board.)
    as a input and also check validation of input.
    """
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
"""
Check if player won using the winning combinations or tie.
there is There are a total of 8 ways to arrange the same sign and win the game.
3 in rows,3 in colums and 2 diagonoly.so define 3 different function for checking all possiblities.
"""

def checkrows(board):
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


def checkcolumn(board):
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
    