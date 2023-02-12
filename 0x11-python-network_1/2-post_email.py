#!/usr/bin/python3
"""Displays the body of the response"""

import urllib.request
from sys import argv
import ssl

def main():
    ssl._create_default_https_context = ssl._create_unverified_context()
    body = urllib.parse.urlencode({'email': argv[2]})
    body = body.encode('ascii')
    with urllib.request.urlopen(argv[1], body) as url:
        print(url.read().decode('utf-8'))
if __name__ == "__main__":
    (main)
