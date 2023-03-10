#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        big = my_list[0]
        for num in my_list:
            if num > big:
                big = num
        return big


if __name__ == "__main__":
    max_integer()
