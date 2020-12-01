# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
import random

def getSOWPODS():
    
    with open('sowpods.txt','r') as f:
        words = f.read().splitlines()
    
    return words[int(random.choice(range(0,len(words)+1)))]

print(getSOWPODS())