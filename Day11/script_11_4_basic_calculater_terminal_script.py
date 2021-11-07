'''
A simple calculator that has the following functionalities:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit

and does so, in the form of an infinite loop with a menu and an option to exit the program.
'''

def perform_addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print()
    print("The sum of the two numbers is: ", num1 + num2)
    print()

def perform_subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print()
    print("The difference of the two numbers is: ", num1 - num2)
    print()

def perform_multiplication():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print()
    print("The product of the two numbers is: ", num1 * num2)
    print()

def perform_division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print()
    print("The quotient of the two numbers is: ", num1 // num2)
    print("The remainder of the two numbers is: ", num1 % num2)
    print()

def calculator():
    
    while True:
        print("""
        Press 1 for Addition
        Press 2 for Subtraction
        Press 3 for Multiplication
        Press 4 for Division
        Press 5 to Quit
        """)
        choice = int(input("Enter your choice: "))
        print()

        if (choice == 1):
            perform_addition()
        elif (choice == 2):
            perform_subtraction()
        elif (choice == 3):
            perform_multiplication()
        elif (choice == 4):
            perform_division()
        elif (choice == 5):
            print("Thank you for using the calculator!")
            print()
            break
        else:
            print("Invalid choice!")
            print()    

calculator()