# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def gen_fib():
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    del fib[-1]
    return fib

def getEven(l):
    evens = []
    for num in l:
        if num % 2 == 0:
            evens.append(num)
    return evens

def listSum(l):
    total = 0
    for num in l:
        total += num
    return total

EvenFibTotal = listSum(getEven(gen_fib()))
print(EvenFibTotal)