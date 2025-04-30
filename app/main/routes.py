from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.datastructures import FileStorage
from app.utils.ai_processor import analyze_resume  # wherever your AI logic lives

main_bp = Blueprint("main", __name__, template_folder="templates/main")

@main_bp.route("/")
def index():
    # home page with upload button
    return render_template("index.html", title="Home")


@main_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        file: FileStorage = request.files.get("resume")
        if not file:
            flash("Please choose a file to upload.", "warning")
            return redirect(url_for("main.upload"))

        # run your AI analysis on the file storage object
        feedback = analyze_resume(file)
        return render_template("results.html", title="Results", feedback=feedback)

    # GET → show the upload form
    return render_template("upload.html", title="Upload Resume")