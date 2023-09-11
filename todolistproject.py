import os
import json
from datetime import datetime

# Define the filename for storing tasks
TASKS_FILE = "tasks.json"

# Initialize the tasks dictionary
tasks = []

# Check if the tasks file exists and load tasks
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

def add_task(name, priority, due_date):
    task = {
        "name": name,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    save_tasks()
    print("Task added successfully.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks()
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task index.")

def mark_task_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Application")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        name = input("Enter task name: ")
        priority = input("Enter priority (high/medium/low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(name, priority, due_date)
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        index = int(input("Enter the index of the task to mark as completed: "))
        mark_task_completed(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")