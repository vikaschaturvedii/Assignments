import sys
import webbrowser


def display_menu():
    print("Welcome to My Project!")
    print("1. Function 1")
    print("2. Function 2")
    print("3. Function 3")
    print("4. Function 4")
    print("5. Function 5")
    print("0. Exit")


def function1():
    print("Executing Function 1")
    try:
        # Perform file handling operations or any other desired functionality
        file_name = input("Enter file name: ")
        with open(file_name, "r") as file:
            content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


def function2():
    print("Executing Function 2")
    try:
        # Perform file handling operations or any other desired functionality
        file_name = input("Enter file name: ")
        with open(file_name, "a") as file:
            content = input("Enter content to append: ")
            file.write(content)
            print("Content appended successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


def function3():
    print("Executing Function 3")
    try:
        # Perform file handling operations or any other desired functionality
        file_name = input("Enter file name: ")
        with open(file_name, "w") as file:
            content = input("Enter content to write: ")
            file.write(content)
            print("Content written successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


def function4():
    print("Executing Function 4")
    try:
        # Perform desired functionality
        site = input("Enter site URL: ")
        print(f"Navigating to site: {site}")
        webbrowser.open(site)
    except Exception as e:
        print("An error occurred:", str(e))


def function5():
    print("Executing Function 5")
    try:
        # Perform desired functionality
        username = input("Enter username: ")
        password = input("Enter password: ")
        # Implement login functionality or any other desired functionality
        if username == "admin" and password == "password":
            print("Login successful.")
        else:
            print("Invalid credentials.")
    except Exception as e:
        print("An error occurred:", str(e))


def main_menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            function1()
        elif choice == "2":
            function2()
        elif choice == "3":
            function3()
        elif choice == "4":
            function4()
        elif choice == "5":
            function5()
        elif choice == "0":
            sys.exit("Exiting the program.")
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
