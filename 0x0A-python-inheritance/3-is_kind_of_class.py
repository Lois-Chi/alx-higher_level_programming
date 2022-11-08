#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Return if the object is an instance of a class"""
    return isinstance(obj, a_class)
