# In-Memory Todo Console App (Phase I: The Evolution of Todo)

This repository contains the Phase I implementation of the "Evolution of Todo" project. The objective of this phase was to build a command-line todo application that stores tasks entirely in memory, developed using a Spec-Driven Development (SDD) approach.

## Project Summary

This application is a simple command-line interface (CLI) for managing a to-do list. All task data is stored ephemerally in memory and will be lost when the application closes. It demonstrates a clean, layered architecture in Python, focusing on core functionality and readability.

## Features

The application supports the following core features:

*   **Add Task**: Create new tasks with a title and description.
*   **View Tasks**: List all existing tasks with their details and status.
*   **Update Task**: Modify the title and/or description of a task.
*   **Delete Task**: Remove tasks from the list (with confirmation).
*   **Mark Task Complete/Incomplete**: Toggle the completion status of a task.

## How to Run the Application

### Prerequisites

-   Python 3.13 or higher.

### Running Steps

1.  **Open your terminal or command prompt.**
2.  **Navigate to the root directory of this project** (where this `README.md` file is located).
3.  **Execute the application** using the Python interpreter:

    ```bash
    python main.py
    ```

4.  The application will start, display a welcome message, and present a numbered menu of options. Follow the prompts to interact with your to-do list.

## Project Structure

The core application code is organized as follows:

```
.
├── main.py             # Application entry point
├── src/
│   ├── cli.py          # Handles command-line interface and user interaction
│   ├── database.py     # Manages in-memory data storage for tasks
│   ├── models.py       # Defines the Task data structure
│   └── services.py     # Implements the business logic for task operations
├── specs/              # Contains all specification, plan, and task documents
└── history/            # Stores prompt history records
```

## Spec-Driven Development (SDD)

This project was developed using a strict Spec-Driven Development (SDD) workflow, guided by Spec-Kit Plus. All design and implementation decisions are documented in the `specs/` directory, including:

*   **Constitution**: Outlines the project's core principles and rules.
*   **Specification (`spec.md`)**: Details user stories, functional, and non-functional requirements.
*   **Implementation Plan (`plan.md`)**: Describes the architecture and technical approach.
*   **Task List (`tasks.md`)**: Breaks down the implementation into granular, actionable steps.
