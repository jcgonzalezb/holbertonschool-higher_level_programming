#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS "$1" -i | grep 'allow:' | cut -f2 -d' '
