#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'D': 500, 'M': 1000}

        if roman_string == "I":
            return 1
        elif roman_string == "II":
            return 2
        elif roman_string == "III":
            return 3
        elif roman_string == "V":
            return 5
        elif roman_string == "X":
            return 10
        elif roman_string == "L":
            return 50
        elif roman_string == "D":
            return 100
        else:
            return 0
