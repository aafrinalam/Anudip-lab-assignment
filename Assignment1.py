#################################################################################################################################

# Q.1 print helloworld.................................................................................

print("Hello World")

# Output :- Hello World

#################################################################################################################################

# Q.2 describe local variable and global variable code........................................................................

# Definition :- Local variables are those defined within a function. They are scoped to the function in which they are defined, meaning they cannot be accessed outside of that function.

def localVariableFunction():
    message = "Aafrin"   # This is a local variable
    print(message)

localVariableFunction()

# Output :- Aafrin

# Definition :- Global variables are defined outside of any function or class. They can be accessed from any part of the program, including inside functions.

globalVariable = "Hello World"  

def globalVariableFunction():
    print(globalVariable)   # Accessing global variable inside the function

globalVariableFunction()    # Calling functions

# Output :- Hello World

#################################################################################################################################

# Q.3 Write a code that describe Indentation error

# definition :- An indentation error occurs when the spaces or tabs used for indentation do not conform to Python's syntax rules

# def print_numbers():
# for i in range(1, 6):    #Expected indented block
# print(i)                 #Expected indented block

# print_numbers()

# Error :- for i in range(1, 6):    #Expected indented block

# Solution :-
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()

# output :- 
1
2
3
4
5

#################################################################################################################################

# Q.4 write a code that describe local and global variable with same name

name = "global"

def print_name():
    name = "local"
    print("Inside the function:", name)

print_name()  

print("Outside the function:", name)

# Output :- 
# Inside the function: local
# Outside the function: global

#################################################################################################################################

# Q.5 Write a code for string, int and float input.

name = input("Enter your name: ")      # Taking string input 

age = int(input("Enter your age: "))       # Taking integer input 

weight = float(input("Enter your weight in kilo: "))       # Taking float input 

print("Name:", name)
print("Age:", age)
print("Weight:", weight, "kilo")

# Output :- 
# Enter your name: Aafrin
# Enter your age: 23
# Enter your height in kilo: 52

# Name: Aafrin
# Age: 23
# Weight: 52.0 kilo
