from mcp.server.fastmcp import FastMCP
import json # For pretty printing dicts in mock responses

# Create an MCP server instance for GitHub
github_mcp = FastMCP(name="GitHubMCPServer", title="GitHub MCP Server - Enhanced with Resources")

# --- Tools ---

@github_mcp.tool(title="Get Issue Information")
def get_issue_info(issue_id: int) -> str:
    """
    Retrieves basic information about a GitHub issue given its ID.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'get_issue_info' called for issue_id: {issue_id}")
    return json.dumps({
        "issue_id": issue_id,
        "title": f"Placeholder Title for Issue {issue_id}",
        "author": "user_placeholder",
        "status": "open",
        "url": f"https://github.example.com/owner/repo/issues/{issue_id}"
    })

@github_mcp.tool(title="List Repository Files")
def list_repo_files(path: str = "") -> list[str]:
    """
    Lists files in the GitHub repository at a given path.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'list_repo_files' called for path: '{path}'")
    if path == "" or path == "/":
        return ["README.md", "src/", "LICENSE", ".gitignore", "(Placeholder files at root)"]
    elif path == "src" or path == "src/":
        return ["main.py", "utils.py", "github_mcp_server/", "(Placeholder files in src/)"]
    else:
        return ["(Placeholder: No files found or path not recognized)"]

@github_mcp.tool(title="Get File Content")
def get_file_content(path: str) -> str:
    """
    Retrieves the content of a specific file from the GitHub repository.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'get_file_content' called for path: '{path}'")
    if path == "README.md":
        return "# Placeholder README Content\nThis is a dummy README file."
    elif path == "src/main.py":
        return "print('Hello from src/main.py placeholder!')"
    else:
        return f"// Placeholder content for {path}\nFile not found or content not specified in placeholder."

@github_mcp.tool(title="Create Branch")
def create_branch(branch_name: str, base_branch: str = "main") -> str:
    """
    Creates a new branch in the GitHub repository.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'create_branch' called. Branch: '{branch_name}', Base: '{base_branch}'")
    return json.dumps({
        "branch_name": branch_name,
        "base_branch": base_branch,
        "status": "success",
        "url": f"https://github.example.com/owner/repo/tree/{branch_name}"
    })

@github_mcp.tool(title="Create Commit")
def create_commit(branch_name: str, commit_message: str, file_changes: list) -> str:
    """
    Creates a new commit on a specified branch with the given file changes.
    'file_changes' is a list of dicts, e.g., [{'path': 'file.py', 'content': 'new content'}].
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'create_commit' called. Branch: '{branch_name}', Message: '{commit_message}'")
    print(f"File changes: {file_changes}")
    return json.dumps({
        "commit_sha": "ph_sha_" + branch_name.replace("/", "_") + "_12345abc",
        "branch": branch_name,
        "message": commit_message,
        "status": "success",
        "url": f"https://github.example.com/owner/repo/commit/ph_sha_{branch_name.replace('/', '_')}_12345abc"
    })

@github_mcp.tool(title="Create Pull Request")
def create_pull_request(title: str, body: str, head_branch: str, base_branch: str) -> str:
    """
    Creates a new pull request in the GitHub repository.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'create_pull_request' called. Title: '{title}', Head: '{head_branch}', Base: '{base_branch}'")
    return json.dumps({
        "pr_number": 123, # Placeholder PR number
        "title": title,
        "head_branch": head_branch,
        "base_branch": base_branch,
        "status": "open",
        "url": f"https://github.example.com/owner/repo/pull/123"
    })

@github_mcp.tool(title="Get Issue Comments")
def get_issue_comments(issue_id: int) -> str:
    """
    Retrieves comments for a specific GitHub issue.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Tool 'get_issue_comments' called for issue_id: {issue_id}")
    comments = [
        {"user": "commenter_a", "body": f"This is the first placeholder comment for issue {issue_id}."},
        {"user": "commenter_b", "body": f"Another insightful comment here for issue {issue_id}."}
    ]
    if issue_id == 42: # Special case for testing
        comments.append({"user": "special_user", "body": "This is a special comment for issue 42!"})
    return json.dumps(comments)

# --- Resources ---

@github_mcp.resource(uri="github://{owner}/{repo}/issues/{issue_id:int}", title="GitHub Issue Resource")
def get_issue_resource(owner: str, repo: str, issue_id: int) -> dict:
    """
    Provides a specific GitHub issue as an MCP resource.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Resource 'github://{owner}/{repo}/issues/{issue_id}' requested.")
    return {
        "id": issue_id,
        "title": f"Placeholder Issue Title for {issue_id} from resource",
        "body": "This is a placeholder body for the issue, fetched via resource.",
        "state": "open",
        "labels": ["bug", "placeholder", "resource-fetched"],
        "url": f"https://github.com/{owner}/{repo}/issues/{issue_id}",
        "owner": owner,
        "repo": repo
    }

@github_mcp.resource(uri="github://{owner}/{repo}/files/{filepath:path}", title="GitHub File Content Resource")
def get_file_content_resource(owner: str, repo: str, filepath: str) -> dict:
    """
    Provides the content of a specific file from GitHub as an MCP resource.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Resource 'github://{owner}/{repo}/files/{filepath}' requested.")
    content = f"# Placeholder content for {filepath} in {owner}/{repo}\n"
    if filepath == "README.md":
        content += "This is a dummy README file obtained via resource."
    elif filepath == "src/main.py":
        content += "print('Hello from src/main.py placeholder, obtained via resource!')"
    else:
        content += "File content not specifically defined in placeholder for this path."
    return {
        "owner": owner,
        "repo": repo,
        "path": filepath,
        "content": content,
        "encoding": "utf-8" # Assuming utf-8
    }

@github_mcp.resource(uri="github://{owner}/{repo}/pulls/{pr_id:int}", title="GitHub Pull Request Resource")
def get_pull_request_resource(owner: str, repo: str, pr_id: int) -> dict:
    """
    Provides details of a specific GitHub Pull Request as an MCP resource.
    (Placeholder implementation)
    """
    print(f"GitHubMCPServer: Resource 'github://{owner}/{repo}/pulls/{pr_id}' requested.")
    return {
        "owner": owner,
        "repo": repo,
        "pr_id": pr_id,
        "title": f"Placeholder PR Title for #{pr_id}",
        "body": f"This is a placeholder body for pull request #{pr_id} in {owner}/{repo}.",
        "state": "open", # or "closed", "merged"
        "author": "pr_author_placeholder",
        "source_branch": f"feature/branch-{pr_id}",
        "target_branch": "main",
        "url": f"https://github.com/{owner}/{repo}/pull/{pr_id}",
        "created_at": "2023-01-01T10:00:00Z", # ISO 8601 format
        "updated_at": "2023-01-01T10:05:00Z"
    }

# --- Comments for running (can be kept at the end) ---
# To run this server (for development/testing with MCP inspector):
# Ensure 'mcp' is installed (e.g., via uv pip install "mcp[cli]")
# Then, from the root of the 'coding_agent' project:
# export PYTHONPATH=\$PYTHONPATH:./src
# uv run mcp dev src/github_mcp_server/server.py

# if __name__ == "__main__":
#     print("Starting GitHub MCP Server (Enhanced with Resources)...")
#     # github_mcp.run(transport="streamable-http", host="127.0.0.1", port=8001) # Example
