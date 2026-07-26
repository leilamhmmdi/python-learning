# Function Arguments in Python

# Positional Arguments

def func(x, y, z):
    print(x + y + z)

func(2, 3, 4)


# Keyword Arguments

def func(x, y, z):
    print("x:", x)
    print("y:", y)
    print("z:", z)

func(x=1, y=2, z=3)


# Mixing Positional and Keyword Arguments

def func(x, y, z):
    print("x:", x)
    print("y:", y)
    print("z:", z)

func(1, y=2, z=3)


# Packing with *

x, y, *z = 1, 2, 3, 4, 5, 6, 7

print(x)
print(y)
print(z)


# Unpacking a List

numbers = [2, 5, 10]

def func(x, y, z):
    print(x)
    print(y)
    print(z)

func(*numbers)


# Unpacking a Dictionary

data = {
    "x": 1,
    "y": 20,
    "z": 5
}

def func(x, y, z):
    print(x)
    print(y)
    print(z)

func(**data)


# Default Parameters

def func(x=5, y=10, z=15):
    print(x)
    print(y)
    print(z)

func()
func(1, 2)


# Mixed Default Parameters

def func(x, y=10, z=15):
    print(x)
    print(y)
    print(z)

func(2)


# *args

def func(*args):
    print(args)

func(1, 2, 3, 4, 5)


# **kwargs

def func(**kwargs):
    print(kwargs)

func(x=1, y=2, name="Leila")


# Combination of All

def func(a, b=2, *c, **d):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

func(1, 2, 3, 4, 5, age=23, city="Tabriz")


# Keyword-only Arguments

def func(a, *, age, city):
    print(a)
    print(age)
    print(city)

func(1, age=23, city="Tabriz")


# Positional-only and Keyword-only

def func(a, b, /, c, d, *, e, f):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

func(1, 2, 3, d=4, e=5, f=6)
