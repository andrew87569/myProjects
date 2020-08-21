# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word. 
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.

import random

def getWord():
    
    with open('hangman.txt','r') as f:
        words = f.read().splitlines()
    
    return words[int(random.choice(range(0,len(words)+1)))]

print(type(getWord()))