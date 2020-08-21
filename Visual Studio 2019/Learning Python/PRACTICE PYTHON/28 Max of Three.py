# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

import random

nums = []
for num in range(3):
    num = random.choice(range(1,100))
    print(num)
    nums.append(num)
nums = sorted(nums)
print('Largest:',nums[-1])