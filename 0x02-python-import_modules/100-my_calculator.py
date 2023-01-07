#!/usr/bin/python3
# _ _ _ _ BUILDING MY OWN CALCULATOR _ _ _ _
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operators = ['+', '-', '*', '/']
    a = 0
    b = 0
    # _ _ _ CHECKING IF THE ARGUMENTS SUM UP TO THREE
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
        exit(1)

    # _ _ COLLECTING THE TWO VALUES AND THE OPERATOR TO USE _ _
    i = 1
    for idx, num in enumerate(sys.argv[1:]):
        if idx == 1:
            a = int(num)
            continue
        elif idx == 3 and int(num) in range(0, 1000):
            b = int(num)
            continue
        # _ _ RETURN A FUNCTION BASED ON THE OPERATOR _ _
        elif idx == 2 and num in operators:
            if num == '+':
                print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))
            elif num == '-':
                print("{:d} - {:d} = {:d}".format(a, b, (sub(a, b))))
            elif num == '*':
                print("{:d} * {:d} = {:d}".format(a, b, (mul(a, b))))
            elif num == '/':
                print("{:d} / {:d} = {:d}".format(a, b, (div(a, b))))
            elif i == 2 and num not in ['+', '-', '*', '/']:
                print("Unknown operator. Available operators: +, -, * and /")
                print("1")
                exit(1)
        i += 1
