#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays only body of a 200 status code response.
curl -sL "$1"
