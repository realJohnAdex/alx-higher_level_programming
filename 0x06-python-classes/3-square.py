#!/usr/bin/python3
"""This is a module defining a new object Square"""


class Square:
    """A simple imnplementation of a Square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of the square. """
        return (self.__size ** 2)
