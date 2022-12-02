#!/usr/bin/python3

if __name__ == "__main__":
    """Print the command line arguments"""
    import sys

    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i, arg in enumerate(argv):
            if i == 0:
                continue
            print("{}: {}".format(i, arg))
