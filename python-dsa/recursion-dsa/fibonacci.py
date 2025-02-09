# fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

print(f"The fibonacci series sum of {10} is {fib(10)}")

# fibonacci range
def fib(n, m):
    if m == n:
        return n
    if m == n+1:
        return n+1
    return fib(n, m-1)+fib(n, m-2)

print(f"The fibonacci series sum of {0} to {5} is {fib(0, 5)}")

