# GenAI Resume Analyzer 🤖

AI-powered resume analysis system with DevOps integration

![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDZ4Z3V5eGx5ZGN0M3FhZ3R6emVjZ2N4bGJ6YjB1bGxqZ3JmOXlxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7qE1YN7aBOFEPyow/giphy.gif)

## Features
- **GenAI Analysis**: Resume scoring, skill matching, feedback
- **File Support**: PDF, DOCX, TXT
- **DevOps Ready**: Docker + GitHub Actions CI/CD
- **Web Interface**: Simple UI for uploads

## Quick Start
```bash
git clone https://github.com/yourusername/genai-resume-analyzer
cd genai-resume-analyzer

# Build and run
docker build -t genai-analyzer .
docker run -p 5000:5000 genai-analyzer

