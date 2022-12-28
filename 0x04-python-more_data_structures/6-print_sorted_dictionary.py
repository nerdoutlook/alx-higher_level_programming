#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for index in sorted(a_dictionary):
        if a_dictionary is None:
            print(a_dictionary)
        print("{}: {}".format(index, a_dictionary[index]))


"""
a_dictionary = {}
a_dictionary = { 'language': "C", 'Number': 89,
                 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
"""
