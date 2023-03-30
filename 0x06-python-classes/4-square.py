#!/usr/bin/python3
"""This is a module defining a new object Square"""


class Square:
    """A simple imnplementation of a Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ This getter returns the value of private var size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns the area of the square. """
        return (self.__size ** 2)
