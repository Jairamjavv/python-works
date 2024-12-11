from datetime import datetime

# swapping two numbers
a: int = 100
b: int = 200
print(f"Before swapping, a:{a}, b:{b}")
a, b = b, a
print(f"After swapping, a:{a}, b:{b}")

# reversing a string
a: str = "Jairam"
print(f"Before reversing the string, a:{a}")
a = a[::-1]
print(f"After reversing the string, a:{a}")

# factorial of a number, 3 ways
a: int = 6
b: int = 6
c: int = 6
fact_a: int = lambda n: [1, 0][n > 1] or fact_a(n - 1) * n
fact_b: int = lambda n: fact_a(n - 1) * n if n > 1 else 1
fact_c: int = lambda n: [1, fact_a(n - 1) * n][n > 1]
print(f"Factorial of {a} is {fact_a(a)}")
print(f"Factorial of {b} is {fact_b(b)}")  # faster than fact_a
print(f"Factorial of {c} is {fact_c(c)}")  # faster than fact_a but similar to fact_b
print(datetime.now().strftime("%H:%M:%S.%f"))  # includes milliseconds

# prime numbers
p = 50
primes_p = list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, p)))
print(f"The prime numbers under {p} are {primes_p}")

# string palindrome
str_1 = "Malayalam"
str_2 = "malayalam"
palindrome = str_1.lower() == str_2[::-1].lower()
print(f"{str_1} == {str_2} ==> {palindrome} ")

# squaring numbers using list comprehension
print(
    f"The square of the following numbers\n {list(range(10))} are {[i**2 for i in range(10)]}"
)
# alternative way using lambda and map functions
print(
    f"The square of the following numbers\n {list(range(10))} are {list(map(lambda x: x**2, range(10)))}"
)

# even numbers
e_num = 100
print(
    f"list of even numbers under {e_num} are {list(filter(lambda x: x%2 == 0, range(e_num)))}"
)

# sum of first n numbers
from functools import reduce

s_num = 10
print(
    f"The sum of first {s_num} are {reduce(lambda x, y: x+y, range(s_num+1))}(inlcusive) and {reduce(lambda x, y: x+y, range(s_num))}(exclusive)"
)

"""
Good blog on learning lambda's in python:
https://blog.ashutoshkrris.in/mastering-lambdas-a-guide-to-anonymous-functions-in-python#heading-using-lambda-functions-as-arguments-in-higher-order-functions-map-filter-reduce

Another good blog covering python one liners
https://www.freecodecamp.org/news/python-one-liners/
"""

# making a dictionary from 2 lists, but the lists should be ordered accordingly
movie_name = ["Vikram", "Leo", "Kaithi", "Master", "Maanagaram"]
imdb_ratings = [8.3, 7.2, 8.4, 7.4, 8.1]
movie_ratings = dict(zip(movie_name, imdb_ratings))
"""
Below is an alternative method
movie_ratings = {k: v for k, v in zip(movie_name, imdb_ratings)}
"""
print(f"The Movie ratings are: {movie_ratings}")

# listing out things using enumerate function
print(
    f"List of movies made by Lokesh Kanagaraj are\n: {dict(enumerate(movie_name, start=1))}"
)


# joining string 5 times
print(
    f"Movie rating in increasing order {" > ".join([str(i) for i in sorted(imdb_ratings)][::-1])}"
)
