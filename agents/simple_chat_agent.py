

"""
A simple chat agent framework example.

- BaseModelConnector: Interface for model connectors
- OpenAIModelConnector: Example stub for OpenAI
- ChatAgent: Simple agent using a model connector and prompt

Usage example at the bottom.
"""


# Allow running as a script by adding project root to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Import ModelChoice enum and ModelConnectorFactory from model_connectors
from connectors.models.model_connectors import ModelChoice, ModelConnectorFactory

# Import BaseModelConnector for type hinting
from connectors.models.base import BaseModelConnector


# Import model connectors from the connectors/models directory

# No need to import individual connectors or base here

# Import pre-defined system prompts
from prompts.system_prompts import WEATHER_AGENT

class ChatAgent:
    def __init__(self, model_connector: BaseModelConnector, system_prompt: str):
        self.model_connector = model_connector
        self.system_prompt = system_prompt

    def chat(self, user_message: str) -> str:
        prompt = f"{self.system_prompt}\nUser: {user_message}\nAgent:"
        return self.model_connector.generate(prompt)

# Example usage:
if __name__ == "__main__":

    # Use a pre-defined system prompt for weather info
    system_prompt = WEATHER_AGENT

    # User can choose which model connector to use


    # Set model choice here
    model_choice = ModelChoice.GOOGLE_GEMINI  # Change to ModelChoice.GOOGLE_GEMINI to use Google Gemini

    # Use the factory to get the model connector
    model = ModelConnectorFactory.get_model_connector(model_choice)

    # Create the chat agent
    agent = ChatAgent(model_connector=model, system_prompt=system_prompt)
    # Simulate a chat
    user_input = "What's the most likely weather in San Francisco during summer?"
    response = agent.chat(user_input)
    print(response)
