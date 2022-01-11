#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":

    URL = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    response = requests.post(URL, data={"q": letter})

    try:
        r_json = response.json()
        if r_json:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
