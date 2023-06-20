# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    return num1 / num2

# Function to perform modulus
def modulus(num1, num2):
    return num1 % num2

# Function to perform exponentiation
def exponentiate(num1, num2):
    return num1 ** num2

# Function to perform floor division
def floor_divide(num1, num2):
    return num1 // num2

# Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing calculations using different operators
addition = add(num1, num2)
subtraction = subtract(num1, num2)
multiplication = multiply(num1, num2)
division = divide(num1, num2)
modulus_result = modulus(num1, num2)
exponentiation = exponentiate(num1, num2)
floor_division = floor_divide(num1, num2)

# Displaying the results
print("Results:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus_result)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)
