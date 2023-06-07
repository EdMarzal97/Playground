import math

print("lest solve some cuadratic formula like ax^2 + bx + c")

a = int(input("insert a: "))
b = int(input("insert b: "))
c = int(input("insert c: "))

print(
    "your equation is: ",
    a,
    "x^2 + ",
    b,
    "x + ",
    c,
)

positiveX = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
negativeX = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print("the value point of X in your equation is: ", positiveX, " and ", negativeX)
