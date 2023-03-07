#!/usr/bin/python3
for tens in range(9):
    for unit in range((tens + 1), 10):
        if tens != unit:
            print(f"{tens:d}", end="")
            if (tens == 8 and unit == 9):
                print(f"{unit:d}")
            else:
                print(f"{unit:d}", end=", ")
