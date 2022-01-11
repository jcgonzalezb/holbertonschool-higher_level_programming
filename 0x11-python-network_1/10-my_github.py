#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":

    URL = 'https://api.github.com/user'
    response = requests.get(URL, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    r_json = response.json()
    print(r_json.get('id'))
