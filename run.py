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

#check for win or tie

#switch the player

#check again after switch for win or tie


# run the game

printBoard(board)