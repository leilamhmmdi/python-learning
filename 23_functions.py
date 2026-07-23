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
