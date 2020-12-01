# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("Give a string: ")
list_str = list(string.lower())
reverse_string = list(reversed(list_str))

if reverse_string == list_str:
    print(string.title() + " is a palindrome.")
else:
    print(string.title() + " is not a palindrome.")