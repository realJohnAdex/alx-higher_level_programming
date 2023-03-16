#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    for k, v in a_dictionary.items():
        if v == value:
            del_list.append(k)
    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
