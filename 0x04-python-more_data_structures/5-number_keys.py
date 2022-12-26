#!/usr/bin/python3
def number_keys(a_dictionary):
    keys_count = 0
    for i in a_dictionary:
        keys_count += 1
    return(keys_count)


"""
a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
"""
