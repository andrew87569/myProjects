# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
# and print out the results to the screen. I have a .txt file for you, if you want to use it!

with open('nameslist.txt', 'r') as open_file:
    read_file = open_file.read().splitlines()
    open_file.close()
names = {}

for line in read_file:
    if line in names:
        names[line] += 1
    elif line not in names:
        names[line] = 1

print(names)

# Extra:
# - Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, 
#   and count how many of each “category” of each image there are.

with open('Training_01.txt', 'r') as f:
    read_file = f.read().splitlines()
    f.close()

categories = {}

for jpg in read_file:
    x = jpg.split('/')[2]
    if x not in categories:
        categories[x] = 1
    elif x in categories:
        categories[x] += 1
    
print(categories)