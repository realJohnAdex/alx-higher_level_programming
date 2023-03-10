#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    bool_list = [True if num % 2 == 0 else False for num in my_list]
    return bool_list


if __name__ == "__main__":
    divisible_by_2()
