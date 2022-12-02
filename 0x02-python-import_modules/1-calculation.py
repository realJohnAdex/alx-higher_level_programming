#!/usr/bin/python3
if __name__ == "__main__":
    """imports functions from the file calculator_1.py, does some Maths"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    add_ = add(a, b)
    sub_ = sub(a, b)
    mul_ = mul(a, b)
    div_ = div(a, b)
    print("{} + {} = {}".format(a, b, add_))
    print("{} - {} = {}".format(a, b, sub_))
    print("{} * {} = {}".format(a, b, mul_))
    print("{} / {} = {}".format(a, b, div_))
