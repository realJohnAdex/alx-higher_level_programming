#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = -2
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = len(my_list)
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = len(my_list) + 1
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = 0
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
