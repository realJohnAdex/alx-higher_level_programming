#!/usr/bin/python3
def print_last_digit(number):
    """a function that prints the last digit of a number"""
    if number < 0:
        abs_number = abs(number)
        last_digit = abs_number % 10
    else:
        last_digit = number % 10
    print("{}".format(last_digit), end='')
    return last_digit
