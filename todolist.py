tasks = []

def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"task_name": task_name, "completed": False})
    print("Task added successfully!")

def mark_completed():
    view_tasks()
    task_index = int(input("Enter the index of the task to mark as completed: "))
    tasks[task_index]["completed"] = True
    print("Task marked as completed!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task_name']} - {status}")

def remove_task():
    view_tasks()
    task_index = int(input("Enter the index of the task to remove: "))
    removed_task = tasks.pop(task_index)
    print(f"Task '{removed_task['task_name']}' removed successfully!")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_completed()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
