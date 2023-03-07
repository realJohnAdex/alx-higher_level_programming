#!/usr/bin/python3
def fizzbuzz():
    """prints the numbers from 1 to 100 separated by a space"""
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        elif i % (3 * 5) == 0:
            print("FizzBuzz", end=' ')
        else:
            print("{}".format(i), end=' ')
