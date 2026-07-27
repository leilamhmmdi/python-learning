# Inheritance
# Inheritance allows a class to use properties and methods
# from another class.
#
# Parent class = base class
# Child class = derived class



# Simple inheritance example


class Animal:

    def eat(self):

        print("Animal is eating")



class Dog(Animal):

    def bark(self):

        print("Dog is barking")



dog = Dog()

# Method inherited from Animal class

dog.eat()

# Method from Dog class

dog.bark()



# Adding constructor in parent and child class


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def show_info(self):

        print(self.name, self.age)



class Student(Person):

    def __init__(self, name, age, student_id):

        # Calling parent constructor

        super().__init__(name, age)

        self.student_id = student_id



student = Student("Leila", 22, 101)


student.show_info()

print(student.student_id)



# Method overriding
# Child class can change parent method behavior.


class Animal:

    def sound(self):

        print("Some sound")



class Cat(Animal):

    def sound(self):

        print("Meow")



class Dog(Animal):

    def sound(self):

        print("Woof")



cat = Cat()

dog = Dog()


cat.sound()

dog.sound()



# Multiple inheritance
# A class can inherit from more than one class.


class Camera:

    def take_photo(self):

        print("Taking photo")



class Phone:

    def call(self):

        print("Calling")



class Smartphone(Camera, Phone):

    pass



phone = Smartphone()


phone.take_photo()

phone.call()



# Exercise:
# Create a Vehicle parent class
# Create Car and Motorcycle child classes


class Vehicle:

    def __init__(self, brand):

        self.brand = brand


    def move(self):

        print("Vehicle is moving")



class Car(Vehicle):

    def move(self):

        print(self.brand, "car is driving")



class Motorcycle(Vehicle):

    def move(self):

        print(self.brand, "motorcycle is driving")



car = Car("BMW")

motorcycle = Motorcycle("Honda")


car.move()

motorcycle.move()
