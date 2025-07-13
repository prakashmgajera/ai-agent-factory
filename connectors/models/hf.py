from .base import BaseModelConnector
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional, but recommended for local development


class HuggingFaceModelConnector(BaseModelConnector):
    """Connector for HuggingFace models using the HuggingFace Hub InferenceClient chat API (supports HF_TOKEN from env)."""
    def __init__(self, model_name: str = "HuggingFaceTB/SmolLM3-3B"):
        import os
        from huggingface_hub import InferenceClient
        self.model_name = model_name
        # Try to load from .env, fallback to system env
        self.api_key = os.environ.get("HF_TOKEN") or os.getenv("HF_TOKEN")
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=self.api_key,
        )

    def generate(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
            )
            return completion.choices[0].message["content"]
        except Exception as e:
            return f"[HuggingFace Chat API Exception] {e}"
