#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    a = len(argv)
    j = 1
    
    if a == 1:
        print("0 arguments.".format(a))
    else:
        print("{} arguments:".format(a))
        for i in argv[1:]:
            print("{}: {}".format(j, i))
            j = j + 1
