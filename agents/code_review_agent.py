import subprocess
from agents.agent_base import Agent

class CodeReviewAgent(Agent):
    def review(self, code_path: str) -> str:
        try:
            result = subprocess.run(["semgrep", "--config", "auto", code_path], capture_output=True, text=True)
            return result.stdout if result.stdout else "No issues found."
        except Exception as e:
            return f"Error running Semgrep: {e}"