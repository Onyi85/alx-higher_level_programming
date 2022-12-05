#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii_val = ord(i)
        if ascii_val in range(97, 123):
            ascii_val -= 32
        print("{}".format(chr(ascii_val)), end='')
    print()
