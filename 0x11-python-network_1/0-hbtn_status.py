#!/usr/bin/python3
""" Python script that fetches a URL """
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        string = data.decode('utf-8')
        print("\t- utf8 content: {}".format(string))
