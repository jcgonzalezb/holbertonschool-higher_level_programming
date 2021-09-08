#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    i = 0
    for i in str:
        if ord(i) >= 97 and ord(i) < 122:
            new_string += chr(ord(i)-32)
        else:
            new_string += i
    print(new_string)
