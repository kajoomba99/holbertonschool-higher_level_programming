#!/usr/bin/python3
"""some commentary"""
import requests

r = requests.get('https://intranet.hbtn.io/status')
content = r.text

print(f"""Body response:
    - type: {type(content)}
    - content: {content}""")
