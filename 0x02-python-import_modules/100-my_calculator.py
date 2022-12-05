#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    op_list = ['+', '-', '*', '/']
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    try:
        if sys.argv[2] not in op_list:
            print("Unknown operator. Available: +, -, * and /")
            sys.exit(1)
    except ValueError:
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, int(a) + int(b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, int(a) * int(b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, int(a) - int(b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, int(int(a) / int(b))))
