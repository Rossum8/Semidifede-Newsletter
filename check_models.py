import google.generativeai as genai
import os

# Configure Gemini API using environment variables
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not found. Please set it first.")
    exit(1)

genai.configure(api_key=api_key)

print("Fetching available models for your API key...")
print("-" * 40)

# List all models that support the generateContent method
available_models = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            print(m.name)
    print("-" * 40)
    print(f"Total models available for text generation: {len(available_models)}")
except Exception as e:
    print(f"An error occurred while fetching models: {e}")
