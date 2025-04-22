import os
import openai

# Load OpenAI key from environment (or set directly)
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_and_analyze_text(file_path):
    try:
        # Read uploaded file content
        with open(file_path, 'r', encoding='utf-8') as f:
            resume_text = f.read()

        # Call OpenAI API for feedback
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a resume reviewer AI. Provide professional, constructive feedback on resumes."
                },
                {
                    "role": "user",
                    "content": f"Here is the resume:\n\n{resume_text}\n\nGive feedback."
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        ai_feedback = response['choices'][0]['message']['content']
        return ai_feedback

    except Exception as e:
        return f"Error during AI analysis: {str(e)}"