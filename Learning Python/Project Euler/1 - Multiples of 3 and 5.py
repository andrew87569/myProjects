# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sumMultiples(a,b,c):
    multiplesSum = 0
    
    for num in range(1, c):
        if (num % a) == 0 or (num % b) == 0:
            multiplesSum += num
    
    return multiplesSum

print(sumMultiples(3,5,1000))