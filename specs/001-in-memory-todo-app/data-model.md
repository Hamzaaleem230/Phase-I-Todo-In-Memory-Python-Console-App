# Data Model: In-Memory Todo Console App

This document defines the data entities for the feature, based on the `spec.md`.

## Task Entity

The core entity of the application.

**Attributes**:

| Name | Type | Description | Constraints |
|---|---|---|---|
| `id` | integer | Unique identifier for the task. | Auto-incrementing, starting from 1. Cannot be updated. |
| `title` | string | The title of the task. | Mandatory. Cannot be an empty string. |
| `description` | string | A detailed description of the task. | Optional. Can be empty. |
| `status` | boolean | The completion status of the task. | Defaults to `False` (Incomplete). |

**State Transitions**:

- A `Task` is created with `status = False`.
- The `status` can be toggled between `False` (Incomplete) and `True` (Complete) by the user.

**Relationships**:

- None. This is a single-entity model.
