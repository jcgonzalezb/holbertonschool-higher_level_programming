#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]

    if lenght > 0:
        res = (lenght, first)
    else:
        res = None
    return res
