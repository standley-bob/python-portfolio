from pathlib import Path

from software.job_application_tracker.store import JobStore
from software.smart_file_organizer.organizer import apply, ensure_sandbox, plan


def test_organizer_plans_and_applies(tmp_path: Path):
    inbox = ensure_sandbox(tmp_path)
    moves = plan(inbox)
    assert any(m.folder == "Images" for m in moves)
    moved = apply(moves)
    assert moved >= 1
    assert plan(inbox) == []


def test_organizer_live_check(tmp_path: Path):
    from software.smart_file_organizer.organizer import live_check

    report = live_check(tmp_path / "check")
    assert report["ok"] is True
    assert report["moved"] == report["expected"]
    assert report["folders"]["Images"] == ["holiday.jpg"]
    assert report["folders"]["Code"] == ["demo.py"]


def test_job_store_roundtrip(tmp_path: Path):
    store = JobStore(tmp_path / "jobs.sqlite")
    job = store.add("Acme", "Python intern", "Applied")
    store.set_status(job.id, "Interview")
    rows = store.list_jobs()
    assert rows[0].company == "Acme"
    assert rows[0].status == "Interview"
    store.delete(job.id)
    assert store.list_jobs() == []
