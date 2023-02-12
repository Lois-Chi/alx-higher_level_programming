#!/usr/bin/python3
"""Sends a request with the email and displays the body of the response"""

import requests
from sys import argv
import ssl

if __name__ == '__main__':
    context = ssl._create_unverified_context()
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
