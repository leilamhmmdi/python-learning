# Basic if-elif-else
x = 4
if x == 5:
    print("x is 5")
elif x == 4:
    print("x is 4")
elif x == 3:
    print("x is 3")
else:
    print("x is not 5")
    
# Grading System
mark = int(input("Enter a number:"))
if 15 <= mark <= 20:
    print("Excellent")
elif 10 <= mark < 15:
    print("Good")
elif 0 <= mark < 10:
    print("Need More Practice")
else:
    print("Wrong")

# Multiple if
mark = int(input("Enter a number:"))

if mark > 5:
    print("A")

if mark == 7:
    print("B")

if mark <= 10:
    print("C")

# if + elif
mark = int(input("Enter a number:"))

if mark > 5:
    print("A")

if mark == 7:
    print("B")
elif mark <= 10:
    print("C")

# Nested if
mark = int(input("Enter a number:"))

if mark >= 10:

    if 15 <= mark <= 20:
        print("Excellent")

    elif 10 <= mark < 15:
        print("Good")

    else:
        print("Wrong")

else:
    print("Rejected")
    
