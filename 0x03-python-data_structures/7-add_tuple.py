#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    container = []
    dummy = (0, )
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    new_tuple = ()

    if len1 == 0 and len2 == 0:
        return((0, 0))
    if len1 > 2:
        for i, j in zip(tuple_a[:2], tuple_b):
            container.append(i + j)
    elif len2 > 2:
        for i, j in zip(tuple_a, tuple_b[:2]):
            container.append(i + j)
    elif len1 == 1:
        new_tuple = tuple_a + dummy
        for i, j in zip(new_tuple, tuple_b):
            container.append(i + j)
    elif len2 == 1:
        new_tuple = tuple_b + dummy
        for i, j in zip(tuple_a, new_tuple):
            container.append(i + j)
    elif len1 == 0:
        new_tuple = tuple_a + dummy + dummy
        for i, j in zip(new_tuple, tuple_b):
            container.append(i + j)
    elif len2 == 0:
        new_tuple = tuple_b + dummy + dummy
        for i, j in zip(tuple_a, new_tuple):
            container.append(i + j)
    else:
        for i, j in zip(tuple_a, tuple_b):
            container.append(i + j)

    return(tuple(container))
