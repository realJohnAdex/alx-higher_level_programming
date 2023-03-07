#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            upper = chr(ord(char) - 32)
        else:
            upper = char
        print("{}".format(upper), end='')
    print("".format())
