# Even or odd
def even_or_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))

print(even_or_odd(number))


# Maximum of two numbers
def maximum(x, y):

    if x > y:
        return x

    return y


a = int(input("First number: "))
b = int(input("Second number: "))

print(maximum(a, b))


# Smallest of three numbers
def smallest(x, y, z):

    if x <= y and x <= z:
        return x

    if y <= x and y <= z:
        return y

    return z


a = int(input("Enter x: "))
b = int(input("Enter y: "))
c = int(input("Enter z: "))

print(smallest(a, b, c))




# Find the larger number

def maximum(x, y):
    if x > y:
        return x
    return y


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(maximum(x, y))



# Find the smallest number

def smallest(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    return z


x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

print(smallest(x, y, z))



# Calculate factorial

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter a number: "))

print(factorial(number))


# Print user information

def information(first_name, last_name, age):

    return (
        f"My name is {first_name} "
        f"{last_name} and I am {age} years old."
    )


first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

print(information(first_name, last_name, age))



# User registration

def registration():

    user = {}

    national_id = input("Enter national ID: ")
    phone = input("Enter phone number: ")

    while True:

        password = input("Enter password: ")

        if len(password) < 8:
            print("Password is too short.")
            continue

        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)

        if not has_upper:
            print("Password must contain an uppercase letter.")
            continue

        if not has_lower:
            print("Password must contain a lowercase letter.")
            continue

        break

    user["national_id"] = national_id
    user["phone"] = phone
    user["password"] = password

    print(user)


registration()
