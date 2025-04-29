# app/utils/ai_processor.py
import os
import openai
from werkzeug.datastructures import FileStorage

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(pdf_file: FileStorage) -> str:
    # ... your existing logic ...
    result = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[{ "role": "system", "content": "Analyze this resume..." },
                { "role": "user",   "content": pdf_text }]
    )
    return result.choices[0].message.content