# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def largePrmFctr(num):
    factors = []
    for x in range(3,10000):
        if num % x == 0:
            factors.append(x)
    return factors[-1]

print(largePrmFctr(600851475143))