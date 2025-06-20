import json # For printing structured data if needed

class LLMProvider:
    def __init__(self, api_key, mcp_server_configs=None):
        self.api_key = api_key
        self.mcp_server_configs = mcp_server_configs if mcp_server_configs else []
        print(f"LLM Provider initialized. MCP Servers configured: {len(self.mcp_server_configs)}")

    def _prepare_anthropic_request(self, prompt_messages, max_tokens=1024):
        request_body = {
            "model": "claude-opus-4-20250514", # Example model
            "max_tokens": max_tokens,
            "messages": prompt_messages
        }
        if self.mcp_server_configs:
            request_body["mcp_servers"] = self.mcp_server_configs

        headers = {
            "content-type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01"
        }
        if self.mcp_server_configs: # Add beta header only if MCP servers are used
            headers["anthropic-beta"] = "mcp-client-2025-04-04"

        return "https://api.anthropic.com/v1/messages", headers, request_body

    def generate_text(self, prompt: str, task_type="general"):
        """
        Generates text using the LLM. If mcp_server_configs are provided
        and task_type suggests tool use, it will configure the request for MCP.
        For now, this method simulates the API call.
        """
        print(f"LLMProvider: Received prompt for '{task_type}': {prompt}")

        prompt_messages = [{"role": "user", "content": prompt}]

        api_url, headers, body = self._prepare_anthropic_request(prompt_messages)

        print(f"LLMProvider: Simulating API call to Anthropic.")
        print(f"LLMProvider: URL: {api_url}")
        print(f"LLMProvider: Headers: {json.dumps(headers)}")
        print(f"LLMProvider: Body: {json.dumps(body)}")

        if self.mcp_server_configs and task_type == "gitlab_query":
            print(f"LLMProvider: Simulating LLM used a GitLab MCP tool via connector.") # Added specific print
            simulated_llm_response_content = f"Accessed GitLab via MCP. The pipeline status is: SUCCESSFUL. (Simulated)"
            return simulated_llm_response_content
        elif self.mcp_server_configs and task_type == "github_query": # New block, correctly indented
            print(f"LLMProvider: Simulating LLM used a GitHub MCP tool via connector.")
            simulated_llm_response_content = f"Accessed GitHub via MCP. The README.md content is: '# GitHub Readme'. Issue 42 comments: ['Comment 1 on 42'] (Simulated)"
            return simulated_llm_response_content
        else:
            # Simulate a general text generation response
            print(f"LLMProvider: Simulating general LLM text generation.")
            return f"This is a simulated LLM response to: {prompt}"

    def generate_code(self, prompt: str) -> str:
        print(f"LLMProvider (generate_code): Generating code for prompt: {prompt}")
        return self.generate_text(f"Generate code for this task: {prompt}", task_type="code_generation")

    def review_code(self, code: str) -> str:
        print(f"LLMProvider (review_code): Reviewing code: {code}")
        return self.generate_text(f"Review this code: {code}", task_type="code_review")
