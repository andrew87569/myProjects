import random
import math

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else :
            b %= a
    return max(a, b)

def coPrime(a, b):
    return gcd(a, b) == 1

def approxPi():
    total = 0
    coPrimes = 0
    
    for _ in range(1000000):
        if coPrime(random.randint(1,1000000000),random.randint(1,1000000000)):
            coPrimes += 1
        total += 1

    x = coPrimes / total
    return math.sqrt(6/x)

print(approxPi())