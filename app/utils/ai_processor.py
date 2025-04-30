# app/utils/ai_processor.py

import os
from werkzeug.datastructures import FileStorage
from openai import OpenAI

from app.utils.extract_text import extract_text

# Initialize the new OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_file: FileStorage) -> str:
    """
    1. Extract text from the uploaded resume (PDF/DOCX/TXT).
    2. Send it to OpenAI via the new client interface.
    3. Return the model's response as a string.
    """
    # 1) extract text
    text = extract_text(resume_file)

    # 2) build and send the chat-completion request
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert resume reviewer. "
                    "Provide bullet-point feedback on structure, clarity, strengths, "
                    "and areas for improvement."
                ),
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        temperature=0.3,
        max_tokens=800,
    )

    # 3) extract and return the assistant's message
    return response.choices[0].message.content