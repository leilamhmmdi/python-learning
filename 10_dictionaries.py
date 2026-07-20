# Creating a Dictionary
d = {
    "varzesh": 10.25,
    "riazi": 6.5,
    "andishe1": 4,
    "andishe2": 9.75
}
print(d)

# Accessing Values
print(d["varzesh"])
print(d["riazi"])

# Dictionary Keys
print(d.keys())

d = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
print(d)

# Dictionary Values
print(d.values())

# Dictionary Items
print(d.items())


# Add a new key
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 56
print(d)

# Empty dictionary
d = {}
d['d'] = 56
print(d)

# Get key and value from user
key1 = input('Enter first key: ')
value1 = input('Enter first value: ')
key2 = input('Enter second key: ')
value2 = input('Enter second value: ')

d = {}
d[key1] = value1
d[key2] = value2

print(d)
