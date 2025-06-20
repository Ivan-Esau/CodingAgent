import os # Import os to access environment variables
from core import CodingAgent
from llm import LLMProvider
from git_operations import GitOps # GitOps might be phased out or changed

def main():
    print("Initializing Coding Agent System...")

    # Attempt to get ANTHROPIC_API_KEY from environment
    # Pass this to LLMProvider. If not found, LLMProvider will use its default (None or DUMMY_KEY)
    # and operate in simulation mode.
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    if not anthropic_api_key:
        print("Main: ANTHROPIC_API_KEY environment variable not found. LLMProvider will run in simulation mode.")
        # LLMProvider's __init__ will handle falling back to simulation if api_key is None or dummy
        # We can pass None or the DUMMY key explicitly if we want to be certain from main's perspective
        # anthropic_api_key = "DUMMY_ANTHROPIC_API_KEY" # Ensure simulation
    else:
        print(f"Main: Found ANTHROPIC_API_KEY (length: {len(anthropic_api_key)}). LLMProvider might attempt real calls if key is valid.")


    gitlab_mcp_config = {
        "type": "url",
        "url": "https://placeholder.gitlab-mcp.example.com/sse",
        "name": "gitlab_tool_server",
    }

    github_mcp_config = {
        "type": "url",
        "url": "https://placeholder.github-mcp.example.com/sse",
        "name": "github_tool_server",
    }

    # Pass the retrieved (or default) API key to LLMProvider
    llm_provider = LLMProvider(api_key=anthropic_api_key, mcp_server_configs=[gitlab_mcp_config, github_mcp_config])

    # GitOps role might change significantly if LLM uses MCP tools for Git.
    # For now, it's still initialized.
    git_ops = GitOps(token="DUMMY_GIT_TOKEN")

    agent = CodingAgent(llm_client=llm_provider, git_client=git_ops)

    print("Coding Agent System initialized.")
    print(f"LLMProvider Simulation Mode: {llm_provider.simulation_mode}")
    print("=" * 40)

    # GitLab Test Case
    gitlab_task_description = "What is the status of the latest pipeline on my GitLab project?"
    print(f"Main script starting GitLab task: {gitlab_task_description}")
    agent.process_task(gitlab_task_description, task_type="gitlab_query")
    print("=" * 40)

    # GitHub Test Case
    github_task_description = "Get the content of 'README.md' from the GitHub repo and then get comments for issue 42."
    print(f"Main script starting GitHub task: {github_task_description}")
    agent.process_task(github_task_description, task_type="github_query")
    print("=" * 40)

    # General Code Generation Test Case
    coding_task_description = "Refactor the authentication module to use a new hashing library."
    print(f"Main script starting Coding task: {coding_task_description}")
    agent.process_task(coding_task_description, task_type="code_generation")
    print("=" * 40)

    print("Coding Agent task processing finished in main script.")

if __name__ == "__main__":
    main()
