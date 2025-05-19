import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL", "https://openrouter.ai/api/v1")
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4")

client = OpenAI(
    base_url=OPENROUTER_API_URL,
    api_key=OPENROUTER_API_KEY,
)

def chat_with_llm(system_prompt: str, user_prompt: str, model: str = None) -> str:
    model = model or DEFAULT_MODEL
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        }
    )
    return response.choices[0].message.content