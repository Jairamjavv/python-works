"""Source: https://www.youtube.com/watch?v=cqQf3lEoN08"""

"""
eval: evaluate the string given
"""

source_code: str = "print('Welcome to Quick Calculator')"
eval(source_code)

# quick calculator
quick_calc: str = input("Enter Expression:")
print(eval(quick_calc))


"""
exec: execute
"""

source_code_exec: str = """
print("using exec() to execute this piece of code")
a = 100
b = 250
print(b//a)
"""
exec(source_code_exec)
