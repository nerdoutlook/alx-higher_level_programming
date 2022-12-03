#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    j = 0
    for i in str:
        if j == n:
            pass
        else:
            copy = copy + i
        j = j + 1
    return(copy)
