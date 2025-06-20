# Coding Agent Project

This project is an autonomous coding agent designed to understand tasks, write code, and interact with Git repositories (like GitLab or GitHub).

## Project Goals (High-Level)

- **LLM Integration**: Allow users to specify which LLM to use (e.g., Anthropic models).
- **Git Workflow Automation**: Enable the agent to manage Git operations such as branching, committing, pushing, and potentially merging.
- **Task Management**: Allow the agent to read tasks/tickets, prioritize them, and work on them autonomously.
- **Pipeline Awareness**: Monitor CI/CD pipeline statuses and attempt to debug errors.
- **Frontend Interface**: Provide a user-friendly frontend for configuration, monitoring, and interaction.
- **Secure Credential Management**: Handle API keys and other sensitive data securely.

## Current Structure

The project is in its initial phase and has the following basic structure:

```
coding_agent/
├── config/
│   └── config.example.yaml  # Example configuration for API keys
├── src/
│   ├── core/
│   │   └── __init__.py      # Contains CodingAgent class for orchestrating tasks
│   ├── git_operations/
│   │   └── __init__.py      # Contains GitOps class for Git interactions (placeholder)
│   ├── llm/
│   │   └── __init__.py      # Contains LLMProvider class for LLM interactions (placeholder)
│   ├── __init__.py
│   └── main.py              # Main executable script to run the agent
├── tests/
│   └── __init__.py          # Placeholder for tests
└── README.md                # This file
```

### Modules

- **`coding_agent/src/main.py`**: The main entry point to run the agent.
- **`coding_agent/src/core/__init__.py`**: Defines the `CodingAgent` class, which is responsible for the main workflow of processing a task, coordinating with the LLM and Git modules.
- **`coding_agent/src/llm/__init__.py`**: Defines `LLMProvider`, a placeholder for interacting with Large Language Models (e.g., for code generation, code review).
- **`coding_agent/src/git_operations/__init__.py`**: Defines `GitOps`, a placeholder for handling Git commands (e.g., commit, push, branch).
- **`coding_agent/config/`**: Intended for configuration files. `config.example.yaml` shows an example of how API keys might be stored.
- **`coding_agent/tests/`**: Will contain unit and integration tests.

## Getting Started (Current - Placeholder Implementation)

To run the current placeholder version:

```bash
python3 coding_agent/src/main.py
```

This will simulate the agent processing a predefined task using the placeholder modules.

## Next Steps

The immediate next steps involve fleshing out the placeholder modules with actual functionality for LLM communication and Git operations.
