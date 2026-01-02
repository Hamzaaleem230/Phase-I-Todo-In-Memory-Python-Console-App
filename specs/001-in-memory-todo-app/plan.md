# Implementation Plan: In-Memory Todo Console App

**Branch**: `001-in-memory-todo-app` | **Date**: 2026-01-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-in-memory-todo-app/spec.md`

## Summary

This plan outlines the implementation of a simple, in-memory, console-based Todo application in Python. The application will adhere strictly to the constitution and the clarified specification, featuring a clean, layered architecture to separate concerns and ensure readability and maintainability.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python Standard Library Only
**Storage**: In-memory (Python dictionary)
**Testing**: `unittest` (Python standard library)
**Target Platform**: Console Application
**Project Type**: Single project
**Performance Goals**: All user operations must complete within 100 milliseconds.
**Constraints**: Beginner-readable, simple, deterministic, no external frameworks.
**Scale/Scope**: 5 core features, single user, ephemeral data.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] I. No Manual Application Code: All code will be generated from this plan.
- [X] II. Python Console Application: The project is a pure Python console app.
- [X] III. In-Memory Data Storage: Data will be stored in a Python dictionary.
- [X] IV. Clean Architecture: The proposed structure separates data, logic, and UI.
- [X] V. Core Features: The plan maps directly to the 5 core features.
- [X] VI. Task Structure: The data model matches the `Task` entity specification.
- [X] VII. Python Version: The project will target Python 3.13+.
- [X] VIII. Simplicity: The solution is minimal and uses only the standard library.
- [X] IX. Standard Library Only: No external frameworks will be used.
- [X] X. Specification-Driven: The plan is derived directly from the spec.
- [X] XI. Code Generation: This plan enables code generation.

*All constitutional gates pass.*

## Project Structure

### Documentation (this feature)

```text
specs/001-in-memory-todo-app/
├── plan.md              # This file
├── research.md          # Confirms no research was needed
├── data-model.md        # Defines the Task entity
├── quickstart.md        # Explains how to run the app
├── contracts/           # Empty, as this is not a service-based app
│   └── .gitkeep
└── tasks.md             # To be created by /sp.tasks command
```

### Source Code (repository root)

```text
src/
├── models.py         # Contains the Task data class.
├── database.py       # Manages the in-memory data store.
├── services.py       # Contains the business logic for task management.
└── cli.py            # Handles all user interaction (menu, input, output).
main.py               # The main entry point for the application.
tests/
└── (To be implemented in a later phase)
```

**Structure Decision**: A single project structure with a layered architecture is chosen. This aligns with the constitution's principles of simplicity, clean architecture, and readability. It provides a clear separation of concerns, making the codebase easy to understand, maintain, and test, while being future-proof for potential enhancements.

### File-by-File Responsibility

-   **`main.py`**:
    -   **Responsibility**: The application's entry point.
    -   **Execution**: It will import the main loop function from `cli.py` and execute it to start the application.

-   **`src/models.py`**:
    -   **Responsibility**: Defines the shape of the data.
    -   **Implementation**: Will contain a `Task` dataclass (from the `dataclasses` module) with fields: `id: int`, `title: str`, `description: str`, `status: bool`.

-   **`src/database.py`**:
    -   **Responsibility**: Manages in-memory storage.
    -   **Implementation**: Will contain a dictionary named `_tasks` to store `Task` objects, with the task ID as the key. A variable, `_next_id`, will be used to generate new, auto-incrementing IDs. It will provide functions like `get_task`, `get_all_tasks`, `save_task`, and `delete_task`. This module will be the single source of truth for all task data.

-   **`src/services.py`**:
    -   **Responsibility**: Implements all business logic. It acts as the intermediary between the CLI and the database.
    -   **Implementation**: Will contain functions like `add_task(title, description)`, `update_task(task_id, title, description)`, `delete_task(task_id)`, etc. These functions will interact with the `database.py` module to perform CRUD operations and will contain logic like validating input (e.g., non-empty titles) before passing data to the database module.

-   **`src/cli.py`**:
    -   **Responsibility**: Handles all command-line interaction.
    -   **Implementation**: Will contain the main application loop (`main_loop`). It will display the numbered menu, prompt the user for input, and call the appropriate functions in `services.py` based on the user's choice. It is also responsible for printing task lists and confirmation/error messages to the console.

### Execution Flow

1.  The user runs `python main.py`.
2.  `main.py` calls the `main_loop()` function in `cli.py`.
3.  `cli.py` enters a `while` loop that continues until the user chooses to exit.
4.  Inside the loop, `cli.py` prints the menu of options (Add, View, Update, etc.).
5.  `cli.py` prompts the user for a choice.
6.  Based on the choice, `cli.py` calls the corresponding function in `services.py` (e.g., `services.add_task(...)`).
7.  `services.py` performs the business logic and validation, then calls the necessary function in `database.py`.
8.  `database.py` modifies the in-memory `_tasks` dictionary.
9.  Control returns to `cli.py`, which displays a success or error message.
10. The loop repeats.

### User Command to Function Mapping

| User Command (in CLI) | `cli.py` Function | `services.py` Function | `database.py` Functions |
|---|---|---|---|
| 1. Add Task | `_handle_add_task()` | `add_task()` | `save_task()` |
| 2. View Tasks | `_handle_view_tasks()` | `get_all_tasks()` | `get_all_tasks()` |
| 3. Update Task | `_handle_update_task()` | `update_task()` | `get_task()`, `save_task()` |
| 4. Delete Task | `_handle_delete_task()` | `delete_task()` | `get_task()`, `delete_task()` |
| 5. Mark Complete/Incomplete | `_handle_toggle_status()` | `toggle_task_status()` | `get_task()`, `save_task()` |
| 6. Exit | (Breaks the main loop) | - | - |

## Complexity Tracking

No violations of the constitution were required. The plan adheres to all principles.
