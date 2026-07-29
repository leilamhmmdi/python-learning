# Read a file

with open("test1.txt", "r") as file:
    data = file.read()
    print(data)


# Read a file line by line

with open("test1.txt", "r") as file:
    for line in file:
        print(line.strip())


# Write to a file

with open("test1.txt", "w") as file:
    file.write("Hello World")



# Append to a file


with open("test1.txt", "a") as file:
    file.write("\nPython Learning")



# Write multiple lines

names = ["Leila", "Sevin", "Negin"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")



# Read the new file

with open("names.txt", "r") as file:
    print(file.read())
