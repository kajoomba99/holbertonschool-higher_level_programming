#!/usr/bin/python3
"""some commentary"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    bad_r = requests.get(url)
    try:
        bad_r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
    else:
        print(bad_r.text)
