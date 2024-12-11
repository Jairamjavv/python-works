"""
other uses of `*` and `/`
Source: https://www.youtube.com/watch?v=IysuuNzb9hg
"""


# arguments before `/` are considered positional arguments which means they have fixed spot
def myfunction_1(a, b, /, c, d):
    print(a, b, c, d)


myfunction_1(1, 2, 3, 4)
myfunction_1(10, 20, c=30, d=40)
try:
    myfunction_1(a=1, b=2, c=3, d=4)
except Exception as e:
    print(str(e))


# arguments after `*` are considered keyword arguments which means they have to be explicitely mentioned while calling the function
def myfunction_2(a, b, *, c, d):
    print(a, b, c, d)


myfunction_2(a=1, b=2, c=3, d=4)
try:
    myfunction_2(1, 2, 3, 4)
except Exception as e:
    print(str(e))
