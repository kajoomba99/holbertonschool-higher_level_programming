#!/bin/bash
# takes in a URL, sends a request to that URL,
curl -Is "$1" -X GET | grep "Content-Length" | grep -oP '[0-9]+'
