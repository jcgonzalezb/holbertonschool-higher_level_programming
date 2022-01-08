#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

curl -sI "$1" -o test |cat test | sed 's/.*Content-Length: //' | cut -d " " -f 1 | sed -n '5p'
