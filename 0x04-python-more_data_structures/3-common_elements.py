#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for element in set_1:
        print(element)
        for element2 in set_2:
            print(element2)
            if element == element2:
                new_set.add(element)
    return(new_set)


"""
set_1 = { "Python", "Javascript" }
set_2 = { "Python", "Javascript" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
"""
"""
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
"""
