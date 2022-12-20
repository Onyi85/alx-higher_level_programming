#!/usr/bin/python3
# _ _ This function devides 2 integers and print result
def safe_print_division(a, b):
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
