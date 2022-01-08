#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

curl -sLI -- "$1" | grep -i 'content-length' | tr -s '\t ' ' ' | cut -d ' ' -f 2
