# operations.py

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
