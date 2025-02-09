# factorial
# 5! = 5*4*3*2*1
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(f"The factorial of {5} is {fact(5)}")