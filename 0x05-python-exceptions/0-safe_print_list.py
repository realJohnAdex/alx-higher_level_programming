#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            print_count += 1
    except IndexError as err:
        pass
    finally:
        print()
        return (print_count)
