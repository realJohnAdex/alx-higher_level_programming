#!/usr/bin/python3
"""This is a module defining a new object Square"""


class Square:
    """A simple imnplementation of a Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ This getter returns the value of private var 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ This getter returns the value of private var 'position'"""
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the area of the square. """
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #
        prints a blank line if __size equals zero """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" "*self.__position[0], end='')
                print("#"*self.__size)
