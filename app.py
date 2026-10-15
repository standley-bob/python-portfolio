from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, redirect, render_template, request, url_for

from data.projects import all_projects, get_project
from data.site import ABOUT, EMAIL, HANDLE, INTRO, LOCATION, NAME, ROLE, SKILLS, SOCIALS, TAGLINE
from mailer import MailNotConfigured, mail_ready, send_contact
from software.ats_resume_builder.web import bp as ats_bp
from software.job_application_tracker.web import bp as jobs_bp
from software.movie_recommendation_finder.web import bp as movies_bp
from software.smart_file_organizer.web import bp as organizer_bp

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
MESSAGES = ROOT / "data" / "messages.json"
log = logging.getLogger(__name__)

app = Flask(__name__)
app.json.compact = False
app.register_blueprint(organizer_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(movies_bp)
app.register_blueprint(ats_bp)


@app.context_processor
def inject_site():
    return context()


def context(**extra):
    payload = {
        "name": NAME,
        "handle": HANDLE,
        "role": ROLE,
        "location": LOCATION,
        "email": EMAIL,
        "tagline": TAGLINE,
        "intro": INTRO,
        "about": ABOUT,
        "skills": SKILLS,
        "socials": SOCIALS,
        "projects": all_projects(),
        "year": datetime.now(timezone.utc).year,
    }
    payload.update(extra)
    return payload


@app.get("/")
def home():
    return render_template("index.html", **context())


@app.get("/projects/<slug>")
def project_detail(slug: str):
    project = get_project(slug)
    if not project:
        abort(404)
    return render_template("project.html", **context(project=project))


@app.get("/api/projects")
def api_projects():
    return jsonify({"projects": all_projects()})


@app.get("/api/health")
def api_health():
    return jsonify({"ok": True, "service": "python-portfolio", "mail": mail_ready()})


@app.post("/contact")
def contact():
    payload = {
        "name": (request.form.get("name") or "").strip(),
        "email": (request.form.get("email") or "").strip(),
        "message": (request.form.get("message") or "").strip(),
        "at": datetime.now(timezone.utc).isoformat(),
    }
    if not payload["name"] or not payload["email"] or not payload["message"]:
        return render_template("index.html", **context(contact_error="Please fill in every field.")), 400

    _store_message(payload)
    try:
        send_contact(payload)
    except MailNotConfigured:
        return render_template(
            "index.html",
            **context(
                contact_error="Mail is not set up yet. The note was saved on the server, not emailed."
            ),
        ), 503
    except Exception:
        log.exception("contact mail failed")
        return render_template(
            "index.html",
            **context(
                contact_error="Could not reach Gmail. The note was saved on the server."
            ),
        ), 502
    return redirect(url_for("home", sent=1) + "#contact")


def _store_message(payload: dict) -> None:
    MESSAGES.parent.mkdir(parents=True, exist_ok=True)
    inbox = []
    if MESSAGES.exists():
        inbox = json.loads(MESSAGES.read_text(encoding="utf-8"))
    inbox.append(payload)
    MESSAGES.write_text(json.dumps(inbox, indent=2), encoding="utf-8")


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html", **context()), 404


if __name__ == "__main__":
    app.run(debug=True)
