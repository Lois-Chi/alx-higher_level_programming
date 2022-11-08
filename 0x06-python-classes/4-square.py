#!/usr/bin/python3
    """A square class."""


class Square:
    """ Representation of a square"""

    def __init__(self, size=0):
        """Initialization of the class square.
        Args:
           size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """The size of the Square"""
        return (self.__size)

    @size.setter
    def size(self, SizeValue):
        """set size of the Square"""
        if type(SizeValue) != int:
            raise TypeError("size must be an integer")
        elif SizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = SizeValue

     def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
