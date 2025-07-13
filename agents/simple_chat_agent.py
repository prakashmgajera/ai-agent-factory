"""
A simple chat agent framework example.

- BaseModelConnector: Interface for model connectors
- OpenAIModelConnector: Example stub for OpenAI
- ChatAgent: Simple agent using a model connector and prompt

Usage example at the bottom.
"""

# Import model connectors from the connectors/models directory
from connectors.models.base import BaseModelConnector
from connectors.models.openai import OpenAIModelConnector
from connectors.models.google_gemini import GoogleGeminiModelConnector

class ChatAgent:
    def __init__(self, model_connector: BaseModelConnector, system_prompt: str):
        self.model_connector = model_connector
        self.system_prompt = system_prompt

    def chat(self, user_message: str) -> str:
        prompt = f"{self.system_prompt}\nUser: {user_message}\nAgent:"
        return self.model_connector.generate(prompt)

# Example usage:
if __name__ == "__main__":
    # Define a system prompt for weather info
    system_prompt = (
        "You are a helpful assistant that provides weather information for any city or area. "
        "When the user asks about the weather, respond with the current weather details."
    )

    # User can choose which model connector to use
    model_choice = "openai"  # Change to "gemini" to use Google Gemini

    if model_choice == "openai":
        model = OpenAIModelConnector(api_key="your-openai-api-key")
    elif model_choice == "gemini":
        model = GoogleGeminiModelConnector(api_key="your-gemini-api-key")
    else:
        raise ValueError("Unknown model choice")

    # Create the chat agent
    agent = ChatAgent(model_connector=model, system_prompt=system_prompt)
    # Simulate a chat
    user_input = "What's the weather in Paris?"
    response = agent.chat(user_input)
    print(response)
