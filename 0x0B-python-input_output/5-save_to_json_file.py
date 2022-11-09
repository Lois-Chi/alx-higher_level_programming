#!/usr/bin/python3

"""
Function that writes an Object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
