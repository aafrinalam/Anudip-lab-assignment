#################################################################################################################################

# Q.1 Write a program for arithmetic operators

def main():
    print("Arithmetic Operators")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))   

    print("\n Select an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}") # f-strings provide a way to embed expressions inside string literals, using curly braces {}
    elif choice == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice.")
 

if __name__ == "__main__":
    main()

# Output :- 
# Arithmetic Operators
# Enter the first number: 20
# Enter the second number: 20

#  Select an option:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter choice (1/2/3/4): 3

# Result: 20.0 * 20.0 = 400.0

#################################################################################################################################

# Q.2 Write a program for assignment operators

def main():
    print("Assignment Operators")
    
    a = float(input("Enter the value for a: "))
    b = float(input("Enter the value for b: "))

    print(f"\nInitial values: a = {a}, b = {b}")

    c = a
    print(f"\nAssignment Operator: c = a\nc = {c}")

    a += b
    print(f"Addition Assignment: a += b\nNow, a = {a}")

    a -= b
    print(f"Subtraction Assignment: a -= b\nNow, a = {a}")

    a *= b
    print(f"Multiplication Assignment: a *= b\nNow, a = {a}")

    if b != 0:
        a /= b
        print(f"Division Assignment: a /= b\nNow, a = {a}")
    else:
        print("zero is not allowed.")

    if b != 0:
        a %= b
        print(f"Modulus Assignment: a %= b\nNow, a = {a}")
    else:
        print("zero is not allowed.")

if __name__ == "__main__":
    main()

# Output :- 
# Initial values: a = 4.0, b = 2.0
# Assignment Operator: c = a
# c = 4.0
# Addition Assignment: a += b
# Now, a = 6.0
# Subtraction Assignment: a -= b
# Now, a = 4.0
# Multiplication Assignment: a *= b
# Now, a = 8.0
# Division Assignment: a /= b
# Now, a = 4.0
# Modulus Assignment: a %= b
# Now, a = 0.0

#################################################################################################################################

# Q.3 Write a program for Bitwise operators 

def bitwiseOperator(a, b):
    print(f"Numbers: a = {a}, b = {b}")

    andResult = a & b
    print(f"{a} & {b} = {andResult} ( AND operator)")

    orResult = a | b
    print(f"{a} | {b} = {orResult} ( OR operator)")

    xorResult = a ^ b
    print(f"{a} ^ {b} = {xorResult} ( XOR operator)")

    notResult_a = ~a
    notResult_b = ~b
    print(f"~{a} = {notResult_a} ( NOT of a operator)")
    print(f"~{b} = {notResult_b} ( NOT of b operator)")

num1 = 6  
num2 = 3  
bitwiseOperator(num1, num2)

# Output :- 
# Numbers: a = 6, b = 3
# 6 & 3 = 2 ( AND operator)
# 6 | 3 = 7 ( OR operator)
# 6 ^ 3 = 5 ( XOR operator)
# ~6 = -7 ( NOT of a operator)
# ~3 = -4 ( NOT of b operator)

#################################################################################################################################

# Q.4 Write a program to calculate the greatest of three numbers.

def findGreatestNumber(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = 80
num2 = 56
num3 = 92

greatest = findGreatestNumber(num1, num2, num3)
print(f"The greatest of the numbers {num1}, {num2}, and {num3} is {greatest}")


# Output :- The greatest of the numbers 80, 56, and 92 is 92

#################################################################################################################################

# 1.      Calculate the area of a circle.

import math      # math module is imported to use the value of π (math.pi)

def calculateCircleArea(radius):
    if radius <= 0:
        return "It must be positive number."
    return math.pi * (radius ** 2)

radius = float(input("Enter an number \n"))

area = calculateCircleArea(radius)
print(f"The area of the circle {radius} is {area:.2f}")


# Output :- The area of the circle with radius 2.0 is 12.57

#################################################################################################################################

# 2.      Calculate the area of a triangle.

def calculateTriangleArea(base, height):
    if base <= 0 or height <= 0:
        return "It must be positive number."
    return 0.5 * base * height

base = float(input("Enter an number for base \n"))
height = float(input("Enter an number for height \n"))

area = calculateTriangleArea(base, height)
print(f"The area of the triangle {base} and {height} is {area}")


# Output :- The area of the triangle 20.0 and 30.0 is 300.0

#################################################################################################################################

# 3.      Calculate the area of a rectangle.

def calculateRectangleArea(length, width):
    if length <= 0 or width <= 0:
        return "It must be positive numbers."
    return length * width

length = float(input("Enter an number for length \n"))
width = float(input("Enter an number for width \n"))

area = calculateRectangleArea(length, width)
print(f"The area of the rectangle {length} and {width} is {area}")

# Output :- 
# Enter an number for length 
# 5
# Enter an number for width
# 2
# The area of the rectangle 5.0 and 2.0 is 10.0

#################################################################################################################################

# 4.      Calculate the area of a square.

def calculateSquareArea(sideLength):
    if sideLength <= 0:
        return "It must be positive number."
    return sideLength ** 2  #** is the exponentiation operator in Python.

sideLength = float(input("Enter an number \n"))

area = calculateSquareArea(sideLength)
print(f"The area of the square  {sideLength} is {area}")


# Output :- 
#Enter an number 
# 8
# The area of the square 8.0 is 64.0
