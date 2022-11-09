#!/usr/bin/python3

"""
Function that reads a text file.
"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
