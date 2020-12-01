# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Give a number: "))

if number % 4 != 0:
    if (number % 2) > 0:
        print("This number is odd.")
    else:
        print("This number is even.")
else:
    print("This number is a multiple of 4.")

num = int(input("Give a number to check: "))
check = int(input("Give a number to divide by: "))

if num % check == 0:
    print("This number divides evenly.")
else:
    print("This number will not divide evenly.")