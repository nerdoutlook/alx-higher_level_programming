#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    container = []
    dummy = (0, )
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 > 2:
        for i, j in zip(tuple_a[:2], tuple_b):
            container.append(i + j)
    elif len2 > 2:
        for i, j in zip(tuple_a, tuple_b[:2]):
            container.append(i + j)
    else:
        for i, j in zip(tuple_a, tuple_b):
            container.append(i + j)

    return(tuple(container))
