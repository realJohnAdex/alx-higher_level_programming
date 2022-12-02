#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguments"""
    import sys

    argv = sys.argv
    res = 0
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        res += int(arg)

    print("{:d}".format(res))
