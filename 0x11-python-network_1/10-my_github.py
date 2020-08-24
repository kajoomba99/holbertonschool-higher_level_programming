#!/usr/bin/env python3
"""some commentary"""
import requests
from sys import argv


username = argv[1]
password = argv[2]
response = requests.get('https://api.github.com/user', auth=(username, password))
try:
	id = response.json()['id']
except Exception as e:
	id = None
finally:
	print(id)
