#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]

    if sentence == 0:
        first = None

    res = (lenght, first)
    return res
