# This is a simple, command prompt calculator that does baisc 4 operatrions

# functions
def add(a, b):
    return (a + b)
def sub(a, b):
    return (a - b)
def mul(a, b):
    return (a * b)
def div(a, b):
    while (b == 0):
        b = float(input("Enter a non zero denominator : "))
    return (a / b)

# Taking the first number from the user
number_1 = input("Enter 1st number : ")
number_1_works = 0
while (number_1_works != 1):
    try:
        number_1 = float(number_1)
        number_1_works = 1
    except ValueError:
        number_1 = input(f"Enter 1st number : ")

# Taking the Second numeber from the user
number_2 = input("Enter 2nd number : ")
number_2_works = 0
while (number_2_works != 1):
    try:
        number_2 = float(number_2)
        number_2_works = 1
    except ValueError:
        number_2 = input(f"Enter 2nd number : ")


# Taking User input for the operation
print(f"Enter 1 to do Addition : \nEnter 2 to do Subtraction : \nEnter 3 to do Multipication : \nEnter 4 to do division : ")
operation = input("Enter your choice : ")
operation_works = 0
while(operation_works != 1):
    if operation in ["1", "2", "3", "4"]:
        operation_works = 1
    else:
        operation = input("Enter a valid choice : ")


# Doing the operation selected by the user and displaying the output
if (operation == "1"):
    print(f"{add(number_1, number_2)}")
elif (operation == "2"):
    print(f"{sub(number_1, number_2)}")
elif (operation == "3"):
    print(f"{mul(number_1, number_2)}")
elif (operation == "4"):
    print(f"{div(number_1, number_2)}")