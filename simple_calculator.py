'''
    A simple calculator
    Xiao Lang
'''

# This is a function to add two numbers
def add_number(x, y):
    return x + y

# This is a function to subtract two numbers
def subtract_number(x, y):
    return x - y

# This is a function to multiplies two numbers
def multiply(x, y):
    return x * y

# This is a function to divides two numbers
def divide(x ,y):
    return x / y

print("-----------------------------")
print("Select following options: ")
print("\t 1. Addition")
print("\t 2. Subtraction")
print("\t 3. Multiplication")
print("\t 4. Division")
print("\t ")
print("\t 0. exit")
print("-----------------------------")

start_calculation = True

while start_calculation:
    try:
        user_choice = int(input("Please enter your selection: "))
        if user_choice == 1:
            input_number1 = int(input("Please enter the first number: "))
            input_number2 = int(input("Please enter the second number"))
            print("{} + {} = {}".format(input_number1, input_number2, add_number(input_number1, input_number2)))
        elif user_choice == 2:
            input_number1 = int(input("Please enter the first number: "))
            input_number2 = int(input("Please enter the second number"))
            print("{} - {} = {}".format(input_number1, input_number2, subtract_number(input_number1, input_number2)))
        elif user_choice == 3:
            input_number1 = int(input("Please enter the first number: "))
            input_number2 = int(input("Please enter the second number"))
            print("{} * {} = {}".format(input_number1, input_number2, multiply(input_number1, input_number2)))
        elif user_choice == 4:
            input_number1 = int(input("Please enter the first number: "))
            input_number2 = int(input("Please enter the second number"))
            print("{} / {} = {}".format(input_number1, input_number2, divide(input_number1, input_number2)))
        elif user_choice == 0:
            start_calculation = False
            print("Stop Calculation")
        else:
            print("Please re-enter a correct number")
    except ValueError:
        print("Please enter an integer")

print("hahahah")