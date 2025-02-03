import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("this is not an int")
    sys.exit(1)

try:
    quotient = x / y
    print(quotient)
except ZeroDivisionError:
    print("you can't divide by 0 fool")
    sys.exit(1)