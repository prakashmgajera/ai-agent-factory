
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

Below is an example of how to create a simple chat agent using this framework:

```python
from connectors.models.openai import OpenAIModelConnector
from connectors.models.gemini import GoogleGeminiModelConnector
from agents.simple_chat_agent import ChatAgent

system_prompt = (
    "You are a helpful assistant that provides weather information for any city or area. "
    "When the user asks about the weather, respond with the current weather details."
)

# Choose model connector
model = OpenAIModelConnector(api_key="your-openai-api-key")
# or
# model = GoogleGeminiModelConnector(api_key="your-gemini-api-key")

agent = ChatAgent(model_connector=model, system_prompt=system_prompt)
response = agent.chat("What's the weather in Paris?")
print(response)
```

## Getting Started

1. Clone the repository
2. Install dependencies (if any)
3. Add your API keys and configuration
4. Start building your agents!

## License

MIT
