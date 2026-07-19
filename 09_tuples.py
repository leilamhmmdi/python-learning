# Creating Tuples
t = (1,)
print(type(t))

t = (1, 2.5, "hello", [1, 5, 8], (1, 8, 0))
print(t)

# Tuple Immutability
t = (1, 2.5, "hello", [1, 5, 8], (1, 8, 0))
t[3][1] = 0
print(t)

# Tuple Packing
t = 1, 2, 3, 4
print(t)

# Single Element Tuple
t = 1,
print(type(t))

# Converting Iterable to List
x = "hello"
print(list(x))
