def ds(roll_no, name):
    # Create data structures
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {'Roll No': roll_no, 'Name': name}

    # Print initial data structures
    print("Initial data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Modify values during runtime
    roll_no_new = input("Enter new Roll No: ")
    name_new = input("Enter new Name: ")

    # Modify list
    my_list[0] = roll_no_new
    my_list[1] = name_new

    # Modify tuple
    my_tuple = (roll_no_new, name_new)

    # Modify set
    my_set.remove(roll_no)
    my_set.add(roll_no_new)
    my_set.remove(name)
    my_set.add(name_new)

    # Modify dictionary
    my_dict['Roll No'] = roll_no_new
    my_dict['Name'] = name_new

    # Print modified data structures
    print("\nModified data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Delete data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    # Verify deletion
    print("\nData structures after deletion:")
    print("List:", my_list)  # Raises NameError
    print("Tuple:", my_tuple)  # Raises NameError
    print("Set:", my_set)  # Raises NameError
    print("Dictionary:", my_dict)  # Raises NameError


# Test the function
roll_no_input = input("Enter Roll No: ")
name_input = input("Enter Name: ")
ds(roll_no_input, name_input)
