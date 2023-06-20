# Arithmetic operators
num1 = 10
num2 = 3

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)
print()

# Assignment operators
x = 5
x += 3
print("Assignment Operator (+=):", x)
x -= 2
print("Assignment Operator (-=):", x)
x *= 4
print("Assignment Operator (*=):", x)
x /= 2
print("Assignment Operator (/=):", x)
x %= 3
print("Assignment Operator (%=):", x)
x //= 2
print("Assignment Operator (//=):", x)
x **= 3
print("Assignment Operator (**=):", x)
print()

# Comparison operators
a = 5
b = 7
print("Comparison Operators:")
print("Equal to (==):", a == b)
print("Not equal to (!=):", a != b)
print("Greater than (>):", a > b)
print("Less than (<):", a < b)
print("Greater than or equal to (>=):", a >= b)
print("Less than or equal to (<=):", a <= b)
print()

# Logical operators
p = True
q = False
print("Logical Operators:")
print("Logical AND (and):", p and q)
print("Logical OR (or):", p or q)
print("Logical NOT (not):", not p)
print()

# Identity operators
x = 10
y = 10
z = 5
print("Identity Operators:")
print("Is (x is y):", x is y)
print("Is not (x is not z):", x is not z)
print()

# Membership operators
numbers = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("In (2 in numbers):", 2 in numbers)
print("Not in (6 not in numbers):", 6 not in numbers)
print()

# Bitwise operators
a = 10  # 1010 in binary
b = 6   # 0110 in binary
print("Bitwise Operators:")
print("Bitwise AND (&):", a & b)   # 0010 -> 2
print("Bitwise OR (|):", a | b)    # 1110 -> 14
print("Bitwise XOR (^):", a ^ b)   # 1100 -> 12
print("Bitwise NOT (~):", ~a)      # 0101 -> -11 (2's complement)
print("Bitwise Left Shift (<<):", a << 2)   # 101000 -> 40
print("Bitwise Right Shift (>>):", a >> 2)  # 0010 -> 2
