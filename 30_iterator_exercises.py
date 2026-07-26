# Iterator Exercises

from itertools import count
import time
import os


# Countdown from 100 to 70 (1 second)

counter = count(100, step=-1)

while True:
    value = next(counter)
    print(value)
    time.sleep(1)

    os.system("cls" if os.name == "nt" else "clear")

    if value == 70:
        break


# Countdown from 69 to 40 (0.5 second)

counter = count(69, step=-1)

while True:
    value = next(counter)
    print(value)
    time.sleep(0.5)

    os.system("cls" if os.name == "nt" else "clear")

    if value == 40:
        break


# Countdown from 39 to 1 (0.25 second)

counter = count(39, step=-1)

while True:
    value = next(counter)
    print(value)
    time.sleep(0.25)

    os.system("cls" if os.name == "nt" else "clear")

    if value == 1:
        break

print("BOOM!")
