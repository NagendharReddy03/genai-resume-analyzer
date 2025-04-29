import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_feedback(resume_text):
    try:
        prompt = f"""You are a professional HR assistant. Analyze the following resume and provide detailed, constructive feedback in bullet points. Highlight strengths, suggest improvements, and identify any missing sections:

Resume:
\"\"\"
{resume_text}
\"\"\"
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or 'gpt-4' if available
            messages=[
                {"role": "system", "content": "You are a helpful resume reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        feedback = response['choices'][0]['message']['content'].strip()
        return feedback

    except Exception as e:
        return f"Error generating feedback: {e}"