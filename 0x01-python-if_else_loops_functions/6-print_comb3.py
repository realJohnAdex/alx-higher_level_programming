#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        print("{:d}".format(i), end='')
        print("{:d}".format((i + j) % 10), end=', ')
