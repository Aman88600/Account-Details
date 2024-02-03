# This is a cmd based app, that, allows user to add, view and delete tasks.
tasks = []
exit = 0

while (exit != 1):
    choice = int(input(f"Enter 1 to add tasks\n2 to Delete tasks\n3 to view tasks : "))
    if choice == 1:
        task = input(f"Enter your task : ")
        tasks.append(task)
    elif choice == 2:
        for i in tasks:
            print(f"{i}")
    elif choice == 0:
        exit = 1
