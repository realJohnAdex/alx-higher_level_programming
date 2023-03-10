#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if 0 <= idx < (len(my_list_copy)):
        my_list_copy[idx] = element
    return my_list_copy


if __name__ == "__main__":
    new_in_list()
