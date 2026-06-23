"""Simple To-Do List program for Project 1."""


def print_menu():
    print("\nChoose an action:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Clear all tasks")
    print("5. Quit")


def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Added task: {task}")
    else:
        print("No task entered. Try again.")


def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your task list is empty. Add a task first.")


def remove_task(tasks):
    if not tasks:
        print("There are no tasks to remove.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to remove: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("That task number is not in the list.")


def clear_tasks(tasks):
    if not tasks:
        print("The task list is already empty.")
        return

    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        tasks.clear()
        print("All tasks have been cleared.")
    else:
        print("Clear canceled.")


def main():
    tasks = []

    print("Welcome to the To-Do List program!")
    print("Manage your tasks using the menu below.")

    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            clear_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()