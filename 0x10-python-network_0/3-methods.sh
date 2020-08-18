#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl "$1" -Is | tr -d '\r' | sed -En 's/^Allow: (.*)/\1/p'
