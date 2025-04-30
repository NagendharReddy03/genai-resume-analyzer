# app/main/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.datastructures import FileStorage

from app.main.forms import UploadForm
from app.utils.ai_processor import analyze_resume

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    # Look in app/templates/main/index.html
    return render_template("main/index.html", title="Home")


@main_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file: FileStorage = form.resume.data
        feedback = analyze_resume(form.resume.data)
        # Render results.html under templates/main
        return render_template("main/results.html", title="Results", feedback=feedback)

    return render_template("main/upload.html", title="Upload Resume", form=form)