#!/ussr/bin/env python3
"""some commentary"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    bad_r = requests.get(url)
    code = bad_r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(bad_r.text)
