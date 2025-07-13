"""
Abstract base class for all model connectors.

Usage:
    class MyConnector(BaseModelConnector):
        ...
"""
"""
BaseModelConnector: Abstract base class for all model connectors.
"""
from abc import ABC, abstractmethod

class BaseModelConnector(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the model given a prompt."""
        pass
