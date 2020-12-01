# In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal.
# So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# 
# Bonus:
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version,
# keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.

import numpy

game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

def choiceTTT(plr,row,col):
    
    row = row - 1
    col = col - 1

    if game[row][col] == 0:
        
        if plr == 1:
            game[row][col] = 'X'

        elif plr == 2:
            game[row][col] = 'O'

        print(game[0],'\n',game[1],'\n',game[2])
    else:
        print("Please choose a place without a piece.")

def FillBoard(game):
    
    while True:
        
        checkFull = set()
        for y in range(3):
            for x in range (3):    
                checkFull.add(game[y][x])
        
        if 0 in checkFull:
                choiceTTT(int(input('Player: ')),int(input('Row: ')),int(input('Column: ')))
        
        elif 0 not in checkFull:
            return print('Game over - board was filled.')