#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    total = 0
    for i in my_list:
        total = total + i
    return(total)


"""
my_list = [1, 2, 3, 1, 4, 2, 5]
print(uniq_add(my_list))
"""
