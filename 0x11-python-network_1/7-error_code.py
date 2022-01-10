#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":

    URL = sys.argv[1]
    email = sys.argv[2]
    response_text = requests.post(URL, data={"email": email})
    string = response_text.decode('utf-8')
    print("Your email is: {}".format(string))


    try:
        with urllib.request.urlopen(URL) as response:
            response_text = response.read()
            string = response_text.decode('utf-8')
            print(string)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
