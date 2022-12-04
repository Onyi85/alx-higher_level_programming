#!/usr/bin/python3
def islower(c):
    lowercase = list(range(97, 123))
    uppercase = list(range(65, 91))
    if ord(c) in lowercase:
        return True
    else:
        return False
