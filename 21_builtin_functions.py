# zip()
names = ["sevin", "leila", "hakan", "elhan"]
ages = [17,22,27,31]

for name, age in zip(names, ages):
    print(f"{name} : {age}")


# reversed()
for item in reversed(names):
    print(item)


# sorted()
for item in sorted(names):
    print(item)


for item in sorted(names, reverse=True):
    print(item)


# Sort by length
for item in sorted(names, key=len):
    print(item)


# Reverse range
for i in reversed(range(10)):
    print(i)
  


# Combines multiple iterables together

names = ["Sevin", "Leila", "Hakan", "Elhan"]
ages = [17, 22, 27, 31]

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")


# reversed()
# Iterates over a sequence in reverse order

names = ["Sevin", "Leila", "Hakan", "Elhan"]

for name in reversed(names):
    print(name)


# sorted()
# Sorts elements in ascending order

names = ["Sevin", "Leila", "Hakan", "Elhan"]

for name in sorted(names):
    print(name)


# Sort in descending order

names = ["Sevin", "Leila", "Hakan", "Elhan"]

for name in sorted(names, reverse=True):
    print(name)


# Reverse a sorted list

names = ["Sevin", "Leila", "Hakan", "Elhan"]

for name in reversed(sorted(names)):
    print(name)


# Sort by string length

names = ["Sevin", "Leila", "Hakan", "Eli"]

for name in sorted(names, key=len):
    print(name)


# Reverse a range

for number in reversed(range(10)):
    print(number)


# len()
# Count the number of characters

text = input("Enter a text: ")
print(len(text))


# sum()
# Calculate the sum of numbers

total = sum(range(1, 101))
print(total)


# any()
# Returns True if at least one value is True

values = [False, False, True]
print(any(values))


# all()
# Returns True if all values are True

values = [True, True, True]
print(all(values))


# enumerate()
# Returns index and value together

fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
