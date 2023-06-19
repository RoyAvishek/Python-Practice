# Write a program that validates if a given string follows a specific pattern using regular expressions.

import re

def chack_pattern(string, pattern):

    regex = re.compile(pattern)

    found = regex.fullmatch(string)

    if found:
        print("Given string follows the pattern")
    else:
        print("Given string does not follows the pattern")


pattern = r'^[A-Za-z]+\d{2}$'
string1 = "Aa23"

chack_pattern(string1,pattern)