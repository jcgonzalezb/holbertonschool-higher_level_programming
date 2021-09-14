#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]

    if sentence == None:
        first = None

    res = (lenght, first)
    return res
