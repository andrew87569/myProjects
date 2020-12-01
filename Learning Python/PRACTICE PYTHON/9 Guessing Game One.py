# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# - Keep the game going until the user types “exit”
# - Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

a = random.randint(1, 100)
guesses = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    
    if guess == "exit":
            break
    else:
        try:
            if int(guess) in range(1, 101):
                guess = int(guess)
                if guess < a:
                    print("\nToo low!\n")
                    guesses += 1
                    continue
                
                elif guess > a:
                    print("\nToo high!\n")
                    guesses += 1
                    continue
                
                elif guess == a:
                    print("\nExactly right!")
                    guesses += 1    
                    
                    if guesses == 1:
                        print("It took you 1 guess!")
                        break
                    
                    elif guesses > 1:
                        print("It took you " + str(guesses) + " guesses!")
                        break
            else:
                print("\nInvalid input. Please guess a number between 1 and 9, or type \"exit\" to end the game.\n")
                continue
        
        except ValueError:
                print("\nInvalid input. Please guess a number between 1 and 9, or type \"exit\" to end the game.\n")
                continue