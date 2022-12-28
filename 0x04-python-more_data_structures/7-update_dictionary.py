#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update_ = {key: value}
    a_dictionary.update(update_)
    return(a_dictionary)


"""
print_sorted_dictionary = \
            __import__('6-print_sorted_dictionary').print_sorted_dictionary
my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "a"
value = "A"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
"""
"""
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("-------------")
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("-------------")
"""
