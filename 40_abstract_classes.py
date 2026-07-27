# Abstract Classes
# Abstract class is a class that cannot create objects directly.
# It is used as a blueprint for other classes.
#
# We use:
# ABC -> Abstract Base Class
# abstractmethod -> create abstract methods



from abc import ABC, abstractmethod



# Abstract class example


class Animal(ABC):


    @abstractmethod
    def sound(self):

        pass



# Child classes must implement abstract methods


class Dog(Animal):


    def sound(self):

        print("Woof")



class Cat(Animal):


    def sound(self):

        print("Meow")



dog = Dog()

cat = Cat()


dog.sound()

cat.sound()



# We cannot create object from abstract class

# animal = Animal()
# This will give an error



# Example:
# Payment system


class Payment(ABC):


    @abstractmethod
    def pay(self, amount):

        pass




class CreditCard(Payment):


    def pay(self, amount):

        print(
            "Paid",
            amount,
            "with credit card"
        )



class PayPal(Payment):


    def pay(self, amount):

        print(
            "Paid",
            amount,
            "with PayPal"
        )



class Cash(Payment):


    def pay(self, amount):

        print(
            "Paid",
            amount,
            "with cash"
        )




payments = [

    CreditCard(),

    PayPal(),

    Cash()

]


for payment in payments:

    payment.pay(100)



# Exercise:
# Create an abstract Shape class
# Every shape must have area() method.


class Shape(ABC):


    @abstractmethod
    def area(self):

        pass




class Rectangle(Shape):


    def __init__(self, width, height):

        self.width = width
        self.height = height



    def area(self):

        return self.width * self.height




class Circle(Shape):


    def __init__(self, radius):

        self.radius = radius



    def area(self):

        return 3.14 * self.radius ** 2




shapes = [

    Rectangle(5, 4),

    Circle(3)

]


for shape in shapes:

    print(shape.area())
