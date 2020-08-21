# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, 
# and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

import numpy

def checkTTTgame(game):
        
        # Check horizontal
        for y in range(3):
                if game[y][0] == game[y][1] == game[y][2] and game[y][0] != 0:
                        return print("Player " + str(game[y][0]) + " wins with horizontal")
        
        # Check vertical
        for x in range(3):
                if game[0][x] == game[1][x] == game[2][x] and game[0][x] != 0:
                        return print("Player " + str(game[0][x]) + " wins with vertical.")
        
        # Check Diagonal
        if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0] and game[0][0] != 0:
                return print("Player " + str(game[0][0]) + " wins with diagonal.")
        else:
                return print("No winner.")

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

checkTTTgame(game)

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

checkTTTgame(winner_is_2)

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

checkTTTgame(winner_is_1)

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

checkTTTgame(winner_is_also_1)

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

checkTTTgame(no_winner)

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

checkTTTgame(also_no_winner)