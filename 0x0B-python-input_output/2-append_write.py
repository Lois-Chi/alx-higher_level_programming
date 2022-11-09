#!/usr/bin/python3

"""
Function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """string at the end of a text file"""
    with open(filename, 'a') as f:
        c = f.write(text)
    return c
