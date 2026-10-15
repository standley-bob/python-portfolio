from __future__ import annotations

from flask import Blueprint, Response, render_template, request

from data.projects import get_project
from data.site import NAME
from software.ats_resume_builder.builder import as_html, build_resume
from software.ats_resume_builder.extract import from_upload

bp = Blueprint(
    "ats",
    __name__,
    url_prefix="/apps/ats",
    template_folder="templates",
    static_folder="static",
)


def _inputs():
    designation = (request.form.get("designation") or "").strip()
    company = (request.form.get("company") or "").strip()
    jd = (request.form.get("jd") or "").strip()
    resume = (request.form.get("resume") or "").strip()
    upload = request.files.get("resume_file")
    if upload and upload.filename:
        resume = from_upload(upload.filename, upload.read()) or resume
    include = request.form.get("include_suggested") == "on"
    return designation, company, jd, resume, include


@bp.get("/")
def home():
    return render_template(
        "ats_app.html",
        name=NAME,
        project=get_project("ats-resume-builder"),
        result=None,
        error=None,
        form={},
    )


@bp.post("/")
def analyze():
    designation, company, jd, resume, include = _inputs()
    form = {
        "designation": designation,
        "company": company,
        "jd": jd,
        "resume": resume,
        "include_suggested": include,
    }
    if not designation or not company or not jd or not resume:
        return render_template(
            "ats_app.html",
            project=get_project("ats-resume-builder"),
            result=None,
            error="Add designation, company, job description, and a resume (paste or file).",
            form=form,
        ), 400
    result = build_resume(resume, jd, designation, company, include_suggested=include)
    return render_template(
        "ats_app.html",
        project=get_project("ats-resume-builder"),
        result=result,
        error=None,
        form=form,
    )


@bp.post("/download")
def download():
    fmt = (request.form.get("fmt") or "txt").lower()
    designation, company, jd, resume, include = _inputs()
    if not resume or not jd:
        return "Nothing to download.", 400
    built = build_resume(resume, jd, designation, company, include_suggested=include)
    slug = f"{designation}_{company}_resume".replace(" ", "_")
    if fmt == "html":
        payload = as_html(built["text"], f"{designation} resume")
        return Response(
            payload,
            mimetype="text/html",
            headers={"Content-Disposition": f"attachment; filename={slug}.html"},
        )
    if fmt == "docx":
        from docx import Document
        import io

        doc = Document()
        for line in built["text"].splitlines():
            doc.add_paragraph(line)
        buf = io.BytesIO()
        doc.save(buf)
        return Response(
            buf.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename={slug}.docx"},
        )
    return Response(
        built["text"],
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={slug}.txt"},
    )
