from random import random
from random import uniform
from random import randint
from random import randrange
from random import choice
from random import sample
import random


print(random())

print(uniform(0,100))

print(randint(0,100))

print(randrange(5,100,2))


names = ["sevin","leila","hakan","eli"]

print(choice(names))

print(sample(names,2))


# Shuffle
numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)

random.shuffle(numbers)

print(numbers)


# Dice probability
total = 10000

counts = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

for _ in range(total):

    result = randint(1,6)

    counts[result] += 1


for face, count in counts.items():
    probability = count / total
    print(face, probability)



# Import random functions
random()
Returns a random float between 0 and 1

for _ in range(5):
    print(random())


# uniform()
# Returns a random float within a given range

for _ in range(5):
    print(uniform(0, 100))


# randint()
# Returns a random integer within a given range

for _ in range(5):
    print(randint(0, 100))


# randrange()
# Returns a random number with a custom step

for _ in range(5):
    print(randrange(5, 100, 2))


# choice()
# Selects one random element from a list

names = ["Sevin", "Leila", "Hakan", "Eli"]

print(choice(names))


# sample()
# Selects multiple unique random elements

names = ["Sevin", "Leila", "Hakan", "Eli"]

print(sample(names, 2))


# shuffle()
# Shuffles a list in place

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Before:", numbers)

random.shuffle(numbers)

print("After :", numbers)


# Dice Simulation
# Roll a die 10,000 times

total_rolls = 10000

counts = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

for _ in range(total_rolls):
    result = randint(1, 6)
    counts[result] += 1

print("Dice Roll Results")
print("-" * 30)

for number, count in counts.items():
    probability = count / total_rolls
    print(
        f"{number}: {count} times | Probability = {probability:.4f}"
    )
