#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return(None)
    max_key = [key for key, value in a_dictionary.items() if value ==
               max(a_dictionary.values())]
    if len(max_key) == 1:
        max_key = max_key[0]
    return(max_key)


"""
#a_dictionary = {'John': 12, 'Bob': 14,
#                'Mike': 14, 'Molly': 16,
#                'Adam': 16}
a_dictionary = {}
new = best_score(a_dictionary)
print(new)
"""
