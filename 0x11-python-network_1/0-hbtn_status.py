#!/usr/bin/python3
"""some commentary"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as my_req:
        respuesta = my_req.read()
        tipo = type(respuesta)
        decoded = respuesta.decode('utf8')
        print("Body response:")
        print("\t- type: {}".format(tipo))
        print("\t- content: {}".format(respuesta))
        print("\t- utf8 content: {}".format(decoded))
