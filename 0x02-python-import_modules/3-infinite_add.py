#!/usr/bin/python3
# _ _ _THIS PROGRAM IS AN INFINITE ADDING CALCULATOR _ _ _
if __name__ == "__main__":
    # _ _ DEFINING THE FLAG, ITERATOR AND SUM VARIABLES _ _
    import sys
    sum = 0
    if len(sys.argv) == 1:
        print("0")

    # _ _ FOR LOOP
    if len(sys.argv) > 1:
        for num in sys.argv[1:]:
            num = int(num)
            # _ _ _ SUMING THE ARGUMENTS _ _ _
            sum += num

        # _ _ _ PRINTING THE SUM OF ARGUMENT _ _ _
        print(sum)
