from flask import Blueprint, render_template, request, jsonify
from app.utils.resume_parser import parse_resume
from app.utils.ai_analysis import analyze_resume
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
            
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        if file and allowed_file(file.filename):
            text_content = parse_resume(file)
            analysis = analyze_resume(text_content)
            return jsonify(analysis)
            
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf', 'docx', 'txt'}