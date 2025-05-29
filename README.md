GenAI Resume Analyzer 🧠📄

A powerful, AI-driven resume screening tool that helps recruiters and job seekers by automating resume analysis, extracting key information, and generating insightful feedback using Generative AI.

🔍 Project Overview

GenAI Resume Analyzer is a modern web application built to:
	•	Parse and extract structured data from resumes
	•	Use NLP and Generative AI to assess resumes
	•	Offer intelligent feedback on strengths, keywords, and improvement areas
	•	Streamline the resume screening process for hiring teams

🚀 Features
	•	✅ Resume upload and parsing
	•	🧠 AI-generated resume feedback using OpenAI API
	•	📊 Keyword extraction and job fit insights
	•	🔐 Secure login & registration
	•	📦 Dockerized for easy deployment
	•	🌐 CI/CD-ready with GitHub Actions and Docker Compose

🛠️ Tech Stack
Technology
Purpose
Python
Core backend logic and scripts
FastAPI
RESTful API for resume analysis
OpenAI API
Generative feedback engine
Docker
Containerization
GitHub Actions
CI/CD workflow automation
SQLite
Lightweight database integration
HTML/CSS/JS
User interface

🧱 Project Structure
genai-resume-analyzer/
├── app/
│   ├── main.py
│   ├── inference.py
│   └── train.py
├── templates/
├── uploads/
├── .github/workflows/docker-ci.yml
├── docker-compose.yml
├── Dockerfile
└── README.md

⚙️ Setup Instructions
	1.	Clone the repository: git clone https://github.com/NagendharReddy03/genai-resume-analyzer.git
cd genai-resume-analyzer
  2.  Create a .env file and add your OpenAI API Key: OPENAI_API_KEY=your_openai_key_here
  3.	Build and run with Docker Compose: docker-compose up --build
  4.	Access the app: Visit http://localhost:8000 in your browser.
  
🧪 Test the Endpoint
	•	Visit: http://localhost:8000/docs
	•	Try the /analyze endpoint with a test resume input.

📈 Future Enhancements
	•	Job description matching
	•	Role-based feedback and scoring
	•	Integration with ATS platforms
	•	Advanced visual analytics

📄 License

This project is open-source and available under the MIT License. 

Contributions welcome! If you have ideas or find bugs, feel free to open an issue or submit a pull request.
