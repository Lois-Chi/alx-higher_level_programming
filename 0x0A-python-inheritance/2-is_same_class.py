#!/usr/bin/python3

"""
Write a function that returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Return if the object is an instance of the class"""
    return type(obj) == a_class
