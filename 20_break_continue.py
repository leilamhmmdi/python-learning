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



# ASCII Code Examples
Print character from ASCII code
print(chr(78))

# Unicode Examples
print("\uFEED")
print("\U0001F60D")


# Convert characters to ASCII codes
letters = ["L", "e", "i", "l", "a"]

for letter in letters:
    print(ord(letter))


# Convert ASCII codes to characters
ascii_codes = [67, 92, 102, 100, 87, 72, 110]

for code in ascii_codes:
    print(chr(code))


# Break Example
Stop the loop when character 'd' is found

ascii_codes = [67, 92, 102, 100, 87, 72, 110]

for code in ascii_codes:
    if chr(code) == "d":
        break

    print(chr(code))


# Continue Example
# Skip numbers divisible by 3

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 3 == 0:
        continue

    print(number)


# Nested Loops

first_list = [10, 5, 23, 1, 90, 43, 57, 78, 21]
second_list = [6, 10, 57, 21, 2, 66, 1234, 5]

for x in first_list:
    for y in second_list:
        if x == y:
            print(x)


# Optimized Version
first_list = [10, 5, 23, 1, 90, 43, 57, 78, 21]
second_list = [6, 10, 57, 21, 2, 66, 1234, 5, 10]

for item in first_list:
    if item in second_list:
        print(item)


# Infinite Loop with Break

while True:
    character = input("Enter a character (q to quit): ")

    if character.lower() == "q":
        print("Program terminated.")
        break
