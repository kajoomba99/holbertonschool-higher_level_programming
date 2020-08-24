#!/usr/bin/python3
"""some commentary"""
import urllib.request


if __name__ == "__main__":
     with urllib.request.urlopen('https://intranet.hbtn.io/status') as my_req:
          respuesta = my_req.read()
          print("""Body response:
          - type: {}
          - content: {}
          - utf8 content: {}""".format(
               type(respuesta),
               respuesta,
               respuesta.decode('utf8')))
