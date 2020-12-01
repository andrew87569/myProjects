# You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy ... After you’ve written the program, try to find the optimal strategy!

import random

def guess():
  print('''--------- Welcome to the guessing game! ---------

Think of a number 0 - 100.

I will guess the number: tell me if it is `too high` or `too low`.
If I am right, respond with `yes`. To exit the game, type `exit`.''')
  
  guesses = 0
  nums = list(range(0,101))
    
  while True:
    num = random.choice(nums)
    guesses += 1
    answer = input("\nIs it " + str(num) + "? ")
    
    if answer == 'too high':
      nums = [i for i in nums if i < num]
          
    elif answer == 'too low':
      nums = [i for i in nums if i > num]
          
    elif answer == 'yes':
      if guesses == 1:
        print("It took 1 guess!")
      else:
        print("\nIt took " + str(guesses) + " guesses!")
      break
    
    elif answer == 'exit':
      break
    
    else:
      guesses -= 1
      print("Incorrect input.")

guess()