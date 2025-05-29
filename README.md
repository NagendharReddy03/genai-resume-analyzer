<p align="center">
 
<h1 align="center">🧠 GenAI Resume Analyzer</h1>

<p align="center">
  <em>AI-powered resume feedback system that helps recruiters and applicants evaluate resumes with precision and intelligence.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/NagendharReddy03/genai-resume-analyzer?style=for-the-badge"/>
  <img src="https://img.shields.io/github/last-commit/NagendharReddy03/genai-resume-analyzer?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/NagendharReddy03/genai-resume-analyzer?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge"/>
</p>

---

## 🚀 Features

- 🧠 AI-based resume feedback using OpenAI
- 📄 Resume parsing and keyword extraction
- 🔐 Secure login and registration system
- 📈 Real-time analysis via Swagger UI
- 🐳 Fully Dockerized with CI/CD support
- 🌐 FastAPI-powered backend with responsive design


---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python, FastAPI, SQLite           |
| AI Engine  | OpenAI GPT API                    |
| Frontend   | HTML, CSS, Jinja2                 |
| DevOps     | Docker, GitHub Actions, CI/CD     |
| Infra      | Docker Compose                    |

---

## ⚙️ Getting Started

```bash
# Clone repository
$ git clone https://github.com/NagendharReddy03/genai-resume-analyzer.git
$ cd genai-resume-analyzer

# Add your OpenAI key
$ cp .env.example .env
# Add OPENAI_API_KEY=your_api_key_here

# Build and run containers
$ docker-compose up --build

# Open in browser
Visit: http://localhost:8000
```

---

## 📂 Directory Structure

```bash
.
├── app
│   ├── main.py            # Entry point
│   ├── inference.py       # AI logic
│   └── train.py           # Model training
├── templates              # HTML templates
├── uploads                # Resume uploads
├── .github/workflows      # CI/CD
├── Dockerfile             # Docker config
├── docker-compose.yml     
└── .env.example           # Environment variables
```

---

## 🧪 Test Your API

> Visit [http://localhost:8000/docs](http://localhost:8000/docs) to access interactive Swagger UI and test your endpoints.

---

## 📌 TODO

- [ ] JD Matching System
- [ ] Role-based scoring
- [ ] Feedback PDF Export
- [ ] Resume template suggestions

---

## 🤝 Contributing

Contributions are always welcome! Please fork this repo and submit a pull request. Let’s build better hiring tools together. 💼

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍ Connect

- 👨‍💻 GitHub: [@NagendharReddy03](https://github.com/NagendharReddy03)
- 📫 Email: nagendharreddy.work@gmail.com
- 🌐 LinkedIn: [Connect with me](https://linkedin.com/in/NagendharReddy03)

---

<p align="center">
  <em>"Build smarter applications with the power of Generative AI."</em>
</p>
