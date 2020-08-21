# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# - Use binary search.

a = [1, 3, 5, 30, 42, 43, 500]

def inList(num, aList):
    for i in aList:
        if i != num:
            inList = False
            continue
        elif i == num:
            inList = True
            break
    return inList
        
print(inList(30, a))