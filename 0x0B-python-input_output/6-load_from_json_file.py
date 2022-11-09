#!/usr/bin/python3

"""
Function that creates an Object
"""

import json


def load_from_json_file(filename):
    """Create an Object"""
    with open(filename, 'r') as f:
        return json.load(f)
