"""
https://pythonprinciples.com/challenges
Middle letter: Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. If there is no middle letter,
your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""


def mid(str_in):
    if len(str_in) % 2:
        mid_len = len(str_in) // 2
        return str_in[mid_len]
    else:
        return ""


print(mid("a"))
print(mid("abc"))
print(mid("abcd"))
