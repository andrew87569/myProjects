# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
# sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def get_num(prompt="Please enter a number: "):
    return int(input(prompt))

def gen_fib(num):
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        for _ in range(3, num + 1):
            fib.append(fib[-1] + fib[-2])
    return fib

print(gen_fib(num=get_num("How many numbers in the sequence? ")))