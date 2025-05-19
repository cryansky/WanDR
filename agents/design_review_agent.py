from agents.agent_base import Agent
from llm_client import chat_with_llm
from util import load_prompt_template, extract_text_from_pdf

class DesignReviewAgent(Agent):
    def review(self, dr_document: str) -> str:
        system_prompt = load_prompt_template("prompts/design_review_prompt.md")
        design_description = extract_text_from_pdf(dr_document)
        return chat_with_llm(system_prompt, design_description)