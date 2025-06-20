class CodingAgent:
    def __init__(self, llm_client, git_client):
        self.llm_client = llm_client
        self.git_client = git_client # Role of git_client might change
        print("CodingAgent initialized with LLM and Git clients")

    def process_task(self, task_description: str, task_type: str = "general"):
        print(f"CodingAgent processing task ('{task_type}'): {task_description}")

        if task_type == "gitlab_query":
            # This task will go to the LLM, which might use MCP tools
            print("CodingAgent: Task is GitLab related, leveraging LLM with potential MCP tools.")
            llm_response = self.llm_client.generate_text(prompt=task_description, task_type="gitlab_query")
            print(f"CodingAgent: LLM response for GitLab query: {llm_response}")

        elif task_type == "github_query": # New block, correctly indented
            print("CodingAgent: Task is GitHub related, leveraging LLM with potential MCP tools.")
            llm_response = self.llm_client.generate_text(prompt=task_description, task_type="github_query")
            print(f"CodingAgent: LLM response for GitHub query: {llm_response}")

        elif task_type == "code_generation":
            print("CodingAgent: Task is code generation.")
            generated_code = self.llm_client.generate_code(prompt=task_description)
            print(f"Agent received generated code: \n{generated_code}")

            # Optional: Review code (could also be MCP enabled if a review tool exists)
            review_comments = self.llm_client.review_code(code=generated_code)
            print(f"Agent received review comments: \n{review_comments}")

            print("CodingAgent: (Simulated) Code generation and review complete. Git operations would follow.")

        else:
            print(f"CodingAgent: Unknown task type '{task_type}'. Treating as general prompt.")
            llm_response = self.llm_client.generate_text(prompt=task_description, task_type="general")
            print(f"CodingAgent: LLM response: {llm_response}")

        print(f"Task '{task_description}' processed by CodingAgent.")
        return "Task processing completed by CodingAgent."
