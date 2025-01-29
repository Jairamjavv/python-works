a = [1,2,3,4,5,6,7]
b = a[:] # deep copy or full slice
c = a # shallow copy

print(a)
# [1, 2, 3, 4, 5, 6, 7]

print(b)
# [1, 2, 3, 4, 5, 6, 7]

print(c)
# [1, 2, 3, 4, 5, 6, 7]

# change in 'a'' results in change in 'c' but not in 'b'.
a[2]=100

print(a)
# [1, 2, 100, 4, 5, 6, 7]

print(b)
# [1, 2, 3, 4, 5, 6, 7]

print(c)
# [1, 2, 100, 4, 5, 6, 7]
