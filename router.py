from agents.code_review_agent import CodeReviewAgent
from agents.design_review_agent import DesignReviewAgent

class OpenRouter:
    def __init__(self):
        self.agents = {
            "code_review": CodeReviewAgent(),
            "design_review": DesignReviewAgent(),
        }

    def route(self, task_type: str, input_data: str) -> str:
        agent = self.agents.get(task_type)
        if not agent:
            return f"No agent found for task type: {task_type}"
        return agent.review(input_data)

