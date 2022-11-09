#!/usr/bin/python3

"""
Function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Write a string to a text file"""
    with open(filename, 'w') as f:
        c = f.write(text)
    return c
