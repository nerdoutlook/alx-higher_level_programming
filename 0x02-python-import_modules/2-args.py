#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    a = len(argv) - 1
    j = 1

    if a == 0:
        print("0 arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
        print("{}: {}".format(j, argv[1]))
    else:
        print("{} arguments:".format(a))
        for i in argv[1:]:
            print("{}: {}".format(j, i))
            j = j + 1
