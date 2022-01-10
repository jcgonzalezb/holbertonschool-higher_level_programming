#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":

    URL = 'https://intranet.hbtn.io/status'
    response = requests.get(URL)
    data = response.content
    string = data.decode('utf-8')
    print('Body response:')
    print("\t- type: {}".format(type(string)))
    print("\t- content: {}".format(string))
