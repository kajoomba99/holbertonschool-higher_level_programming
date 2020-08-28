#!/usr/bin/python3
"""Some commentary"""
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[2]
    repo = argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        user,
        repo
    )
    try:
        req = requests.get(url).json()
        for i in range(10):
            sha = req[i].get('sha')
            author_name = req[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except Exception as e:
        pass
