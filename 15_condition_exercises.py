# Even or Odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Larger Number
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("The larger number is:", x)
else:
    print("The larger number is:", y)



# Smallest Number
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x <= y and x <= z:
    print("The smallest number is:", x)
elif y <= x and y <= z:
    print("The smallest number is:", y)
else:
    print("The smallest number is:", z)



# Temperature Checker
temperature = int(input("Enter the temperature: "))

if temperature < 0:
    print("Freezing")
elif 0 <= temperature < 25:
    print("Moderate")
else:
    print("Hot")



# Positive / Negative Even-Odd
number = int(input("Enter a number: "))

if number == 0:
    print("The number is zero")

elif number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

else:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")



# Triangle Check
x = int(input("Enter first angle: "))
y = int(input("Enter second angle: "))
z = int(input("Enter third angle: "))

if x + y + z == 180:
    print("This is a triangle")
else:
    print("This is not a triangle")



# Discount Calculator
price = int(input("Enter the product price: "))

if price >= 1_000_000:
    final_price = price - (price * 0.15)

elif 500_000 <= price < 1_000_000:
    final_price = price - (price * 0.10)

else:
    final_price = price

print("Final price:", final_price)



# Leap Year (Persian Calendar)
year = int(input("Enter a year: "))

remainder = year % 33

if remainder in [1, 5, 9, 13, 17, 22, 26, 30]:
    print("Leap Year")
else:
    print("Not a Leap Year")
