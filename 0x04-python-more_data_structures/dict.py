#!/usr/bin/python3
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
new_dictionary = {key: value for (key, value) in a_dictionary.items()}
d1 = {2: "two"}
for i in sorted(a_dictionary):
    a_dictionary.update(d1)
    print("{}: {}".format(i, a_dictionary[i]))
    
