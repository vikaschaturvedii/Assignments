# Take input from the user
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Calculate the sum of all elements
sum_of_elements = sum(numbers)

# Find the smallest and largest numbers
smallest_number = min(numbers)
largest_number = max(numbers)

# Display the list in ascending and descending order
ascending_order = sorted(numbers)
descending_order = sorted(numbers, reverse=True)

# Convert the list into a tuple
numbers_tuple = tuple(numbers)

# Delete the list
del numbers

# Perform the operations
print("Sum of all elements:", sum_of_elements)
print("Smallest number:", smallest_number)
print("Largest number:", largest_number)
print("List in ascending order:", ascending_order)
print("List in descending order:", descending_order)
print("List converted to a tuple:", numbers_tuple)
