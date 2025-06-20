from core import CodingAgent
from llm import LLMProvider
from git_operations import GitOps # GitOps might be phased out or changed

def main():
    print("Initializing Coding Agent System...")

    # Example MCP server configuration (replace with actual URL when available and public)
    # For now, this URL is a placeholder because local http won't work with Anthropic's connector.
    # When gitlab-mcp-server is running publicly via a tunnel (e.g. ngrok) on HTTPS:
    # e.g., https://your-ngrok-subdomain.ngrok.io/sse or /mcp
    gitlab_mcp_config = {
        "type": "url",
        "url": "https://placeholder.gitlab-mcp.example.com/sse", # IMPORTANT: Needs to be HTTPS
        "name": "gitlab_tool_server",
        # "authorization_token": "YOUR_MCP_SERVER_TOKEN_IF_NEEDED" # Optional
    }

    # Initialize components
    # Pass the MCP server config to LLMProvider
    llm_provider = LLMProvider(api_key="DUMMY_ANTHROPIC_API_KEY", mcp_server_configs=[gitlab_mcp_config])
    git_ops = GitOps(token="DUMMY_GIT_TOKEN") # Role of GitOps might change with MCP

    agent = CodingAgent(llm_client=llm_provider, git_client=git_ops)

    print("Coding Agent System initialized with MCP awareness.")

    # Example task that might use MCP tools via LLM
    gitlab_task_description = "What is the status of the latest pipeline on my GitLab project?"
    print(f"Main script starting GitLab task: {gitlab_task_description}")
    agent.process_task(gitlab_task_description, task_type="gitlab_query") # Added task_type for demo

    print("-" * 20)

    # Example task for general code generation (no MCP expected)
    coding_task_description = "Refactor the authentication module to use a new hashing library."
    print(f"Main script starting Coding task: {coding_task_description}")
    agent.process_task(coding_task_description, task_type="code_generation")


    print("Coding Agent task processing finished in main script.")

if __name__ == "__main__":
    main()
