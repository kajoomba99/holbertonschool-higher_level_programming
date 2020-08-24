#!/usr/bin/env python3
"""some commentary"""
import requests
from sys import argv


url = argv[1]
email = argv[2]
r = requests.post(url, data={'email': email})
print(r.text)
