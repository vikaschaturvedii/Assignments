def write_student_data(roll_number, name, class_name, file="student_data.txt"):
    try:
        with open(file, "a") as f:
            f.writelines([f"Roll Number: {roll_number}\n", f"Name: {name}\n", f"Class: {class_name}\n"])
        
        with open(file, "r") as f:
            data = f.readlines()
            for line in data:
                print(line.rstrip())  # rstrip() removes the trailing newline character

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")

# Example usage
write_student_data(12345, "John Doe", "Class 10")
