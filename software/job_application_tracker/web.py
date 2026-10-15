from flask import Blueprint, redirect, render_template, request, url_for

from data.projects import get_project
from data.site import NAME, ROLE
from software.job_application_tracker.store import STATUSES, JobStore, default_db, seed_if_empty

bp = Blueprint(
    "jobs",
    __name__,
    url_prefix="/apps/jobs",
    template_folder="templates",
    static_folder="static",
)


def store() -> JobStore:
    jobs = JobStore(default_db())
    seed_if_empty(jobs)
    return jobs


@bp.get("/")
def home():
    jobs = store()
    project = get_project("job-application-tracker")
    return render_template(
        "jobs_app.html",
        name=NAME,
        role=ROLE,
        project=project,
        jobs=jobs.list_jobs(),
        counts=jobs.counts(),
        statuses=STATUSES,
        error=None,
    )


@bp.post("/")
def create():
    jobs = store()
    error = None
    try:
        jobs.add(
            company=request.form.get("company") or "",
            role=request.form.get("role") or "",
            status=request.form.get("status") or "Applied",
            url=request.form.get("url") or "",
            applied_on=request.form.get("applied_on") or None,
            notes=request.form.get("notes") or "",
        )
        return redirect(url_for("jobs.home"))
    except ValueError as exc:
        error = str(exc)
    project = get_project("job-application-tracker")
    return render_template(
        "jobs_app.html",
        name=NAME,
        role=ROLE,
        project=project,
        jobs=jobs.list_jobs(),
        counts=jobs.counts(),
        statuses=STATUSES,
        error=error,
    ), 400


@bp.post("/<int:job_id>/status")
def update_status(job_id: int):
    store().set_status(job_id, request.form.get("status") or "Applied")
    return redirect(url_for("jobs.home"))


@bp.post("/<int:job_id>/delete")
def remove(job_id: int):
    store().delete(job_id)
    return redirect(url_for("jobs.home"))
