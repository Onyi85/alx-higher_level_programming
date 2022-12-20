#!/usr/bin/python3
# _ THIS PROJECT BUILDS ON MODULE IN PYTHON
if __name__ == '__main__':
    """Display the addition of two numbers """
    from add_0 import add
    # _ _ DEFINING TWO VARIABLES _ _
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
