import math

# create a class with constructor, decorator and generator
class Circle:
    # constructor or initializer
    def __init__(self, radius: int):
        self.radius = radius

    # non public method (private)
    def _calculate_r_square(self):
        return self.radius**2

    # method
    def calculate_area(self) -> float:
        return round(math.pi*(self._calculate_r_square()), 2)

    # name mangling / super protective
    def __just_print_the_radius(self):
        print(self.radius)

    

# instantiation. Circle is a concrete class.
c1 = Circle(5)
# c1: instance
print(f"Circle with radius:{c1.radius} has area:{c1.calculate_area()}")
# attribute name can be changed
c1.radius = 10
print(f"Circle with radius:{c1.radius} has area:{c1.calculate_area()}")
print(f"{c1.radius} as radius in c1 is an attribute")

'''
built-in vars() function, 
which returns a dictionary of all the members associated with the given object
'''
print(vars(c1))
# accessing the mangled method - bad practice
c1._Circle__just_print_the_radius()

print(c1.__dict__) # similar to using vars()

# Dynamic class
class Record:
    """This is a dynamic class"""

# creating a class object from JSON
john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

j = Record()
for k, v in john.items():
    # using setattr to set the value dynamically to Record
    # setattr<object, attribute variable, value>
    setattr(j, k, v)

print(j.__dict__)
print(getattr(j, "name", "default value")) # if 'name' doesn't exists in 'j' obj then show the 'default value'

# decorator or managed attributes
class CircleUpdated:
    def __init__(self, radius):
        self.radius = radius

    '''
    The @property decorator and @radius.getter essentially serve the same purpose.
    They define a getter method for an attribute. 
    However, @property is the primary way to define a read-only property, 
    while @radius.getter is an explicit way to define the getter if a property has multiple decorators (such as a setter or deleter)
    '''

    # If you only need a getter, just use @property.
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius_value):
        if not isinstance(radius_value, int | float) or radius_value <= 0:
            return ValueError("Only positive number is required")
        else:
            # Instead of self.radius = radius_value, it should be self._radius = radius_value to avoid infinite recursion.
            self._radius = radius_value

    @radius.getter
    def radius(self):
        # if called self.radius, which will lead to an infinite loop.
        return self._radius

c2 = CircleUpdated(12)
# using radius as getter
print(c2.radius)
c2.radius = 15
print(c2.radius)


# simple decorator
def add_decorator(func):
    def wrapper(*args, **kwargs):
        print("First")
        func(*args, **kwargs)
        print("second")    
    return wrapper

# calling the decorator
# method 1
def print_hi():
    print("Hi")
add = add_decorator(print_hi)
add()

# method 2 - pythonic way
@add_decorator
def print_hi_2_times():
    print("hi"*2)

print_hi_2_times()

## References
# https://realpython.com/python-getter-setter/
# https://realpython.com/primer-on-python-decorators/