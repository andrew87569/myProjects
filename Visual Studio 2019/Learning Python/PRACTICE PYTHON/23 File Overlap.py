# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.

def comparelists(list1, list2):
    overlaps = []
    for i in list1:
        if i in list2:
            overlaps.append(i)
    return overlaps

with open('primenumbers.txt', 'r') as f:
    primenums = f.read().splitlines()
    f.close()

with open('happynumbers.txt', 'r') as f:
    happynums = f.read().splitlines()
    f.close()

print(comparelists(primenums, happynums))