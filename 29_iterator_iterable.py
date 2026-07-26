# Iterator and Iterable
# Checking Iterable and Iterator

numbers = [1, 2, 3, 4, 5]

print("__iter__" in dir(numbers))
print("__next__" in dir(numbers))


iterator = iter(numbers)

print("__next__" in dir(iterator))


# Using next()

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Iterating with while

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# itertools.count()

from itertools import count

counter = count(100, step=-1)

print(next(counter))
print(next(counter))
print(next(counter))
