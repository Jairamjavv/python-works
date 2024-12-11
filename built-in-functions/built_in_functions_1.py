# abs() - returns the absolute value, i.e, |a| where 'a' is a real number

abs_a = -100
print("The absolute value for {} is: {}".format(abs_a, abs(abs_a)))

# id(obj) - returns the 'identity' of the object as an integer. Remains constant for same objects.

print("The id for {} is: {}".format(1, id(1)))
print(
    "Id for {} remains the same when ever used. For ex, id of {} is always = {}, whenever called ".format(
        1, 1, id(1)
    )
)

# continue from https://docs.python.org/3/library/functions.html
