# This a dice roller simulator inside the shell
import random

def print_dice_face(number):
    if number == 1:
        print(" ------- ")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print(" ------- ")
    elif number == 2:
        print(" ------- ")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print(" ------- ")
    elif number == 3:
        print(" ------- ")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print(" ------- ")
    elif number == 4:
        print(" ------- ")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print(" ------- ")
    elif number == 5:
        print(" ------- ")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print(" ------- ")
    elif number == 6:
        print(" ------- ")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print(" ------- ")
    else:
        print("Invalid dice face number")
# Choice
exit = 0
while exit == 0:
    print("1 to Roll\n2 to stop")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        number = random.randint(1,6)
        print_dice_face(number)
    elif choice == 2:
        exit = 1
    else:
        print(f"Invalid choice\n")