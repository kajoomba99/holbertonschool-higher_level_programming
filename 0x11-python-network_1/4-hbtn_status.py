#!/usr/bin/python3
"""some commentary"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    content = r.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
