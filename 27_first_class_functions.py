# First-Class Functions
# Nested Functions

def outer(number):
    print(number)

    def inner(value):
        print(value ** 2)

    inner(number)

outer(5)


# Passing Functions as Arguments

numbers = [45, 2, 25, 89, 13]


def ascending(my_list):
    print(sorted(my_list))


def descending(my_list):
    print(sorted(my_list, reverse=True))


def my_sort(func1, func2, my_list):
    func1(my_list)
    func2(my_list)


my_sort(descending, ascending, numbers)


# Returning Functions

numbers = [45, 2, 25, 89, 13]


def my_sort(order):

    def ascending(my_list):
        print(sorted(my_list))

    def descending(my_list):
        print(sorted(my_list, reverse=True))

    def error(my_list):
        print("Invalid option")

    if order == "a":
        return ascending
    elif order == "d":
        return descending
    else:
        return error


choice = input("Enter 'a' for ascending or 'd' for descending: ")

selected_function = my_sort(choice)
selected_function(numbers)
