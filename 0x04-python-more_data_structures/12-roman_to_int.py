#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    prev_num = 0
    num = 0
    for i in roman_string:
        if prev_num < roman_numeral[i]:
            num += roman_numeral[i] - (prev_num * 2)
        elif prev_num >= roman_numeral[i]:
            num += (roman_numeral[i])
            prev_num = roman_numeral[i]
    return num
