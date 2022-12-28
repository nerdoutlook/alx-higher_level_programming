#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    else:
        pass
    return(a_dictionary)


"""
my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = 'a'
"""
"""
a_dictionary = {'language': "C",
                'Number': 89,
                'track': "Low",
                'ids': [1, 2, 3]}
#new_dict = simple_delete(a_dictionary, 'language')
"""
"""
new_dict = simple_delete(my_dict, key)
print(new_dict)
"""
