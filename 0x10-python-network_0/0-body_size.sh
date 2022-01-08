#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

curl -sI "$1" -o test | cat test | grep 'Content-Length:' | cut -f2 -d' '
