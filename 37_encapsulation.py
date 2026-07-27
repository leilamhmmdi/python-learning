# Encapsulation
# Encapsulation means hiding internal data
# and controlling access to it.
#
# In Python:
# _variable  -> protected (by convention)
# __variable -> private (name mangling)



# Public attribute example


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age



student = Student("Leila", 22)


print(student.name)
print(student.age)



# Protected attribute
# It can still be accessed, but it means:
# "Do not use directly outside the class"


class Person:

    def __init__(self, name):

        self._name = name



person = Person("Ali")

print(person._name)



# Private attribute
# Double underscore makes attribute private


class BankAccount:

    def __init__(self, balance):

        self.__balance = balance



    def show_balance(self):

        print("Balance:", self.__balance)



account = BankAccount(1000)


account.show_balance()



# Direct access will cause error
# print(account.__balance)



# Getter and Setter
# Getter reads private data
# Setter changes private data


class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.__balance = balance



    # Getter

    def get_balance(self):

        return self.__balance



    # Setter

    def set_balance(self, amount):

        if amount >= 0:

            self.__balance = amount

        else:

            print("Invalid balance")



account = Account("Leila", 500)


print(account.get_balance())


account.set_balance(1000)

print(account.get_balance())



# Using property decorator
# Cleaner way to create getter and setter


class Product:

    def __init__(self, price):

        self.__price = price



    @property
    def price(self):

        return self.__price



    @price.setter
    def price(self, value):

        if value > 0:

            self.__price = value

        else:

            print("Price must be positive")



product = Product(200)


print(product.price)


product.price = 300

print(product.price)



# Exercise:
# Create a User class
# Store username and password privately
# Create methods to change and show password


class User:

    def __init__(self, username, password):

        self.username = username
        self.__password = password



    def show_password(self):

        print(self.__password)



    def change_password(self, new_password):

        if len(new_password) >= 8:

            self.__password = new_password

        else:

            print("Password is too short")



user = User("Leila", "12345678")


user.show_password()


user.change_password("Python123")


user.show_password()
