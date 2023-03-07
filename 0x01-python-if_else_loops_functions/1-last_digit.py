#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if mod > 5:
    print(f"Last digit of {number:d} is {mod:d} and is greater than 5")
elif mod == 0:
    print(f"Last digit of {number:d} is {mod:d} and is 0")
elif mod < 6 and mod != 0:
    print(f"Last digit of {number:d} is {mod:d} and is less than 6 and not 0")
