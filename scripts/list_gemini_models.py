import google.generativeai as genai

genai.configure()

# List all available models and their supported generation methods
for model in genai.list_models():
    print(f"Model: {model.name}, Supported methods: {model.supported_generation_methods}")
