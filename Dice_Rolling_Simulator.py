import random

number = random.randint(1,6)
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
print_dice_face(number)