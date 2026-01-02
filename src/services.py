from typing import List, Optional
from src.models import Task
import src.database as db

def add_task(title: str, description: str) -> Optional[Task]:
    """
    Adds a new task. The title cannot be empty.
    Returns the created task or None if the title is invalid.
    """
    if not title:
        return None
    
    new_task = Task(id=0, title=title, description=description)
    created_task = db.save_task(new_task)
    return created_task

def get_all_tasks() -> List[Task]:
    """Returns a list of all tasks."""
    return db.get_all_tasks()

def update_task(task_id: int, new_title: str, new_description: str) -> Optional[Task]:
    """
    Updates a task's title and/or description.
    The new title cannot be empty.
    Returns the updated task or None if the task is not found or the new title is invalid.
    """
    task = db.get_task(task_id)
    if not task:
        return None
    
    if not new_title:
        return None
        
    task.title = new_title
    task.description = new_description
    updated_task = db.save_task(task)
    return updated_task

def delete_task(task_id: int) -> bool:
    """
    Deletes a task by its ID.
    Returns True if successful, False otherwise.
    """
    return db.delete_task(task_id)

def toggle_task_status(task_id: int) -> Optional[Task]:
    """
    Toggles the completion status of a task.
    Returns the updated task or None if the task is not found.
    """
    task = db.get_task(task_id)
    if not task:
        return None
        
    task.status = not task.status
    updated_task = db.save_task(task)
    return updated_task
