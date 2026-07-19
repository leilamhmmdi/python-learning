# Creating a List
x = [1, 2, 4, "hello", 4.67, 3 + 5j]
print(x)

# List Slicing
x = [1, 2, 4, "hello", 4.67, 3 + 5j]
print(x[::2])

# Updating List Elements
x = [1, 2, 4, "hello"]
x[0] = "hi"
print(x)

# Nested Lists
x = [1, 2, 4, "hello", 4.67, 3 + 5j, [8, 9, 0]]
print(x[6][1])

# List Concatenation
x = [1, 2, 3]
print([5, 6, 7] + x)

# List Repetition
x = [1, 2, 3]
print(x * 3)

# Comparing Lists
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# List Assignment
x = [1, 2, 3]
y = x

y[0] = 25

print(x)
print(y)

# Replace String in a List
x = [1, 2, 3, "salam"]

x[3] = x[3].replace("salam", "selam")

print(x)

# List Copy
x = [1, 2, 3]
y = x.copy()

print(x)
print(y)

# Shallow Copy

import copy

x = [1, 2, 3]
y = copy.copy(x)

print(x)
print(y)

# Deep Copy

import copy

x = [1, 2, 3]
y = copy.deepcopy(x)

print(x)
print(y)

# append()
x = [1, 2, 3]

x.append(56)

print(x)

# insert()
x = [1, 2, 3]

x.insert(1, 4)

print(x)
