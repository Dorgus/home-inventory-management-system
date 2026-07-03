# Contributing to Home Inventory Management System

## Branch Naming

Create branches based on the issue you're working on:

```
<category>/<short-description>
```

| Category | Use For | Example |
|----------|---------|---------|
| `setup/` | Environment & config (Issues 1) | `setup/init-project` |
| `db/` | Database schema (Issues 2-3) | `db/core-tables` |
| `api/` | Backend API work (Issues 4-9) | `api/flask-setup-categories` |
| `frontend/` | HTML, CSS, JS (Issues 10-16) | `frontend/static-html-layout` |
| `test/` | Testing (Issues 17-19) | `test/pytest-basics` |
| `ci/` | CI/CD pipeline (Issue 20) | `ci/github-actions` |
| `fix/` | Bug fixes | `fix/item-validation` |

## Commit Messages

Use clear, descriptive commit messages:

```
<Short summary of what changed>
```

**Example:**
```
Add Flask setup and categories API endpoint
```

**Rules:**
- Use imperative mood, max 72 characters (e.g., "Add...", "Fix...", "Update...")
- Add a blank line + body for longer explanations if needed
- Keep each commit focused on a single change

## Pull Requests

### Before Opening a PR

- [ ] Your code runs without errors
- [ ] You've tested your changes locally
- [ ] Your branch is up to date with `main` (`git pull origin main`)

### PR Title

Use the same title as the issue:
```
Issue N: <Issue Title>
```
Example: `Issue 4: Backend API - Flask Setup & Categories`

### PR Description

Use this template:

```markdown
## Summary
Brief description of what this PR does.

## Changes
- List the key changes made

## Issue
Closes #<issue-number>

## Testing
How did you test this? What commands to run?
```

> **⚠️ Important:** Every PR **must** include `Closes #N` in the description to link it to the issue. PRs without issue links will be sent back for revision.

## Code Style

- **Python:** Follow PEP 8 conventions
- **Files:** End every file with a newline
- **Imports:** Group into standard library, third-party, and local — separated by blank lines
- **No hardcoded secrets** — use environment variables

## Review Process

1. Open your PR against `main`
2. A reviewer will review your code and leave comments
3. Address all feedback and push fixes to the **same branch**
4. Once approved, **you merge your own PR**

## Questions?

If you're unsure about anything, ask in the PR comments or reach out before writing code.
