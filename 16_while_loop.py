# Basic While Loop
i = 0

while i < 10:
    print(i)
    i += 1


# Print Even Two-Digit Numbers
i = 10

while i < 100:
    print(i)
    i += 2



# Print Even Numbers from User Input

i = int(input("Enter a number: "))

while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1



# Start from the First Two-Digit Even Number
i = int(input("Enter a number: "))

if i < 10:
    i = 10

if i % 2 != 0:
    i += 1

while i < 100:
    print(i)
    i += 2



# Divisors of 12
i = 1

while i <= 12:
    if 12 % i == 0:
        print(i, end=" ")
    i += 1

print()



# Divisors of Any Number
number = int(input("Enter a number: "))
i = 1

while i <= number:
    if number % i == 0:
        print(i, end=" ")
    i += 1

print()



# Factorial
number = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print("Factorial:", factorial)



# Float Increment
value = float(input("Enter a number: "))

while value < 100:
    print(value)
    value += 1.1



# Star Pattern
i = 1

while i <= 10:
    print("*" * i)
    i += 1

i -= 1

while i >= 1:
    print("*" * i)
    i -= 1



# Custom Star Pattern

rows = int(input("Enter the number of rows: "))

i = 1

while i <= rows:
    print("*" * i)
    i += 1

i -= 2

while i >= 1:
    print("*" * i)
    i -= 1



# Iterate Through a List

names = ["Leila", "Aisan", "Hakan", "Elhan"]

i = 0

while i < len(names):
    print(names[i])
    i += 1



# Multiplication Table

i = 1

while i <= 10:

    j = 1

    while j <= 10:
        print(i * j, end="\t")
        j += 1

    print()
    i += 1



# Nested While on Strings

names = ["leila", "jake", "hakan", "elhan"]

i = 0

while i < len(names):

    word = names[i]
    j = 0

    while j < len(word):

        if j % 2 == 0:
            print(word[j].upper(), end="")
        else:
            print(word[j].lower(), end="")

        j += 1

    print()
    i += 1
