print ("Welcome to the To-Do List App!")

tasks = []

try: 
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    pass

while True:
    print("\nChoose an option:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Quit")

    choice = input("Enter choice: ")
    if choice == '1':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif choice == '2':
        task = input("Enter a new task: ")
        tasks.append(task)
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task added.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")