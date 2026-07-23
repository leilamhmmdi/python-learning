# Even or odd
def even_or_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))

print(even_or_odd(number))


# Maximum of two numbers
def maximum(x, y):

    if x > y:
        return x

    return y


a = int(input("First number: "))
b = int(input("Second number: "))

print(maximum(a, b))


# Smallest of three numbers
def smallest(x, y, z):

    if x <= y and x <= z:
        return x

    if y <= x and y <= z:
        return y

    return z


a = int(input("Enter x: "))
b = int(input("Enter y: "))
c = int(input("Enter z: "))

print(smallest(a, b, c))
