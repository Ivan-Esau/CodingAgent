import json
import os
import anthropic # Import the official SDK

class LLMProvider:
    def __init__(self, api_key=None, mcp_server_configs=None):
        self.api_key = api_key if api_key else os.getenv("ANTHROPIC_API_KEY")
        self.mcp_server_configs = mcp_server_configs if mcp_server_configs else []

        if self.api_key and self.api_key != "DUMMY_ANTHROPIC_API_KEY" and self.api_key.strip() != "":
            try:
                self.anthropic_client = anthropic.Anthropic(api_key=self.api_key)
                self.simulation_mode = False
                print(f"LLM Provider initialized with Anthropic SDK client. MCP Servers configured: {len(self.mcp_server_configs)}")
            except Exception as e: # Catch potential errors during client init e.g. bad API key format for some libs
                print(f"LLM Provider: Error initializing Anthropic client: {e}. Falling back to SIMULATION MODE.")
                self.anthropic_client = None
                self.simulation_mode = True
        else:
            self.anthropic_client = None
            self.simulation_mode = True
            print(f"LLM Provider initialized in SIMULATION MODE (No/Dummy API Key). MCP Servers configured: {len(self.mcp_server_configs)}")

    def generate_text(self, prompt: str, task_type="general"):
        print(f"LLMProvider: Received prompt for '{task_type}': {prompt}")

        prompt_messages = [{"role": "user", "content": prompt}]

        # Base request parameters for the SDK
        sdk_request_params = {
            "model": "claude-3-opus-20240229",
            "max_tokens": 1024,
            "messages": prompt_messages
        }

        # For passing to json.dumps for logging
        log_request_params = sdk_request_params.copy()

        extra_kwargs = {}
        if self.mcp_server_configs:
            # As per SDK behavior, custom/beta parameters often go into extra_body or extra_headers
            extra_kwargs["extra_body"] = {"mcp_servers": self.mcp_server_configs}
            extra_kwargs["extra_headers"] = {"anthropic-beta": "mcp-client-2025-04-04"}

            # For logging purposes, show what would be sent
            log_request_params["mcp_servers"] = self.mcp_server_configs # For the log
            log_request_params["anthropic-beta-header-simulated"] = "mcp-client-2025-04-04" # For the log


        print(f"LLMProvider: Preparing to call Anthropic SDK with parameters (logged representation):")
        try:
            print(json.dumps(log_request_params, indent=2))
        except TypeError:
             print(str(log_request_params))


        if self.simulation_mode or not self.anthropic_client:
            print("LLMProvider: SIMULATION MODE - Not making actual API call.")
            if self.mcp_server_configs and task_type == "gitlab_query":
                simulated_llm_response_content = f"Accessed GitLab via MCP. The pipeline status is: SUCCESSFUL. (Simulated)"
                print(f"LLMProvider: Simulating LLM used a GitLab MCP tool.")
                return simulated_llm_response_content
            elif self.mcp_server_configs and task_type == "github_query":
                print(f"LLMProvider: Simulating LLM used a GitHub MCP tool.")
                simulated_llm_response_content = f"Accessed GitHub via MCP. README.md: '# GitHub Readme'. Issue 42: ['Comment 1']. (Simulated)"
                return simulated_llm_response_content
            else:
                print(f"LLMProvider: Simulating general LLM text generation.")
                return f"This is a simulated LLM response to: {prompt}"
        else:
            print("LLMProvider: Attempting ACTUAL API call to Anthropic...")
            try:
                # Combine base parameters with any mcp-specific extras
                final_sdk_params = {**sdk_request_params, **extra_kwargs}

                response = self.anthropic_client.messages.create(**final_sdk_params)

                final_text_response = ""
                if response.content and isinstance(response.content, list) and len(response.content) > 0:
                    for block in response.content:
                        if hasattr(block, 'text'):
                            final_text_response += block.text + "\n"

                print("LLMProvider: Received response from Anthropic API.")
                return final_text_response.strip() if final_text_response else "[No text content in response]"

            except anthropic.APIConnectionError as e:
                print(f"LLMProvider: Anthropic API connection error: {e.__cause__}")
                return f"[ERROR: API Connection Error - {e.__cause__}]"
            except anthropic.RateLimitError as e:
                print(f"LLMProvider: Anthropic API rate limit exceeded: {e.status_code}")
                return f"[ERROR: API Rate Limit Error - {e.status_code}]"
            except anthropic.APIStatusError as e:
                print(f"LLMProvider: Anthropic API status error: {e.status_code} - {e.response}")
                return f"[ERROR: API Status Error - {e.status_code} - {e.message}]"
            except Exception as e:
                print(f"LLMProvider: An unexpected error occurred during API call: {e}")
                return f"[ERROR: Unexpected error during API call - {str(e)}]"

    def generate_code(self, prompt: str) -> str:
        print(f"LLMProvider (generate_code): Simulating code generation for prompt: {prompt}")
        return self.generate_text(f"Generate code for this task: {prompt}", task_type="code_generation")

    def review_code(self, code: str) -> str:
        print(f"LLMProvider (review_code): Simulating code review: {code}")
        return self.generate_text(f"Review this code: {code}", task_type="code_review")
