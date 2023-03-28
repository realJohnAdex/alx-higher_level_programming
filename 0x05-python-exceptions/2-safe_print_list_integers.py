#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            print_count += 1
        except IndexError:
            raise
        except (TypeError, ValueError):
            continue
    print()
    return (print_count)
