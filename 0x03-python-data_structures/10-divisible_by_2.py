#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = [True if n % 2 == 0 else False for n in my_list]
    return bool_list
