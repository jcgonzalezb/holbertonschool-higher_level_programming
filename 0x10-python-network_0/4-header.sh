#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX OPTIONS "$1" -i | grep 'Allow:' | cut -f2-10 -d' '