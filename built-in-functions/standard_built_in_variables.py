# None - usually it is returned from functions that don’t explicitly return anything. Its truth value is false.

print(None)

"""
Ellipsis - This object is accessed through the literal ... or the built-in name Ellipsis. Its truth value is true. Special value used mostly in conjunction with extended slicing syntax for user-defined container data types.
"""


def custom_adder_1(a, b): ...


def custom_adder_2(a, b):
    return Ellipsis


print(custom_adder_1(100, 200))
print(custom_adder_2(10, 20))

print(...)
print([10, 20, ..., 100])

"""
Number - If you just want to check if an argument x is a number, without caring what kind, use isinstance(x, Number). Similarly there are Real, Rational, and Integral are available
"""
from numbers import Number, Real


num_a: int = 100
var_b: str = "100"
float_c: float = 20.123
imag_d = complex(3, 5)
print("If num_a:{} is a Number: {}".format(num_a, isinstance(num_a, Number)))
print("If num_a:{} is a Real number: {}".format(num_a, isinstance(num_a, Real)))
print(
    "If var_b:{} is a Number: {} or Real: {}".format(
        var_b, isinstance(var_b, Number), isinstance(var_b, Real)
    )
)
print(
    "If float_c:{} is a Number: {} or Real: {}".format(
        float_c, isinstance(float_c, Number), isinstance(float_c, Real)
    )
)
print(
    "If imag_d:{} is a Number: {} or Real: {}".format(
        imag_d, isinstance(imag_d, Number), isinstance(imag_d, Real)
    )
)
print(
    "If {} of imag_d:{} is a Number: {} or Real: {}".format(
        imag_d.real,
        imag_d,
        isinstance(imag_d.real, (Real)),
        isinstance(imag_d.real, Real),
    )
)
print(
    "If {} of imag_d:{} is a Number: {} or Real: {}".format(
        imag_d.imag,
        imag_d,
        isinstance(imag_d.imag, (Real)),
        isinstance(imag_d.imag, Real),
    )
)
