#!/usr/bin/python3
for tens in range(9):
    for unit in range((tens + 1), 10):
        if tens != unit:
            print("{:d}".format(tens), end="")
            if (tens == 8 and unit == 9):
                print("{:d}".format(unit))
            else:
                print("{:d}".format(unit), end=", ")
