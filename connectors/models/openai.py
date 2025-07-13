"""
OpenAIModelConnector: Example stub for OpenAI model connector.

Reads the API key from an environment variable (OPENAI_API_KEY), .env file, or prompts the user if not provided.

Usage:
    from connectors.models.openai import OpenAIModelConnector
    model = OpenAIModelConnector()
"""
import os
from typing import Optional
try:
    from connectors.models.base import BaseModelConnector
except ImportError:
    try:
        from .base import BaseModelConnector
    except ImportError:
        raise ImportError("Cannot import BaseModelConnector. Please run as a module or ensure PYTHONPATH is set correctly.")

try:
    # Optional: load environment variables from .env if available
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is not installed; .env support skipped


class OpenAIModelConnector(BaseModelConnector):
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        import openai
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            try:
                self.api_key = input("Enter your OpenAI API key: ").strip()
            except Exception:
                self.api_key = None
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided via argument, .env/OPENAI_API_KEY, or user input.")
        openai.api_key = self.api_key
        self.openai = openai
        self.model = model

    def generate(self, prompt: str) -> str:
        # Actual call to OpenAI ChatCompletion API (openai>=1.0.0)
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response.choices[0].message.content
            if content is not None:
                return content.strip()
            else:
                return "[OpenAI API returned no content]"
        except Exception as e:
            return f"[OpenAI API error: {e}]"
