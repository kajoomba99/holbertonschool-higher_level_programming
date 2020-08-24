#!/usr/bin/env python3
"""some commentary"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as my_req:
    respuesta = my_req.read()
    print(f"""Body response:
    - type: {type(respuesta)}
    - content: {respuesta}
    - utf8 content: {respuesta.decode('utf8')}""")
