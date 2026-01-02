---
id: 0001
title: Initialize Project Constitution
stage: constitution
date: 2026-01-03
surface: agent
model: gemini-pro
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
tests:
  - none
---

## Prompt

/sp.constitution

You are Claude Code operating under Spec-Kit Plus.

Project: Phase I – In-Memory Python Todo Console App

Core Rules (Non-Negotiable):
1. I (the human) will NOT write any application code manually.
2. All code must be generated strictly from specifications.
3. The application must be a pure Python console application.
4. Data must be stored ONLY in memory (no files, no database).
5. Clean architecture, separation of concerns, and readability are mandatory.
6. The system must support exactly these core features:
   - Add Task
   - Delete Task
   - Update Task
   - View Task List
   - Mark Task as Complete / Incomplete
7. Each task must have:
   - Unique ID
   - Title
   - Description
   - Completion status
8. Python version must be compatible with Python 3.13+
9. The solution must be simple, deterministic, and beginner-readable.
10. No external frameworks are allowed (standard library only).
11. Any ambiguity must be resolved by improving the specification, not by guessing.

Subagents (Conceptual):
- Spec Guardian Agent: Ensures constitution compliance.
- Python Quality Agent: Ensures clean Python structure.
- CLI UX Agent: Ensures clear command-line interaction.

Violation of the constitution is not allowed.

## Response snapshot

Wrote the constitution to `.specify/memory/constitution.md` and updated `.specify/templates/plan-template.md` to align with the new principles.

## Outcome

- ✅ Impact: Created the project constitution and aligned dependent templates.
- 🧪 Tests: n/a
- 📁 Files: 2 files modified
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: The process was smooth. The constitution provides a solid foundation for the project.

## Evaluation notes (flywheel)

- Failure modes observed: n/a
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment: n/a
