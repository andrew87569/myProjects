# Write a password generator in Python. Be creative with how you generate passwords 
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:
# - Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string

def passwdgen(strength=input("Would you like a strong or weak password? ")):
    passwd = []
    characters = string.ascii_letters + string.digits + string.punctuation

    if strength == 'strong':
        length = int(input("How many characters for your password? "))
        for _ in range(1, length + 1):
            passwd.append(random.choice(characters))
        random.shuffle(passwd)
        return "".join(passwd)
    elif strength == 'weak':
        passwd = ['password', 'Password123', 'Blue', 'Red', 'Green']
        return random.choice(passwd)

print("Your password is",passwdgen())