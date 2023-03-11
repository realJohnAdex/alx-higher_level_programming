#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argv[2] not in '+-/*':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
        if operator == '-':
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        if operator == '*':
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        if operator == '/':
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
