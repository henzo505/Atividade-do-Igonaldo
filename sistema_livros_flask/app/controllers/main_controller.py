from flask import Blueprint, render_template, session
from app.utils.auth_middleware import login_required
main_bp=Blueprint("main", __name__)
@main_bp.route("/")
@login_required
def home():
    return render_template("home.html", usuario=session.get("username"))
