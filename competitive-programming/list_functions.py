nums = range(1,10)

# function for map
def sq(a):
    return a**2
# implementing map
print(f"Square numbers are: {list(map(sq, nums))}")

# Filter
print(list(filter(lambda a: a%2==0, nums)))

# reduce
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum, nums))