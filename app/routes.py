import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from app.utils.ai_processor import analyze_resume

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/analyze", methods=("GET", "POST"))
@login_required
def analyze():
    summary = None
    if request.method == "POST":
        file = request.files.get("resume")
        if not file:
            flash("Please upload a PDF resume.", "warning")
        else:
            summary = analyze_resume(file)
    return render_template("analyze.html", summary=summary)