#!/usr/bin/python3
def no_c(my_string):
    o = ""
    for j in my_string:
        if j != "c" and j != "C":
            o += j
    my_string = o
    return my_string
