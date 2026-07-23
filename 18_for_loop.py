# Basic for loop
for i in range(10):
    print(i)


# Print even two-digit numbers
for i in range(10, 100, 2):
    print(i)


# Print divisors of a number
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# Print list items
names = ["leila", "jake", "hakan", "elhan"]

for name in names:
    print(name)


# Nested for loop (multiplication table)
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


# Fibonacci sequence
count = int(input("Enter number of terms: "))

a = 0
b = 1

for _ in range(count):
    print(a)
    a, b = b, a + b

# ==================================================
# FOR LOOP EXERCISES
# ==================================================

# Convert English digits to Persian digits
digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹"
}

number = input("Enter a number: ")

result = ""

for digit in number:
    result += digits[digit]

print(result)


# Convert and separate every three digits
digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹"
}

number = input("Enter a number: ")

parts = []

while number:
    parts.insert(0, number[-3:])
    number = number[:-3]

result = ""

for part in parts:
    for digit in part:
        result += digits[digit]
    result += ","

print(result[:-1])


# Check perfect number
number = int(input("Enter a number: "))

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print("Perfect number")
else:
    print("Not a perfect number")


# Print perfect numbers from 1 to 10000
for number in range(1, 10001):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(number)
