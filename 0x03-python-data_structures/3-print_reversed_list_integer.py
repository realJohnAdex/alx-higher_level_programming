#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(item)) for item in my_list[::-1] if len(my_list)]

if __name__ == "__main__":
    print_reversed_list_integer()
