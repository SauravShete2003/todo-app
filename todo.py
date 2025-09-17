print("Welcome to the To-Do List App!")

tasks = []

# Load tasks from file if it exists
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    pass  # if no file exists yet, ignore

while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    print("4. Delete task")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print(f"Task '{task}' added!")

    elif choice == "2":
        print("\nYour tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "4":
        print("\nYour tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)

            # Rewrite file without deleted task
            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(t + "\n")

            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
