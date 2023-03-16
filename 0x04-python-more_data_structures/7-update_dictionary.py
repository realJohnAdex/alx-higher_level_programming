#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k in list(a_dictionary):
        if k == key:
            a_dictionary.update({k: value})
        else:
            a_dictionary[key] = value
    return a_dictionary
