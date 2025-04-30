import openai
import os

def analyze_resume(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "Analyze this resume and provide feedback:"
                       "1. Key strengths\n2. Areas for improvement\n"
                       "3. Skill gap analysis\n4. ATS optimization tips"
        }, {
            "role": "user",
            "content": text
        }]
    )
    
    return response.choices[0].message.content