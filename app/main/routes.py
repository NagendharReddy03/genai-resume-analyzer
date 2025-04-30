# app/main/routes.py
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.utils.ai_processor import analyze_resume

main_bp = Blueprint("main", __name__, template_folder="templates/main")

@main_bp.route("/")
def index():
    return render_template("main/index.html", title="Home")

@main_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        f = request.files.get("resume")
        if not f:
            flash("No file selected", "warning")
            return redirect(url_for("main.upload"))

        filename = secure_filename(f.filename)
        save_path = os.path.join(current_app.instance_path, filename)
        f.save(save_path)

        # call your AI processor
        result = analyze_resume(f)
        flash(result, "info")
        return redirect(url_for("main.index"))

    return render_template("main/upload.html", title="Upload Resume")
