#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    str1 = ""
    for i in range(0, length):
        if i == n:
            pass
        else:
            str1 = str1 + str[i]
    return str1
