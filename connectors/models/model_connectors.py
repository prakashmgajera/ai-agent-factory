"""
Model connector factory and enum for selecting and instantiating model connectors.

Usage:
    from connectors.models.model_connectors import ModelChoice, ModelConnectorFactory
    model = ModelConnectorFactory.get_model_connector(ModelChoice.OPENAI)
"""
from enum import Enum

# Enum for model choices (should match usage in agents/simple_chat_agent.py)
class ModelChoice(Enum):
    OPENAI = "openai"
    GOOGLE_GEMINI = "google_gemini"
    HUGGINGFACE = "huggingface"


# Factory class to get model connector instance
class ModelConnectorFactory:
    @staticmethod
    def get_model_connector(model_choice, api_key=None):
        if model_choice == ModelChoice.OPENAI:
            from connectors.models.openai import OpenAIModelConnector
            return OpenAIModelConnector(api_key=api_key)
        elif model_choice == ModelChoice.GOOGLE_GEMINI:
            from connectors.models.google_gemini import GoogleGeminiModelConnector
            return GoogleGeminiModelConnector(api_key=api_key)
        elif model_choice == ModelChoice.HUGGINGFACE:
            from connectors.models.hf import HuggingFaceModelConnector
            return HuggingFaceModelConnector()
        else:
            raise ValueError(f"Unknown model choice: {model_choice}")
"""
Model connector interfaces and implementations for the agent framework.
This file imports and exposes the main connectors for convenience.
"""

from connectors.models.base import BaseModelConnector
from connectors.models.openai import OpenAIModelConnector
from connectors.models.google_gemini import GoogleGeminiModelConnector
from connectors.models.hf import HuggingFaceModelConnector
