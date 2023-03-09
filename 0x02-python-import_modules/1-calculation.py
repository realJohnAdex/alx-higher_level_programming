#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add_rst = add(a, b)
    sub_rst = sub(a, b)
    mul_rst = mul(a, b)
    div_rst = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_rst))
    print("{:d} - {:d} = {:d}".format(a, b, sub_rst))
    print("{:d} * {:d} = {:d}".format(a, b, mul_rst))
    print("{:d} / {:d} = {:d}".format(a, b, div_rst))
