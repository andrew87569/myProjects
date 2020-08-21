# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("What is your name: ")
age = int(input("What is your age: "))
year = int(input("What is the current year: "))
number = int(input("How many times would you like to hear this: "))
hundred_yr = str((year - age) + 100)


print(("Your name is " + name + " and you are " + str(age) + " years old.\n") * number)
print(("You will be 100 in the year " + hundred_yr + ".\n") * 3)