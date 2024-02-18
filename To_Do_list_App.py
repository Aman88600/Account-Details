# This is a cmd based app, that, allows user to add, view and delete tasks.
tasks = []
exit = 0

while (exit != 1):
    choice = int(input(f"1 to Add Task\n2 to Remove Task\n3 to View Tasks\n4 Exit\nEnter your choice :"))
    if choice == 1:
        task = input(f"Enter your task : ")
        tasks.append(task)
        print("\n")
    elif choice == 2:
        task_number = int(input("Enter the Task number to remove : "))
        tasks.pop(task_number - 1)
        print("\n")
    elif choice == 3:
        for index, element in enumerate(tasks, start=1):
            print(f"{index}. {element}")
        print("\n")
    elif choice == 4:
        exit = 1
