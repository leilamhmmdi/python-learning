# Class Exercises
# Practice creating classes, objects, attributes and methods.



# Exercise 1:
# Create a Person class
# Store name and age
# Print person's information


class Person:

    def info(self, name, age):

        self.name = name
        self.age = age


person1 = Person()

person1.info("Leila", 22)

print(person1.name)
print(person1.age)



# Exercise 2:
# Create a Rectangle class
# Calculate area and perimeter


class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height


    def area(self):

        return self.width * self.height


    def perimeter(self):

        return 2 * (self.width + self.height)



rectangle1 = Rectangle(5, 3)

print("Area:", rectangle1.area())

print("Perimeter:", rectangle1.perimeter())



# Exercise 3:
# Create a BankAccount class
# Deposit and withdraw money


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance


    def deposit(self, amount):

        self.balance += amount


    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

        else:

            print("Not enough money")



account = BankAccount("Leila", 1000)


account.deposit(500)

print(account.balance)


account.withdraw(300)

print(account.balance)



# Exercise 4:
# Create a Car class
# Store brand and speed
# Add a method to increase speed


class Car:

    def __init__(self, brand):

        self.brand = brand
        self.speed = 0


    def accelerate(self, amount):

        self.speed += amount



car = Car("BMW")


car.accelerate(50)

print(car.brand)

print(car.speed)
