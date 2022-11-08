#!/usr/bin/python3

"""A square class."""


class Square:
    """ Representation of a square"""

    def __init__(self, size=0):
        """Initialization of the class square.
        Args:
            size(int): size of the square.
        """
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area of the Square"""
        return self.__size ** 2
