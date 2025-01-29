import random as r

# method 1
def rec_mul(a, b, i=0):
    # stopping condition
    if i == b:
        return 0
    # recursive call
    return a+rec_mul(a, b, i+1)

# method 2
def rec_mul2(a, b):
    # stopping condition
    if b == 0:
        return 0
    # recursive call
    return a+rec_mul(a, b-1)

# inputs
num_a = r.randint(1,100)
num_b = r.randint(1,100)
# testing method 1
print(f"Multiplying {num_a}x{num_b}=",rec_mul(num_a, num_b))

# testing method 2
print(f"Multiplying {num_a}x{num_b}=",rec_mul2(num_a, num_b))
