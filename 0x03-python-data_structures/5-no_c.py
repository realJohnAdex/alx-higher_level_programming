#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char not in 'Cc':
            new_string += char
    return new_string


if __name__ == "__main__":
    no_c()
