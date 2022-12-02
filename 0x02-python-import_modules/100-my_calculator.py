#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{a} {op} {b} = {res}".format(a=a, b=b, op=op, res=res))
