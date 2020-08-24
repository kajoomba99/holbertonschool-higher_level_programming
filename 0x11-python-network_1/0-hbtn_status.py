#!/usr/bin/python3
"""some commentary"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as my_req:
    respuesta = my_req.read()
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
         type(respuesta),
         respuesta,
         respuesta.decode('utf8')))
