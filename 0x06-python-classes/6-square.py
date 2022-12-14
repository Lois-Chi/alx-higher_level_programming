#!/usr/bin/python3
""" A class square."""
class Square():
    """Representation of a class square."""


    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the class square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        """The area of the Square"""
        return self.__size ** 2

    @property
    def size(self):
        """The size of the Square"""
        return self.__size

    @size.setter
    def size(self, SizeValue):
        """set size of the Square"""
        if type(SizeValue) != int:
            raise TypeError("size must be an integer")
        if SizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = SizeValue

    def my_print(self):
        """print the Square"""
        size = self.__size
        position = self.__position
        if size == 0:
            print()
            return
        for r in range(position[1]):
            print()
        for i in range(size):
            for spc in range(position[0]):
                print(" ", end="")
            for j in range(size):
                print("#", end="")
            print()

    @property
    def position(self):
        """The position of the Square"""
        return self.__position

    @position.setter
    def position(self, PositionValue):
        """set position of the Square"""
        if type(PositionValue) != tuple or len(PositionValue) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(val) != int for val in PositionValue):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in PositionValue):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = PositionValue
