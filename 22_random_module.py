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

