"""
https://pythonprinciples.com/challenges
Write a function named capital_indexes. The function takes a single parameter, 
which is a string. Your function should return a list of all the indexes in the 
string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""


def capital_indexes(str_in):
    indexes = [i for i in range(len(str_in)) if str_in[i].isupper()]
    return indexes


print(capital_indexes("Python Is a Programming LanguagE."))
