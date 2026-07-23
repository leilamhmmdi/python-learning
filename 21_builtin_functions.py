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
  
