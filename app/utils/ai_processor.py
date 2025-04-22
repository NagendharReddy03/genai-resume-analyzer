from sentence_transformers import SentenceTransformer
import numpy as np

class ResumeAnalyzer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.skill_keywords = {
            'Programming': ['Python', 'Java', 'C++', 'JavaScript'],
            'DevOps': ['Docker', 'AWS', 'Kubernetes', 'CI/CD'],
            'Databases': ['SQL', 'PostgreSQL', 'MongoDB'],
            'AI/ML': ['PyTorch', 'TensorFlow', 'NLP', 'Computer Vision']
        }

    def extract_text(self, file):
        # Existing extraction logic
        pass

    def analyze_resume(self, text, job_desc=None):
        resume_embed = self.model.encode(text)
        results = {
            'skills': self._extract_skills(text),
            'feedback': []
        }
        
        if job_desc:
            jd_embed = self.model.encode(job_desc)
            results['score'] = self._calculate_score(resume_embed, jd_embed)
            results['feedback'] = self._generate_feedback(text, job_desc)
            
        return results

    def _calculate_score(self, resume_embed, jd_embed):
        return float(np.dot(resume_embed, jd_embed.T).item() * 100)
    
    def _extract_skills(self, text):
        return {category: [skill for skill in skills 
                if skill.lower() in text.lower()]
                for category, skills in self.skill_keywords.items()}
    
    def _generate_feedback(self, text, job_desc):
        feedback = []
        if 'education' not in text.lower():
            feedback.append("Consider adding education section")
        if 'experience' not in text.lower():
            feedback.append("Add more details about work experience")
        return feedback