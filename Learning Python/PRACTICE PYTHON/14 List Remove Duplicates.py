# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# - Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# - Go back and do Exercise 5 using sets, and write the solution for that in a different function.
def rm_dupe(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def rm_dupe2(x):
    return list(set(x))

a = [1, 1, 2, 2, 3, 3, 4, 4, 5]

print(a)
print(rm_dupe(a))
print(rm_dupe2(a))