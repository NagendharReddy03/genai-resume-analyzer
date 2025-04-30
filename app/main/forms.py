# app/main/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadForm(FlaskForm):
    resume = FileField(
        "Select Resume File (PDF/DOCX/TXT)",
        validators=[FileAllowed(["pdf", "docx", "txt"], "Only PDF, DOCX or TXT files allowed")]
    )
    submit = SubmitField("Analyze")