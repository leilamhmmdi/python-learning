# Polymorphism
# Polymorphism means "many forms".
# The same method name can have different behaviors
# in different classes.



# Example 1:
# Different classes have the same method name


class Dog:

    def sound(self):

        print("Woof")



class Cat:

    def sound(self):

        print("Meow")



class Bird:

    def sound(self):

        print("Tweet")



animals = [Dog(), Cat(), Bird()]


for animal in animals:

    animal.sound()



# Example 2:
# Same method name with different calculations


class Rectangle:

    def area(self):

        return 10 * 5



class Circle:

    def area(self):

        return 3.14 * 5 * 5



shapes = [Rectangle(), Circle()]


for shape in shapes:

    print(shape.area())



# Duck Typing
# Python focuses on what an object can do,
# not what type it is.


class Car:

    def move(self):

        print("Car is moving")



class Plane:

    def move(self):

        print("Plane is flying")



def start(vehicle):

    vehicle.move()



car = Car()

plane = Plane()


start(car)

start(plane)



# Method overriding with inheritance


class Animal:

    def make_sound(self):

        print("Animal sound")



class Dog(Animal):

    def make_sound(self):

        print("Bark")



class Cat(Animal):

    def make_sound(self):

        print("Meow")



animals = [

    Dog(),

    Cat(),

    Animal()

]


for animal in animals:

    animal.make_sound()



# Exercise:
# Create a Payment system
# Different payment methods should have
# different pay() behavior.



class Payment:

    def pay(self, amount):

        print("Paying", amount)



class CreditCard(Payment):

    def pay(self, amount):

        print("Paid", amount, "with credit card")



class Cash(Payment):

    def pay(self, amount):

        print("Paid", amount, "with cash")



class Crypto(Payment):

    def pay(self, amount):

        print("Paid", amount, "with crypto")



payments = [

    CreditCard(),

    Cash(),

    Crypto()

]


for payment in payments:

    payment.pay(100)
