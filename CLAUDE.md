# Claude Code Workflow Documentation

This project serves as a reference implementation demonstrating the modern development workflow using Claude Code with the dotfiles from [talent-factory/dotfiles](https://github.com/talent-factory/dotfiles).

## Overview

The UPN Calculator project was developed entirely using the Claude Code workflow, showcasing a structured approach from requirements to implementation.

## Workflow Steps

### Step 1: Create Product Requirements Document (PRD)

The first step is to define what needs to be built using the `/project:create-prd` command.

For this project, the initial prompt was simply:

```bash
/project:create-prd "Ich benötige ein CLI Program oder konkret ein UPN Taschenrechner, welche neben den Grundfunktionen auch sin(), cos() und tan() kennt."
```

This natural language description is all that's needed to get started!

**What happens:**

- Claude analyzes the feature description
- Creates a comprehensive PRD with:
  - Problem statement
  - Goals and objectives
  - Requirements (functional & non-functional)
  - Technical specifications
  - Success metrics
- Saves the PRD to `.plans/{project-name}/PRD.md`

**Benefits:**

- Clear documentation of project goals
- Alignment between stakeholders
- Foundation for planning

### Step 2: Generate Project Plan

From the PRD, create a structured project plan with `/project:create-plan-fs`:

```bash
/project:create-plan-fs
```

**What happens:**

- Analyzes the PRD
- Breaks down work into discrete tasks
- Creates `.plans/{project-name}/` structure with:
  - `EPIC.md` - Epic description
  - `PRD.md` - Product Requirements Document
  - `STATUS.md` - Project status tracking
  - `tasks/` - Individual task files with acceptance criteria

**Task Structure:**

Each task file contains:

- Title and description
- Acceptance criteria
- Dependencies on other tasks
- Status tracking

**Benefits:**

- Filesystem-based task tracking (no external tools needed)
- Clear breakdown of work
- Easy progress tracking with STATUS.md
- Git-friendly (can be committed and reviewed)

### Step 3: Implement Tasks

Implement each task with `/develop:implement-fs-task`:

```bash
/develop:implement-fs-task
```

**What happens:**

1. Shows list of available tasks
2. User selects a task
3. Claude:
   - Creates a feature branch (`task-XXX-description`)
   - Reads task requirements and acceptance criteria
   - Implements the functionality
   - Writes tests
   - Runs tests to verify
   - Creates a commit
   - Pushes the branch
   - Creates a pull request with detailed description
4. Updates task status in `.plans/{project-name}/STATUS.md`

**Benefits:**

- Consistent branch naming
- Automatic PR creation
- Test-driven development
- Clear commit history
- Each task is isolated and reviewable

## Additional Workflow Commands

### Professional Commits

```bash
/develop:commit
```

Creates professional Git commits with:

- Conventional commit format
- Automatic change analysis
- Pre-commit hook support
- Multi-file staging

### Pull Request Creation

```bash
/develop:create-pr
```

Creates pull requests with:

- Automatic summary generation
- Test plan
- Branch comparison
- Commit analysis

### Code Quality

```bash
/develop:ruff-check
```

Runs Ruff linter and formatter on all Python files:

- Automatic code formatting
- Linting issues detection
- Import sorting
- PEP 8 compliance

## Project Structure

### `.plans/` Directory

The `.plans/` directory contains the filesystem-based task management:

```
.plans/
└── upn-taschenrechner-cli/
    ├── EPIC.md                    # Epic description
    ├── PRD.md                     # Product Requirements Document
    ├── README.md                  # Project overview
    ├── STATUS.md                  # Task status tracking
    └── tasks/
        ├── task-001-upn-parser-core.md
        ├── task-002-grundoperationen.md
        ├── task-003-trigonometrische-funktionen.md
        ├── task-004-cli-repl.md
        ├── task-005-stack-management.md
        └── task-006-error-handling.md
```

**STATUS.md Structure:**

The STATUS.md file tracks task completion:

- Lists all tasks with their status (pending/in_progress/completed)
- Shows dependencies between tasks
- Provides progress overview
- Updated automatically when tasks are implemented

**Task File Structure:**

Each task file (e.g., `task-001-upn-parser-core.md`) contains:

- Task title and description
- Acceptance criteria
- Implementation notes
- Dependencies on other tasks

## Advantages of This Workflow

### 1. Documentation-First

- PRD ensures clear understanding
- Requirements are documented before coding
- Easy to review and discuss changes

### 2. Structured Planning

- Tasks are well-defined
- Dependencies are explicit
- Progress is trackable

### 3. Quality Assurance

- Tests are written with implementation
- Code review via pull requests
- Automated linting and formatting

### 4. Git-Friendly

- All planning files are in Git
- Changes are reviewable
- History is preserved

### 5. Autonomous Development

- Claude can work independently on tasks
- Consistent patterns across tasks
- Reduced context switching

## Setup Requirements

### Install dotfiles

```bash
git clone https://github.com/talent-factory/dotfiles
cd dotfiles
# Follow installation instructions
```

### Configure Claude Code

The dotfiles provide:

- Slash commands in `.claude/commands/`
- Agents in `.claude/agents/`
- Project templates

### Dependencies

- Claude Code (latest version)
- Git
- GitHub CLI (`gh`)
- Python >= 3.13 (for this project)
- uv (Python package manager)

## Usage Tips

### Starting a New Project

1. Create PRD first:

   ```bash
   /project:create-prd "Your feature description"
   ```

2. Review and refine the PRD manually in `.plans/{project-name}/PRD.md` if needed

3. Generate plan:

   ```bash
   /project:create-plan-fs
   ```

4. Review STATUS.md and task files in `.plans/{project-name}/tasks/`

5. Start implementing:

   ```bash
   /develop:implement-fs-task
   ```

### Working on Existing Tasks

1. Check task status in `.plans/{project-name}/STATUS.md`
2. Run `/develop:implement-fs-task`
3. Select pending task
4. Claude implements and creates PR
5. Review PR on GitHub
6. Merge when ready

### Tracking Progress

Check `.plans/{project-name}/STATUS.md` for:

- Task status (pending/in_progress/completed)
- Dependencies between tasks
- Overall project progress
- Recently completed tasks

## Example: This Project

This UPN Calculator was built following the exact workflow:

1. **PRD Created**: `.plans/upn-taschenrechner-cli/PRD.md`
   - Started with simple natural language prompt: "Ich benötige ein CLI Program oder konkret ein UPN Taschenrechner, welche neben den Grundfunktionen auch sin(), cos() und tan() kennt."
   - Claude generated comprehensive PRD with requirements, specifications, and success criteria
   - Defined operations (basic arithmetic, trigonometric functions, advanced operations)

2. **Plan Generated**: `.plans/upn-taschenrechner-cli/`
   - Task 001: UPN Parser Core
   - Task 002: Grundoperationen (+, -, *, /)
   - Task 003: Trigonometrische Funktionen
   - Task 004: CLI REPL
   - Task 005: Stack Management
   - Task 006: Error Handling

3. **Tasks Implemented**:
   - Each task got its own branch (e.g., `task-002-grundoperationen`)
   - Tests written for each feature
   - PRs created and merged
   - Status tracked in STATUS.md

4. **Result**:
   - Clean commit history
   - Well-tested code
   - Complete documentation
   - Professional PRs

## Conclusion

This workflow demonstrates how Claude Code can be used for structured, professional software development. The combination of PRD creation, filesystem-based planning, and automated task implementation provides a powerful and reproducible development process.

For more information and to adopt this workflow, see:

- [talent-factory/dotfiles](https://github.com/talent-factory/dotfiles)
- This project as a working example
