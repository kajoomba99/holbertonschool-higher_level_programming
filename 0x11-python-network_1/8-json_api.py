#!/usr/bin/env python3
"""some commentary"""
import requests
import sys


try:
    q = sys.argv[1]
except Exception as e:
    q = ""

r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    json_res = r.json()
    if json_res == {}:
        print("No result")
    else:
        u_id = json_res['id']
        name = json_res['name']
        print("[{}] {}".format(u_id, name))
except Exception as e:
    print("Not a valid JSON")
