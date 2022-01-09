#!/usr/bin/python3
""" Python script that fetches a URL """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        html = data.decode('utf-8')
        print("Body response:")
        print("	- type: {}".format(type(data)))
        print("	- content: {}".format(response.peek()))
        print("	- utf8 content: {}".format(html))
