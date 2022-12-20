#!/usr/bin/python3
# _ _ _ _ HANDS ON EXPERIENCE WITH MODULES _ _ _ _ _
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    """Defining the two integers"""
    a = 10
    b = 5

    """Calling the Addition Function"""
    print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))

    """Calling the Subtraction Function"""
    print("{:d} - {:d} = {:d}".format(a, b, (sub(a, b))))

    """Calling the Multiplication Function"""
    print("{:d} * {:d} = {:d}".format(a, b, (mul(a, b))))

    """Calling the Division Function"""
    print("{:d} / {:d} = {:d}".format(a, b, (div(a, b))))
