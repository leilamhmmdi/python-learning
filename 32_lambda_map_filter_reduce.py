# Lambda functions
# Lambda is a small anonymous function.
# It is useful when we need a simple function only once.


# Normal function
def power(x, y):
    return x ** y


print(power(2, 5))


# Same function using lambda
power_lambda = lambda x, y: x ** y

print(power_lambda(2, 5))



# Lambda with one argument

square = lambda x: x ** 2

print(square(4))



# map()
# map applies a function to every item in an iterable


def multiply(x):
    return x * 2


numbers = [1, 2, 3, 4]

result = map(multiply, numbers)

print(list(result))



# map() with lambda

numbers = [1, 2, 3, 4]

result = map(lambda x: x ** 2, numbers)

print(list(result))



# filter()
# filter keeps only values that return True


def check_number(x):
    if x > 5:
        return True
    else:
        return False


numbers = [1, 9, 7, 5, 2, 3, 4, 78]

result = filter(check_number, numbers)

print(list(result))



# filter() with lambda

numbers = [1, 9, 7, 5, 2, 3, 4, 78]

result = filter(lambda x: x > 5, numbers)

print(list(result))



# reduce()
# reduce combines all items and returns one final value

from functools import reduce


numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)



# reduce with strings

letters = ['l', 'e', 'i', 'l', 'a']

result = reduce(lambda x, y: x + y, letters)

print(result)



# sorted() with key function
# key decides how items should be sorted


numbers = [4, 1, 2, 3, 4, 8, 7, 1, 25, 9]


def sort_key(x):
    return x % 3


result = sorted(numbers, key=sort_key)

print(result)



# Same example using lambda

numbers = [4, 1, 2, 3, 4, 8, 7, 1, 25, 9]

result = sorted(numbers, key=lambda x: x % 3)

print(result)



# Exercise:
# Count how many times a digit appears in a number


def digit_count(number, digit):
    count = 0

    while number > 0:
        if number % 10 == digit:
            count += 1

        number //= 10

    return count



number = int(input("Enter number: "))
digit = int(input("Enter digit: "))

print(digit_count(number, digit))
