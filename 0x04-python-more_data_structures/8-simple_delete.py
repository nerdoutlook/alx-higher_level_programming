#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key)
    return(a_dictionary)


"""
a_dictionary = {'language': "C",
                'Number': 89,
                'track': "Low",
                'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'language')
print(new_dict)
"""
