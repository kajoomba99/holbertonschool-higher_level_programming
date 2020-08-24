#!/usr/bin/python3
"""some commentary"""
import urllib.request
import urllib.parse
from sys import argv


url = argv[1]
email = argv[2]
value = {'email': email}
data = urllib.parse.urlencode(value)
data = data.encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf8'))
