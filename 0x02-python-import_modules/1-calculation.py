#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = "5"

    try:
        a / 1 == a
        b / 1 == b
    except ValueError as ve:
        print(ve)
        pass
    except TypeError as te:
        print(te)
        pass
    else:
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
