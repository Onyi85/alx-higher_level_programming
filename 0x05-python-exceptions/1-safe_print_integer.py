#!/usr/bin/python3
# _ _ This function print an integer
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
