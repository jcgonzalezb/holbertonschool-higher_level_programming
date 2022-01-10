#!/usr/bin/python3
"""
Python script  that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from requests.exceptions import HTTPError
import sys


if __name__ == "__main__":

    URL = sys.argv[1]

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except HTTPError as http_err:
        print("Error code: {}".format(http_err))
