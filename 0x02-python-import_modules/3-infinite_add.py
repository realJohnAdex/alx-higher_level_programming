#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    result = 0
    for arg in argv[1:]:
        result += int(arg)
    print("{:d}".format(result))
