# 1.basic example
"""def greet():
    print("Hello, Python")
greet()"""


# Area of Triangle 
"""def calculate_area():
    length=10
    width=5
    area=length*width
    print(f"Area: {area}")
calculate_area()"""


# 2. Parameters vs arguments
"""def introduce(name,age):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce("Ravikumar",24)
introduce("Sreenu",23)"""


# Keyword Arguments:- Arguments passed by specifying parameter names:
"""def describe_pet(name,animal_type,age):
    print(f"{name} is a {age}-years-old {animal_type}")

describe_pet(animal_type="dog",name="Togo",age=3)
describe_pet(name="Lilly",age=1,animal_type="Cat")"""


# Default Parameters:- Parameters with default values:
"""def greet_user(name,greeting="Hello"):
    print(f"{greeting}, {name}")

greet_user("sreenu")
greet_user("Rake","Hi")
greet_user("Srikanth",greeting="Hey")"""


# 3. Return values:- Functions can return values using the return statement. If no return statement is used, the function returns None.
"""def add_numbers(a,b):
    result = a+b
    return result
sum = add_numbers(5,3)
print(sum)"""

# Multiple return values
"""def mul_return():
    name="Srinu"
    age=23
    return name,age
person_name,person_age = mul_return()
print(f"Name: {person_name}, Age: {person_age}")

person_info = mul_return()
print(person_info)"""

# Conditional Returns
"""def check_even_odd(num):
    if(num % 2 == 0):
        return "Even"
    else:
        return "Odd"
res = check_even_odd(7)
print(res)"""

# Early Return
"""def divide_num(a,b):
    if b == 0:
        return "Error: connot divide by zero"
    return a/b
print(divide_num(10,2))
print(divide_num(10,0))"""

# 4. *args and **kwargs :- These allow functions to accept variable numbers of arguments.
# *args (Arbitrary Positional Arguments) -> Collects extra positional arguments into a tuple:
"""def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
print(sum_all())"""

# Combining regular parameters with *args
"""def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Alice", "Bob", "Charlie")"""

# **kwargs (Arbitrary Keyword Arguments) -> Collects extra keyword arguments into a dictionary:
"""def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Srinu", age=23, city="Hyderabad")"""

# Combining regular parameters with **kwargs
"""def create_profile(name, **details):
    print(f"Profile for {name}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile("Srinu", age=23, job="Engineer", hobby="Reading")
"""

# Combining *args and **kwargs
"""def flexible_function(required_param, *args, **kwargs):
    print(f"Required: {required_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function("Hello", 1, 2, 3, name="Alice", age=25)"""


