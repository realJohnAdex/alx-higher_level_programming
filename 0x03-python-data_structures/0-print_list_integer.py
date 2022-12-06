#!/usr/bin/python3
def print_list_integer(my_list=[]):
    [print("{}".format(item)) for item in my_list if int(item) == item]
