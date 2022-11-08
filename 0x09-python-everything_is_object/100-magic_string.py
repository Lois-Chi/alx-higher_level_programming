#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "H", getattr(magic_string, "H", -1) + 1)
    return "Bestschool" + ", Bestschool" * magic_string.c
