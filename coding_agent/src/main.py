from core import CodingAgent
from llm import LLMProvider
from git_operations import GitOps # GitOps might be phased out or changed

def main():
    print("Initializing Coding Agent System...")

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

    llm_provider = LLMProvider(api_key="DUMMY_ANTHROPIC_API_KEY", mcp_server_configs=[gitlab_mcp_config, github_mcp_config])
    git_ops = GitOps(token="DUMMY_GIT_TOKEN")

    agent = CodingAgent(llm_client=llm_provider, git_client=git_ops)

    print("Coding Agent System initialized with MCP awareness for GitLab and GitHub.")
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
