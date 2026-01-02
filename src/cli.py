import src.services as services

def _handle_add_task():
    """Handles the user interaction for adding a new task."""
    print("Enter task title:")
    title = input("> ")
    print("Enter task description (optional):")
    description = input("> ")
    task = services.add_task(title, description)
    if task:
        print(f"Task '{task.title}' added successfully with ID {task.id}.")
    else:
        print("Error: Task title cannot be empty.")

def _handle_view_tasks():
    """Handles the user interaction for viewing all tasks."""
    tasks = services.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    print("--- Your Tasks ---")
    for task in tasks:
        status = "Complete" if task.status else "Incomplete"
        print(f"ID: {task.id} | Title: {task.title} | Description: {task.description} | Status: {status}")
    print("--------------------")

def _handle_update_task():
    """Handles the user interaction for updating a task."""
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        print("Enter new task title:")
        new_title = input("> ")
        print("Enter new task description (optional):")
        new_description = input("> ")
        
        updated_task = services.update_task(task_id, new_title, new_description)
        
        if updated_task:
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Error: Could not update task {task_id}. Make sure the ID exists and the title is not empty.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def _handle_delete_task():
    """Handles the user interaction for deleting a task."""
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ")
        if confirm.lower() == 'y':
            if services.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error: Task {task_id} not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def _handle_toggle_status():
    """Handles the user interaction for toggling a task's status."""
    try:
        task_id = int(input("Enter the ID of the task to toggle status: "))
        task = services.toggle_task_status(task_id)
        if task:
            status = "Complete" if task.status else "Incomplete"
            print(f"Task {task_id} status changed to {status}.")
        else:
            print(f"Error: Task {task_id} not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def _display_menu():
    """Displays the main menu."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("-----------------------")

def main_loop():
    """The main application loop."""
    print("Welcome to your To-Do List!")
    while True:
        _display_menu()
        choice = input("Enter your choice: ")
        print() # Add a newline for readability
        
        if choice == '1':
            _handle_add_task()
        elif choice == '2':
            _handle_view_tasks()
        elif choice == '3':
            _handle_update_task()
        elif choice == '4':
            _handle_delete_task()
        elif choice == '5':
            _handle_toggle_status()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
