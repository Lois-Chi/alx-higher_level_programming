#!/usr/bin/python3
"""Sends a request and displays the request ID"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as request:
        print(request.headers.get('X-Request-Id'))
