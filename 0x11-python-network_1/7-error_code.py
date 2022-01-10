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
