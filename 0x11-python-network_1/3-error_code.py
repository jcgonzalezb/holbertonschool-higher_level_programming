#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    URL = sys.argv[1]

    try:
        with urllib.request.urlopen(URL) as response:
            response_text = response.read()
            string = response_text.decode('utf-8')
            print(string)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
