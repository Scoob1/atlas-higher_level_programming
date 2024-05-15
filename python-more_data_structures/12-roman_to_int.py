#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    integer = 0
    prev_value = 0

    if roman_string is None:
        return integer
    elif isinstance(roman_string, int):
        return integer
    else:
        for char in roman_string:
            value = roman_dict[char]
            if value > prev_value:
                integer -= 2 * prev_value
            integer += value
            prev_value = value
        return integer
