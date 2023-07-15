# operations.py
# main.py

import operations

import math

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        with open(self.file_name, 'r') as file:
            content = file.read()
        return content
    
    def write_file(self, content):
        with open(self.file_name, 'w') as file:
            file.write(content)
    
    def append_file(self, content):
        with open(self.file_name, 'a') as file:
            file.write(content)

class MathOperations:
    @staticmethod
    def square_root(number):
        return math.sqrt(number)
    
    @staticmethod
    def factorial(number):
        return math.factorial(number)

class StringOperations:
    @staticmethod
    def split_string(string, delimiter):
        return string.split(delimiter)

# File operations
file_op = operations.FileOperations("example.txt")
content = file_op.read_file()
print(content)

file_op.write_file("Hello, World!")
file_op.append_file(" This is an appended content.")
content = file_op.read_file()
print(content)

# Mathematical operations
math_op = operations.MathOperations()
sqrt_result = math_op.square_root(16)
print(sqrt_result)

factorial_result = math_op.factorial(5)
print(factorial_result)

# String operations
string_op = operations.StringOperations()
split_result = string_op.split_string("Hello,World,Python", ",")
print(split_result)

# User-defined exception
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(e)
