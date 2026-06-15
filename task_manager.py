"""Simple To-Do Manager"""

tasks = []

def add_task(task):
    """Add a task to the list."""
    tasks.append(task)

def view_tasks():
    """Display all tasks."""
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(index):
    """Delete a task."""
    if 0 <= index < len(tasks):
        tasks.pop(index)

# Simple Test
def test_add_task():
    """Test function."""
    sample = []
    sample.append("Study")
    assert len(sample) == 1

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        num = int(input("Enter task number: "))
        delete_task(num - 1)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
