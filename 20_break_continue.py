# ASCII code
print(chr(78))

letters = ["L", "e", "i", "l", "a"]

for letter in letters:
    print(ord(letter))


codes = [67, 92, 102, 100, 87, 72, 110]

for code in codes:
    print(chr(code))


# Break example
for code in codes:

    if chr(code) == "d":
        break

    print(chr(code))


# Continue example
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:

    if number % 3 == 0:
        continue

    print(number)


# Nested loop
x = [10,5,23,1,90,43,57,78,21]
y = [6,10,57,21,2,66,1234,5]

for i in x:
    for j in y:
        if i == j:
            print(i)


# Optimized version
for item in x:
    if item in y:
        print(item)


# Infinite loop
while True:

    value = input("Enter a character: ")

    if value == "q":
        break

