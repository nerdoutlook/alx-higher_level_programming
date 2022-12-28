#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        return(a_dictionary.pop(key))
    else:
        return(a_dictionary)


"""
a_dictionary = {'language': "C",
                'Number': 89,
                'track': "Low",
                'ids': [1, 2, 3]}
#new_dict = simple_delete(a_dictionary, 'language')
new_dict = simple_delete(a_dictionary, 'l')
print(new_dict)
"""
