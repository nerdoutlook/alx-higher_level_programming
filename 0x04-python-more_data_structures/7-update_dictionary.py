#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update_ = {key: value}
    a_dictionary.update(update_)
    return(a_dictionary)


"""
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print(new_dict)
print("-------------")
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print(new_dict)
print("-------------")
"""
