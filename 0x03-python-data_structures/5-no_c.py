#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    new_list = [item for item in my_list if item not in "Cc"]
    new_string = ''.join(new_list)
    return new_string
