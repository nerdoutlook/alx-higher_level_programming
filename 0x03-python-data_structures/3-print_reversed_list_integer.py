#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        pass
    else:
        my_list = reversed(my_list)
        for i in my_list:
            print("{:d}".format(i))
