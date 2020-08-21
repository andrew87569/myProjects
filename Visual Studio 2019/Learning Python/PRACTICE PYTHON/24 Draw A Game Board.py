# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def drawBoard(x, y):
    across = ' ---'
    down = '|   '
    
    for y in range(0, y):
        print(across * x)
        print((down * x) + '|')
    print(' ---' * x)

drawBoard(int(input("How many columns would you like to draw? ")), int(input("How many rows would you like to draw? ")))