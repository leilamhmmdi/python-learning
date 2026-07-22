# Exercise 1: Diamond Pattern

rows = int(input("Enter the number of rows: "))

i = 1

while i <= rows:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i += 1

i = rows - 1

while i >= 1:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i -= 1



# Exercise 2: Alternate Uppercase Pattern

names = ["leila", "jake", "hakan", "elhan"]

i = 0

while i < len(names):

    word = names[i]
    j = 0

    while j < len(word):

        if i % 2 == 0:
            if j % 2 == 0:
                print(word[j].upper(), end="")
            else:
                print(word[j].lower(), end="")
        else:
            if j % 2 == 0:
                print(word[j].lower(), end="")
            else:
                print(word[j].upper(), end="")

        j += 1

    print()
    i += 1



# Exercise 3: Fibonacci Sequence
terms = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 0

while i < terms:
    print(a)
    a, b = b, a + b
    i += 1


