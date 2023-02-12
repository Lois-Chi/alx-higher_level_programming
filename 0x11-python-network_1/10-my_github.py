#!/usr/bin/python3

"""Uses the GitHub API to display ID"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get('https://api.github.com/user', auth=(argv[1],
                            argv[2]))
    if "json" not in response.headers.get('content-type'):
        print("Invalid JSON")
    else:
        response = response.json()
        print(response.get('id'))
