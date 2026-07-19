"""
String Examples
"""

# String concatenation

x = "123"
print(x + "2345")

# String repetition

text = "hello"
print(text * 3)

# Convert string to integer

number = "123"
print(int(number) + 4)

# Floating-point precision

x = 0.3
y = 0.6

print(x + y)

# Single and double quotes

text = "I'm Leila"
print(text)

text = 'I\'m Leila'
print(text)

# Raw string

path = r"c:\download\new\telegram"
print(path)

# Multi-line string

message = """hello
world
how
are
you
?"""

print(message)

# String methods

text = "hello world"

print(text.capitalize())
print(text.isdigit())

# F-Strings
x = 20
print(f"Your mark is {x}")

x = 20.223456
print(f"Your mark is {x:.2f}")

x = 2034398575
print(f"Your mark is {x:,.2f}")

x = 20343985.2324
print(f"Your mark is {x:50,.2f}")

x = 20343985.2324
print(f"Your mark is {x:050,.2f}")

x = 20343985.2324
print(f"Your mark is {x:^50,.2f}")

x = 20343985.2324
print(f"Your mark is {x:*^50,.2f}")
