# To-Do List Manager with File Handling

import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task, status = line.strip().rsplit(",", 1)
                tasks.append((task, status == "True"))
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task, status in tasks:
            file.write(f"{task},{status}\n")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for index, (task, status) in enumerate(tasks, start=1):
            print(f"{index}. {'[Done]' if status else '[ ]'} {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))
    save_tasks(tasks)
    print(f"Added task: {task}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        removed_task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"Removed task: {removed_task[0]}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        task, _ = tasks[task_num]
        tasks[task_num] = (task, True)
        save_tasks(tasks)
        print(f"Marked task as done: {task}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
