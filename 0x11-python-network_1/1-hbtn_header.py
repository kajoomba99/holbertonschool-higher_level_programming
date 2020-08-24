#!/usr/bin/python3
"""some commentary"""
import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.getheader("X-Request-Id"))
