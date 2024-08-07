########################################################################################################################

# 1.      Function without Parameters:

def without_parameter():
    print("Hi Aafrin")

without_parameter()

# Output :- Hi Aafrin

########################################################################################################################

# 2.      Function with Parameter:

def with_Parameter(name):
    print(f"Hii, {name}!")

with_Parameter("Aafrin")

# Output :- Hii Aafrin

########################################################################################################################

# 3.      Function with Default Parameter:

def with_default_parameter(name="Aafrin"):
    print(f"Hello, {name}")

with_default_parameter()        
with_default_parameter("World") 

# Output :- Hello Aafrin
# Output :- Hello World

########################################################################################################################

# 4.      Function with Return Keyword:

def add(a, b):
    return a + b
output = add(10, 20)

print(output)  

# Output :- 30

########################################################################################################################

# 5.      Recursion:

#           a) WAP to print factorial value of a given number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

output = factorial(6)
print(f"Factorial of {6} is {output}")

# Output :- Factorial of 6 is 720

########################################################################################################################

#           b) WAP to display Fibonacci series up to 10 iteration using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci_series = [fibonacci(i) for i in range(10)]
print(f"Fibonacci series up to {10} iterations: {fibonacci_series}")

# Output :- Fibonacci series up to 10 iterations: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
