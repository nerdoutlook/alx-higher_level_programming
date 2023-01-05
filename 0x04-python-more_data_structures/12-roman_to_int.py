#!/usr/bin/python3
def roman_to_int(roman_string):
    digits = []
    digit = 0
    roman_numeral_base_list = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
                               'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
                               'X': 10, "XX": 20, "XXX": 30, "XL": 40,
                               "L": 50, "LX": 60, "LXX": 70, "LXXX": 80,
                               "XC": 90, "C": 100, "CC": 200, "CCC": 300,
                               "CD": 400, "D": 500, "DC": 600, "DCC": 700,
                               "DCCC": 800, "CM": 900, "M": 1000, "MM": 2000,
                               "MMM": 3000}
    if roman_string in roman_numeral_base_list.keys():
        value = roman_numeral_base_list.get(roman_string)
        return(value)
        pass
    for alphabet in roman_string:
        if alphabet in roman_numeral_base_list:
            digits.append(roman_numeral_base_list.get(alphabet))

    if len(digits) > 1:
        for num in digits:
            digit = digit + num
        return(digit)


"""
roman_string = "X"
print("{} = {}".format(roman_string, roman_to_int(roman_string)))
"""
"""
roman_string2 = "XXX"
print("{} = {}".format(roman_string2, roman_to_int(roman_string2)))
"""
