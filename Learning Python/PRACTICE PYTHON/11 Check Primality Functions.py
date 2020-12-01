# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def get_num(prompt="Please enter a number: "):
        try:
            return int(input(prompt))
        except ValueError:
            return print("Invalid Input.")

def is_prime(num):
    if num > 1:
        x = list(range(2, num))
        prime = True
        for i in x:
            if num % i == 0:
                prime = False
                break
        if prime:
            return print(str(num),"is prime.")
        if not prime:
            return print(str(num),"is not prime.")
    else:
        return print("Invalid Input.")

is_prime(num=get_num("Please enter a number > 1: "))