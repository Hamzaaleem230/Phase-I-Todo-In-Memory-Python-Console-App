# Tasks: In-Memory Todo Console App

**Input**: Design documents from `/specs/001-in-memory-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

**Tests**: No automated tests were requested in the specification. Tasks for manual validation will be included in the implementation phase.

**Organization**: Tasks are grouped into phases, starting with setup and foundational work, followed by user stories in priority order.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the file and directory structure for the project.

- [X] T001 [P] Create the main application entry point file `main.py`
- [X] T002 [P] Create the source directory `src/`
- [X] T003 [P] Create the data model file `src/models.py`
- [X] T004 [P] Create the in-memory database file `src/database.py`
- [X] T005 [P] Create the business logic file `src/services.py`
- [X] T006 [P] Create the command-line interface file `src/cli.py`
- [X] T007 [P] Create the directory for tests `tests/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement the core data structures required by all other features.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T008 Define the `Task` dataclass in `src/models.py` with `id`, `title`, `description`, and `status` fields.
- [X] T009 Implement the in-memory database in `src/database.py` with a `_tasks` dictionary and a `_next_id` counter.
- [X] T010 [P] Implement the `save_task` function in `src/database.py`.
- [X] T011 [P] Implement the `get_task` function in `src/database.py`.
- [X] T012 [P] Implement the `get_all_tasks` function in `src/database.py`.
- [X] T013 [P] Implement the `delete_task` function in `src/database.py`.

**Checkpoint**: Foundation ready. The data layer is complete.

---

## Phase 3: User Story 1 & 2 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add a task and view the list of all tasks.
**Independent Test**: A user can run the application, add a new task, and see it displayed in the list of tasks.

### Implementation for User Story 1 & 2

- [X] T014 [US1] Implement the `add_task` function in `src/services.py` that validates the title is not empty and calls the database.
- [X] T015 [US2] Implement the `get_all_tasks` function in `src/services.py`.
- [X] T016 [US1] Implement the `_handle_add_task` function in `src/cli.py` to get input from the user.
- [X] T017 [US2] Implement the `_handle_view_tasks` function in `src/cli.py` to display the list of tasks.
- [X] T018 Implement the main menu display in `src/cli.py` to show options for adding and viewing tasks.
- [X] T019 Implement the main application loop in `src/cli.py` to process user input for adding and viewing tasks.
- [X] T020 Implement the main application entry point in `main.py` to start the CLI loop.

**Checkpoint**: User can add and view tasks. This is the core MVP.

---

## Phase 4: User Story 3 - Update Task (Priority: P2)

**Goal**: Allow users to update an existing task's title and/or description.
**Independent Test**: A user can update a task's title and description, and the changes are reflected when viewing the task list.

### Implementation for User Story 3

- [X] T021 [US3] Implement the `update_task` function in `src/services.py`.
- [X] T022 [US3] Add logic to the `update_task` function in `src/services.py` to forbid empty titles.
- [X] T023 [US3] Implement the `_handle_update_task` function in `src/cli.py`.
- [X] T024 [US3] Add the "Update Task" option to the main menu in `src/cli.py`.

**Checkpoint**: User can update tasks.

---

## Phase 5: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to delete a task.
**Independent Test**: A user can delete a task, and it no longer appears in the task list.

### Implementation for User Story 4

- [X] T025 [US4] Implement the `delete_task` function in `src/services.py`.
- [X] T026 [US4] Implement the `_handle_delete_task` function in `src/cli.py` including the confirmation prompt.
- [X] T027 [US4] Add the "Delete Task" option to the main menu in `src/cli.py`.

**Checkpoint**: User can delete tasks.

---

## Phase 6: User Story 5 - Toggle Task Status (Priority: P2)

**Goal**: Allow users to mark a task as complete or incomplete.
**Independent Test**: A user can change a task's status, and the new status is reflected in the task list.

### Implementation for User Story 5

- [X] T028 [US5] Implement the `toggle_task_status` function in `src/services.py`.
- [X] T029 [US5] Implement the `_handle_toggle_status` function in `src/cli.py`.
- [X] T030 [US5] Add the "Mark Task Complete/Incomplete" option to the main menu in `src/cli.py`.

**Checkpoint**: User can manage task completion status.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Finalize the application and handle error conditions.

- [X] T031 Add an "Exit" option to the main menu in `src/cli.py`.
- [X] T032 Implement graceful handling for invalid menu choices in `src/cli.py`.
- [X] T033 Implement error handling for non-existent task IDs in the `services.py` functions for update, delete, and toggle status.
- [X] T034 Ensure all console output is clean, readable, and consistent.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1.
- **Phase 3 (US1 & US2)** depends on Phase 2.
- **Phases 4, 5, and 6 (US3, US4, US5)** depend on Phase 3 and can be implemented in any order.
- **Phase 7 (Polish)** should be done last.

## Implementation Strategy

### MVP First (User Stories 1 & 2)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1 & 2
4.  **STOP and VALIDATE**: At this point, the core application is functional.

### Incremental Delivery

After the MVP is validated, proceed with Phases 4, 5, and 6 in any order. Complete Phase 7 last.
