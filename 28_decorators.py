# Decorators


# Simple Decorator

def star(function):

    def inner():
        print("*" * 40)
        function()
        print("*" * 40)

    return inner


def hello():
    print("Hello Python")


new_function = star(hello)
new_function()


# Using @ Decorator Syntax

def star(function):

    def inner():
        print("*" * 40)
        function()
        print("*" * 40)

    return inner


@star
def welcome():
    print("Welcome")


welcome()


# Decorator with Arguments

def check_zero(function):

    def inner(x, y):
        if y == 0:
            print("Division by zero is not allowed.")
        else:
            function(x, y)

    return inner


@check_zero
def divide(x, y):
    print(x / y)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

divide(a, b)
