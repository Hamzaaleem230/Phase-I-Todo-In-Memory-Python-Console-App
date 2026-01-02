# Feature Specification: In-Memory Todo Console App

**Feature Branch**: `001-in-memory-todo-app`
**Created**: 2026-01-03
**Status**: Draft
**Input**: User description: "Define the full functional specification for Phase I: In-Memory Todo Console App..."

## Clarifications

### Session 2026-01-03
- Q: How should the "Unique ID" for each task be generated? → A: Simple integer increment (1, 2, 3, ...)
- Q: Should the system prevent a user from updating a task to have an empty title? → A: Yes, forbid empty titles on updates and show an error.
- Q: What format should the main menu use? → A: Numbered list of actions (e.g., "1. Add Task", "2. View Tasks")
- Q: What is a measurable target for "fast execution" for any single user operation (e.g., adding a task, viewing tasks)? → A: All user operations complete within 100 milliseconds.
- Q: What should the confirmation prompt be when deleting a task? → A: Prompt: "Are you sure you want to delete task [ID]? (y/N): ". Accept 'y' or 'Y' for yes, any other input (including empty) for no.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a new task (Priority: P1)

As a user, I want to add a new task with a title and description so that I can keep track of my to-dos.

**Why this priority**: This is the most fundamental feature. Without it, the application is not usable.

**Independent Test**: The user can add a task and see it in the task list.

**Acceptance Scenarios**:

1.  **Given** the application is running, **When** the user chooses to add a task and provides a title and description, **Then** the task is added to the list with a unique ID and a status of "Incomplete".
2.  **Given** the application is running, **When** the user chooses to add a task but provides an empty title, **Then** an error message is displayed, and the task is not added.

### User Story 2 - View all tasks (Priority: P1)

As a user, I want to see a list of all my tasks so that I can review what I need to do.

**Why this priority**: This is a core feature for the user to see their tasks.

**Independent Test**: The user can view all added tasks with their details.

**Acceptance Scenarios**:

1.  **Given** there are tasks in the list, **When** the user chooses to view all tasks, **Then** all tasks are displayed with their ID, Title, Description, and Status.
2.  **Given** there are no tasks in the list, **When** the user chooses to view all tasks, **Then** a message indicating that there are no tasks is displayed.

### User Story 3 - Update an existing task (Priority: P2)

As a user, I want to update the title and/or description of a task so that I can correct or change task details.

**Why this priority**: This allows users to manage and maintain their tasks.

**Independent Test**: The user can update a task and see the changes reflected in the task list.

**Acceptance Scenarios**:

1.  **Given** a task exists, **When** the user chooses to update it by providing its ID and a new title and/or description, **Then** the task is updated.
2.  **Given** the user tries to update a task with an ID that does not exist, **When** the user provides the non-existent ID, **Then** an error message is displayed.
3.  **Given** a task exists, **When** the user attempts to update its title to an empty string, **Then** an error message is displayed, and the task's title remains unchanged.

### User Story 4 - Delete a task (Priority: P2)

As a user, I want to delete a task so that I can remove completed or unnecessary tasks.

**Why this priority**: This is an essential task management feature.

**Independent Test**: The user can delete a task, and it will no longer appear in the task list.

**Acceptance Scenarios**:

1.  **Given** a task exists, **When** the user chooses to delete it by its ID and confirms the action, **Then** the task is removed from the list.
2.  **Given** the user tries to delete a task with an ID that does not exist, **When** the user provides the non-existent ID, **Then** an error message is displayed.

### User Story 5 - Mark a task as complete/incomplete (Priority: P2)

As a user, I want to mark a task as complete or incomplete so that I can track my progress.

**Why this priority**: This is a key feature for tracking task status.

**Independent Test**: The user can change the completion status of a task, and the change is reflected in the task list.

**Acceptance Scenarios**:

1.  **Given** a task is incomplete, **When** the user chooses to mark it as complete by its ID, **Then** the task's status is changed to "Complete".
2.  **Given** a task is complete, **When** the user chooses to mark it as incomplete by its ID, **Then** the task's status is changed to "Incomplete".

### Edge Cases

-   Attempting to update, delete, or change the status of a task with a non-existent ID.
-   Providing invalid input at the main menu.
-   Providing an empty title when adding or updating a task.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: System MUST allow a user to add a task with a title and description.
-   **FR-002**: System MUST automatically generate a unique ID for each new task.
-   **FR-003**: System MUST initially mark all new tasks as incomplete.
-   **FR-004**: System MUST allow a user to view a list of all tasks, including their ID, title, description, and completion status.
-   **FR-005**: System MUST allow a user to update the title and/or description of an existing task using its ID. System MUST NOT allow a task's title to be updated to an empty string.
-   **FR-006**: System MUST display an error message if the user tries to update a task with an ID that does not exist.
-   **FR-007**: System MUST allow a user to delete a task using its ID.
-   **FR-008**: System MUST ask for confirmation before deleting a task with the prompt "Are you sure you want to delete task [ID]? (y/N): ". It MUST accept 'y' or 'Y' for confirmation and treat any other input (including empty) as cancellation.
-   **FR-009**: System MUST allow a user to toggle the completion status of a task between "Complete" and "Incomplete" using its ID.
-   **FR-010**: System MUST run in a loop, presenting a clear menu of options as a numbered list of actions, until the user chooses to exit.
-   **FR-011**: System MUST handle invalid user input gracefully.

### Non-Functional Requirements

-   **NFR-001**: No persistent storage (data is stored in-memory).
-   **NFR-002**: No asynchronous code.
-   **NFR-003**: No database.
-   **NFR-004**: No web server.
-   **NFR-005**: All user operations must complete within 100 milliseconds.
-   **NFR-006**: The code must have a clean, modular structure suitable for teaching and demonstration.

### Key Entities *(include if feature involves data)*

-   **Task**:
    -   ID (integer, auto-incrementing)
    -   Title (string)
    -   Description (string)
    -   Completion Status (boolean: Complete/Incomplete)

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: A user can successfully add, view, update, delete, and change the status of a task in under 1 minute per operation.
-   **SC-002**: 100% of core features (add, view, update, delete, toggle status) are implemented and functional.
-   **SC-003**: The application starts and is ready to accept user input in under 2 seconds.
-   **SC-004**: The application provides clear feedback for all user actions (e.g., "Task added successfully," "Task not found").