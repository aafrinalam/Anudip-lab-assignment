#################################################################################################################################

# 1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

def checkEvenOdd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter an number :-\n "))
checkEvenOdd(num)

# Output :- 
# Enter an number :-
# 42          
# Even


#################################################################################################################################

# 2.      Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

def checkAge(age):
    if age >= 18:
        return "You are eligible for voting."
    else:
        return "You are not eligible for voting."

age = int(input("Enter your age :- "))
result = checkAge(age)
print(result)

# Output :- 
# Enter your age :- 12
# You are not eligible for voting


#################################################################################################################################

# 3.      Write a Python program that determines if a given year is a leap year or not.

def checkLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = int(input("Enter a number :- "))

if checkLeapYear(year):
    print(f"{year} is a leap year.")

else:
    print(f"{year} is not a leap year.")

# Output :- 
# Enter a number :- 2010
# 2010 is not a leap year.


#################################################################################################################################

# 4.      Create a Python program that checks if a user-given number is positive, negative, or zero.

def checkNumber(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."


number = float(input("Enter a number: "))
result = checkNumber(number)
print(result)

# Output :- 
# Enter a number: -67
# The number is negative.


#################################################################################################################################

# 5.      Write a Python program that determines the largest of three numbers entered by the user.

def findLargest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

largest = findLargest(n1, n2, n3)
print(f"The largest number is:- {largest}")

# Output :- 
# Enter the first number: 25
# Enter the second number: 56
# Enter the third number: 85
# The largest number is:- 85.0