# Simple function
def hello():
    print("Hello")


hello()


# Function with parameters
def add(x, y):
    return x + y


print(add(5, 10))


# Factorial
def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter a number: "))

print(factorial(number))


# User information
def user_info(first_name, last_name, age):

    return f"My name is {first_name} {last_name} and I am {age} years old."


first = input("First name: ")
last = input("Last name: ")
age = int(input("Age: "))

print(user_info(first, last, age))


# Simple Function
def func():
    print("Hello World")

func()


# Function with One Parameter
def func(x):
    print(2 * x)

number = int(input("Enter a number: "))
func(number)


# Function with Multiple Parameters
def func(x, y):
    print(2 * x + y)

func(5, 6)


# Function with Return
def func():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return 2 * x + y

result = func()
print(result)


# Return vs Print
def square(number):
    return number ** 2

print(square(5))


# Factorial Function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

number = int(input("Enter a number: "))
print(factorial(number))


# Using math.factorial()
# from math import factorial

number = int(input("Enter a number: "))
print(factorial(number))


# User Information Function
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))


def info(first_name, last_name, age):
    return f"My name is {first_name} {last_name} and I am {age} years old."


print(info(first_name, last_name, age))


# Even or Odd Function
def even_or_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))
print(even_or_odd(number))


# Find the Larger Number
def maximum(x, y):

    if x > y:
        return x

    return y


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(maximum(x, y))


# Find the Smallest Number
def smallest(x, y, z):

    if x <= y and x <= z:
        return x

    elif y <= x and y <= z:
        return y

    return z


x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

print("Smallest number:", smallest(x, y, z))
