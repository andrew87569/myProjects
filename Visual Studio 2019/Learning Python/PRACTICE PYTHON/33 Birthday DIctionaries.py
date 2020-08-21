# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.

npcebBdays = {
    'Andrew Clark': '06/22/2003',
    'James Pate': '10/14/2003',
    'Terrance Pollard': '9/29/2003',
    'Moayad AlBayyari': '12/26/2003',
    'Yeshua Alvarado': '01/18/2003',
    'Kevin Ruiz-Virgin': '03/30/2003',
    'Andres Mejia-Peña': '11/19/2002',
    'Demetrio Maya': '10/14/2002'
}

print('Welcome to the NPC Energy Boys birthday dictionary. We have the birthdays of:')
print("\n".join(npcebBdays.keys()))


while True:
    name = input('Who\'s birthday would you like to look up?\n')
    
    if name in npcebBdays.keys():
        print(name + '\'s birthday is ' + npcebBdays[name])
        break
    else:
        print('That name is not in the dictionary.')
        continue