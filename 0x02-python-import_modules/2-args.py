#!/usr/bin/python3
# _ _ _ THIS PROJECT SHOWS HOW TO WORK WITH COMMANDLINE ARGUMENTS
if __name__ == "__main__":
    import sys

    # _ _ _ _TOTAL ARGUMENTS = total - name of program(1)
    n = len(sys.argv) - 1
    # _ _ _ CHECK IF N IS 0, 1 OR > 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(n))
    for i in range(n):
        print("{:d}: {}".format((i + 1), sys.argv[i + 1]))
