#!/usr/bin/python3

# THIS PROJECT INTRODUCES EXCEPTIONS HANDLING IN PYTHON
def safe_print_list(my_list=[], x=0):
    """USING TRY AND EXCEPT TO PRINT
    CERTAIN ELEMENTS/ITEMS TO THE
    STANDARD OUTPUT
    """
    count = 0
    try:
        for item in my_list[0:x]:
            count += 1
            print(item, end='')
        print()
        return count
    except Exception:
        for item in my_list[:]:
            count += 1
            print(item, end='')
        print()
