# Generator
# Generator is a function that uses yield instead of return.
# It returns values one by one and saves its state.


# Simple generator example
def func(name):
    yield name


g = func("Jim")

# next() gets the value until the next yield
print(next(g))


# Every next() runs the generator until it reaches yield
def hello_generator(name):
    yield name
    print("Hello " + name)
    yield


g = hello_generator("Jim")

print(next(g))
next(g)


# Store yield value inside a variable
def test_generator():
    yield "First value"
    yield "Second value"


g = test_generator()

value1 = next(g)
value2 = next(g)

print(value1)
print(value2)



# Generator range example
# Difference between return and yield:
# return creates the whole list in memory
# yield creates values one by one


def gen_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


gr = gen_range(1, 10, 2)

print(list(gr))



# Generator close()
# close() stops the generator

def numbers():
    yield 1
    yield 2
    yield 3


g = numbers()

print(next(g))

g.close()



# Coroutine
# Coroutine can receive values using send()
# yield works as input and output point


def my_gen():
    while True:
        name = yield
        print("My name is", name)


g = my_gen()

# Start generator
next(g)

# Send value into yield
g.send("Leila")

g.close()



# Exercise:
# Create a generator that replaces bad words with stars


bad_words = ["meymoon", "gav"]


def censor(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if word in bad_words:
            result.append("*" * len(word))
        else:
            result.append(word)

    return " ".join(result)


text = input("Enter your sentence: ")

print(censor(text))
