"""
GoogleGeminiModelConnector: Example stub for Google Gemini model connector.

Reads the API key from an environment variable (GEMINI_API_KEY), .env file, or prompts the user if not provided.

Usage:
    from connectors.models.google_gemini import GoogleGeminiModelConnector
    model = GoogleGeminiModelConnector()
"""

import os
from connectors.models.base import BaseModelConnector

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional, but recommended for local development

# Import the official Google Gemini API client
try:
    import google.generativeai as genai
except ImportError:
    genai = None  # Will raise in __init__ if used


class GoogleGeminiModelConnector(BaseModelConnector):
    def __init__(self, api_key: str = None, model_name: str = "models/gemini-2.5-pro"):
        if genai is None:
            raise ImportError("google-generativeai package is required. Install with 'pip install google-generativeai'.")
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            try:
                self.api_key = input("Enter your Google Gemini API key: ").strip()
            except Exception:
                self.api_key = None
        if not self.api_key:
            raise ValueError("Gemini API key must be provided via argument, .env/GEMINI_API_KEY, or user input.")

        # Configure the Gemini API client
        genai.configure(api_key=self.api_key)
        # Use the latest supported Gemini model name. Check the Gemini API docs for updates.
        self.model_name = model_name
        self.model = genai.GenerativeModel(self.model_name)

    def generate(self, prompt: str) -> str:
        # Use the Gemini API to generate a response
        try:
            response = self.model.generate_content(prompt)
            # The response object has a 'text' attribute for the generated text
            return response.text
        except Exception as e:
            return f"[Gemini API error: {e}]"
