#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(item)) for item in my_list[::-1] if len(my_list)]
