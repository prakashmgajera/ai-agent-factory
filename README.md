
# ai-agent-factory

ai-agent-factory is a modular framework for building AI agents with support for pluggable model connectors, prompt templates, knowledge base (RAG), and cloud service connectors.

## Features

- **Model Connectors:** Easily define and use connectors for different LLM providers (e.g., OpenAI, Google Gemini).
- **Prompt Templates:** Organize and reuse prompt templates for agent instructions.
- **Knowledge Base (RAG):** Integrate vector embeddings and retrieval-augmented generation.
- **Cloud Service Connectors:** Connect agents to cloud services like Google Drive, AWS, etc.
- **Extensible:** Add new connectors, agents, and features as needed.

## Directory Structure

```
agents/                  # Agent definitions and logic
connectors/
  models/                # Model connectors (OpenAI, Gemini, etc.)
  cloud_services/        # Cloud service connectors
prompts/                 # Prompt templates
knowledge_base/
  embeddings/            # Vector embedding logic and storage
  retrievers/            # RAG retrievers and knowledge base management
tests/                   # Unit and integration tests
scripts/                 # Utility scripts
config/                  # Configuration files
```


## Example: Simple Chat Agent

Below is an example of how to create a simple chat agent using this framework, following the current structure:

```python
# Import the required classes and enums
from connectors.models.model_connectors import ModelChoice, ModelConnectorFactory
from prompts.system_prompts import WEATHER_AGENT
from agents.simple_chat_agent import ChatAgent

# Use a pre-defined system prompt for weather info
system_prompt = WEATHER_AGENT

# Set model choice (choose from ModelChoice.OPENAI or ModelChoice.GOOGLE_GEMINI)
model_choice = ModelChoice.OPENAI  # or ModelChoice.GOOGLE_GEMINI

# Use the factory to get the model connector (API keys/configuration should be set in your environment or config)
model = ModelConnectorFactory.get_model_connector(model_choice)

# Create the chat agent
agent = ChatAgent(model_connector=model, system_prompt=system_prompt)

# Simulate a chat
user_input = "What's the weather in San Francisco?"
response = agent.chat(user_input)
print(response)
```

## Getting Started

1. Clone the repository
2. Install dependencies (if any)
3. Add your API keys and configuration (see `config/` or environment variables as required by your model connector)
4. Start building your agents!

## License

MIT
