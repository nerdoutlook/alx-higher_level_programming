#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    try:
        a / 1 == a
        b / 1 == b
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        print("{} + {} = {}".format(a, b, add(a, b)))
