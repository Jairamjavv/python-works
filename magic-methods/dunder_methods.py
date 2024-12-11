from datetime import datetime

"""
__repr__/repr()  and __str__/str()
"""
to_day = datetime.now()

print("__repr__: {}".format(to_day.__repr__()))
print("__str__: {}".format(to_day.__str__()))
print(repr(to_day))  # returns the str format
print(str(to_day))  # returns the str format