#!/usr/bin/python3
"""some commentary"""
import urllib.request
import urllib.error
from sys import argv


url = argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
