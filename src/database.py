from typing import Dict, List, Optional
from src.models import Task

# In-memory "database"
_tasks: Dict[int, Task] = {}
_next_id: int = 1

def save_task(task: Task) -> Task:
    """Saves a task to the database, assigning an ID if it's new."""
    global _next_id
    if task.id == 0:  # New task
        task.id = _next_id
        _next_id += 1
    _tasks[task.id] = task
    return task

def get_task(task_id: int) -> Optional[Task]:
    """Retrieves a single task by its ID."""
    return _tasks.get(task_id)

def get_all_tasks() -> List[Task]:
    """Retrieves all tasks, sorted by ID."""
    return sorted(_tasks.values(), key=lambda t: t.id)

def delete_task(task_id: int) -> bool:
    """Deletes a task by its ID. Returns True if successful, False otherwise."""
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False
