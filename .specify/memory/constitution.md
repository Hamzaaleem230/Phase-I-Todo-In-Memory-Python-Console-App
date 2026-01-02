<!--
Sync Impact Report:
Version change: 0.0.0 → 1.0.0
Added sections: All
Templates requiring updates:
- .specify/templates/plan-template.md (⚠ pending)
- .specify/templates/spec-template.md (⚠ pending)
- .specify/templates/tasks-template.md (⚠ pending)
-->
# Phase I – In-Memory Python Todo Console App Constitution

## Core Principles

### I. No Manual Application Code
I (the human) will NOT write any application code manually. All code must be generated strictly from specifications.

### II. Python Console Application
The application must be a pure Python console application.

### III. In-Memory Data Storage
Data must be stored ONLY in memory (no files, no database).

### IV. Clean Architecture
Clean architecture, separation of concerns, and readability are mandatory.

### V. Core Features
The system must support exactly these core features:
- Add Task
- Delete Task
- Update Task
- View Task List
- Mark Task as Complete / Incomplete

### VI. Task Structure
Each task must have:
- Unique ID
- Title
- Description
- Completion status

### VII. Python Version
Python version must be compatible with Python 3.13+

### VIII. Simplicity
The solution must be simple, deterministic, and beginner-readable.

### IX. Standard Library Only
No external frameworks are allowed (standard library only).

### X. Specification-Driven
Any ambiguity must be resolved by improving the specification, not by guessing.

### XI. Code Generation
All code must be generated strictly from specifications.

## Governance

This Constitution supersedes all other practices. Amendments require documentation, review, and approval.

**Conceptual Sub-agents:**
- **Spec Guardian Agent**: Ensures constitution compliance.
- **Python Quality Agent**: Ensures clean Python structure.
- **CLI UX Agent**: Ensures clear command-line interaction.

Violation of the constitution is not allowed.

**Version**: 1.0.0 | **Ratified**: 2026-01-03 | **Last Amended**: 2026-01-03