# Magic Methods
# Magic methods are special methods in Python.
# They start and end with double underscores (__).
#
# Examples:
# __init__
# __str__
# __len__
# __add__
# __eq__



# __str__
# It controls what is printed when we use print(object)


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age



    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}"



student = Student("Leila", 22)


print(student)



# __len__
# It defines the behavior of len(object)


class Team:

    def __init__(self, members):

        self.members = members



    def __len__(self):

        return len(self.members)



team = Team(["Ali", "Sara", "Reza"])


print(len(team))



# __add__
# It changes the behavior of + operator


class Number:

    def __init__(self, value):

        self.value = value



    def __add__(self, other):

        return self.value + other.value



num1 = Number(10)

num2 = Number(20)


print(num1 + num2)



# __eq__
# It controls comparison using ==


class Person:

    def __init__(self, name):

        self.name = name



    def __eq__(self, other):

        return self.name == other.name



person1 = Person("Leila")

person2 = Person("Leila")


print(person1 == person2)



# __lt__
# It controls less than operator (<)


class Product:

    def __init__(self, price):

        self.price = price



    def __lt__(self, other):

        return self.price < other.price



product1 = Product(100)

product2 = Product(200)


print(product1 < product2)



# __getitem__
# Allows object indexing like a list


class MyList:

    def __init__(self, items):

        self.items = items



    def __getitem__(self, index):

        return self.items[index]



my_list = MyList([10, 20, 30])


print(my_list[0])



# Exercise:
# Create a Book class
# Use __str__ to display book information
# Use __eq__ to compare two books


class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author



    def __str__(self):

        return f"{self.title} by {self.author}"



    def __eq__(self, other):

        return (
            self.title == other.title
            and self.author == other.author
        )



book1 = Book("Python", "Leila")

book2 = Book("Python", "Leila")


print(book1)

print(book1 == book2)
