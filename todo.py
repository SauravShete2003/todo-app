def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for t in tasks:
            file.write(t + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    print("\nYour tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid task number.")

def main():
    print("Welcome to the To-Do List App!")
    tasks = load_tasks()

    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Quit")
        print("4. Delete task")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
