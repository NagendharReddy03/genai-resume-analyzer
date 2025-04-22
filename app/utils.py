from PyPDF2 import PdfReader
from docx import Document

def extract_text(file):
    """Extract text from PDF/DOCX/TXT files"""
    if file.filename.endswith('.pdf'):
        reader = PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)
    elif file.filename.endswith('.docx'):
        doc = Document(file)
        return " ".join(para.text for para in doc.paragraphs)
    else:
        return file.read().decode()

def calculate_score(resume_embed, jd_embed):
    """AI-powered matching score (0-100)"""
    if jd_embed is None:
        return None
    similarity = (resume_embed @ jd_embed.T).item()
    return min(100, max(0, int(similarity * 100)))

def generate_feedback(text):
    """GenAI-style feedback"""
    feedback = []
    if len(text) < 300:
        feedback.append("📉 Resume seems too short - add more details!")
    if 'education' not in text.lower():
        feedback.append("🎓 Consider adding education section")
    return feedback or ["✅ Strong resume! Good job!"]