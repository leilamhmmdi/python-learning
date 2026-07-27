# Classes and Objects
# Class is a blueprint for creating objects.
# Object is an instance of a class.



# Simple class

class Car:
    pass


# Creating objects from class

pride = Car()
porch = Car()


print(pride)
print(porch)



# Adding attributes to object

class Student:
    pass


student1 = Student()

student1.name = "Leila"
student1.age = 22


print(student1.name)
print(student1.age)



# Class attributes

class Car:

    color = "white"
    quality = "normal"


car1 = Car()

print(car1.color)
print(car1.quality)



# Method inside class
# Function inside a class is called a method


class Car:

    color = "white"

    def move(self):
        print("Car is moving")


car1 = Car()

print(car1.color)

car1.move()



# self represents the current object

class Car:

    def move(self, speed, acceleration):

        self.speed = speed
        self.acceleration = acceleration



car1 = Car()

car1.move(120, 100)

print(car1.speed)
print(car1.acceleration)



# Constructor (__init__)
# __init__ runs automatically when object is created.


class Car:

    color = "white"

    def __init__(self, size, weight):

        self.size = size
        self.weight = weight


    def move(self, speed):

        self.speed = speed



car1 = Car(2.6, 3)

car1.move(120)


print(car1.size)
print(car1.weight)
print(car1.speed)



# Exercise:
# Create a Student class that stores name and age.


class Student:

    def info(self, name, age):

        self.name = name
        self.age = age



student1 = Student()

student1.info("Leila", 22)


print(student1.name)
print(student1.age)
