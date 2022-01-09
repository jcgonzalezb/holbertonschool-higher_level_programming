#!/usr/bin/python3
"""
Python script that takes in a URL, and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    URL = sys.argv[1]
    email = sys.argv[2]
    params = {
        "email": email
    }

    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")

    with urllib.request.urlopen(URL, data) as response:
        response_text = response.read()
        string = response_text.decode('utf-8')
        print(string)
