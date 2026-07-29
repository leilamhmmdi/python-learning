# Basic try / except

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Catch multiple exceptions

try:
    numbers = [10, 20, 30]
    index = int(input("\nEnter list index: "))
    print(numbers[index])

except (ValueError, IndexError):
    print("Invalid input or index out of range.")



# Using else
# else runs only if no exception occurs

try:
    age = int(input("\nEnter your age: "))

except ValueError:
    print("Age must be a number.")

else:
    print("Age accepted:", age)



# Using finally
# finally always executes

try:
    file = open("example.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")


# Raise an exception manually
age = int(input("\nEnter your age again: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Valid age.")


# Custom Exception
class PasswordTooShortError(Exception):
    """Custom exception for short passwords."""
    pass


def check_password(password):
    if len(password) < 8:
        raise PasswordTooShortError(
            "Password must contain at least 8 characters."
        )

    print("Password accepted.")


try:
    password = input("\nEnter password: ")
    check_password(password)

except PasswordTooShortError as error:
    print(error)



# Generic Exception (not recommended unless necessary)

try:
    x = int(input("\nEnter first number: "))
    y = int(input("Enter second number: "))
    print(x / y)

except Exception as error:
    print("An unexpected error occurred:")
    print(error)
