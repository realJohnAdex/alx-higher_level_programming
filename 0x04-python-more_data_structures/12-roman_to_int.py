#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0
    int_val = 0
    for ch in roman_string:
        if ch == 'M':
            int_val += 1000
        elif ch == 'D':
            int_val += 500
        elif ch == 'C':
            int_val += 100
        elif ch == 'L':
            int_val += 50
        elif ch == 'X':
            int_val += 10
        elif ch == 'V':
            int_val += 5
        elif ch == 'I':
            int_val += 1
        else:
            return 0
    return int_val
