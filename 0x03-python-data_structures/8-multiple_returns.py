#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        whats_in = (0, None)
        return whats_in
    else:
        length = len(sentence)
        first = sentence[0]
        whats_in = (length, first)
        return whats_in
