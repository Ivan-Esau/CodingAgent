from core import CodingAgent # Changed from 'from core import Core'
from llm import LLMProvider
from git_operations import GitOps
# We will load configuration later

def main():
    print("Initializing Coding Agent System...")

    # Initialize components
    llm_provider = LLMProvider(api_key="DUMMY_LLM_API_KEY")
    git_ops = GitOps(token="DUMMY_GIT_TOKEN")

    # Initialize CodingAgent with dependencies
    agent = CodingAgent(llm_client=llm_provider, git_client=git_ops)

    print("Coding Agent System initialized.")

    # Example task
    task_description = "Refactor the authentication module using CodingAgent."
    print(f"Main script starting task: {task_description}")

    # Agent processes the task
    agent.process_task(task_description)

    print("Coding Agent task processing finished in main script.")

if __name__ == "__main__":
    main()
