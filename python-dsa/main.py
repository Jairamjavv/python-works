import random
from gcd import gcd1, gcd2, gcd3, gcd4, gcd5, gcd6, gcd7, gcd8

gcd_num = (random.randint(1,100), random.randint(1,100))

# testing gcd method 1
print(f"The gcd1 for {gcd_num[0]}, {gcd_num[1]} is: {gcd1(gcd_num)}")

# testing gcd method 2
print(f"The gcd2 for {gcd_num[0]}, {gcd_num[1]} is: {gcd2(gcd_num)}")

# testing gcd method 3
print(f"The gcd3 for {gcd_num[0]}, {gcd_num[1]} is: {gcd3(gcd_num)}")

# testing gcd method 4
print(f"The gcd4 for {gcd_num[0]}, {gcd_num[1]} is: {gcd4(gcd_num)}")

# testing gcd method 5
print(f"The gcd5 for {gcd_num[0]}, {gcd_num[1]} is: {gcd5(gcd_num)}")

# testing gcd method 6
print(f"The gcd6 for {gcd_num[0]}, {gcd_num[1]} is: {gcd6(gcd_num)}")

# testing gcd method 7
print(f"The gcd7 for {gcd_num[0]}, {gcd_num[1]} is: {gcd7(gcd_num)}")

# testing gcd method 8
print(f"The gcd8 for {gcd_num[0]}, {gcd_num[1]} is: {gcd8(gcd_num)}")