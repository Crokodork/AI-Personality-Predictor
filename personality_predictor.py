import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def predict_personality(text):
    prompt = f"Based on the following text, provide an analysis of the writer's personality traits:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a psychologist who analyzes personality based on text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    text = input("Enter text for personality analysis: ")
    analysis = predict_personality(text)
    print("\nPersonality Analysis:\n", analysis)
