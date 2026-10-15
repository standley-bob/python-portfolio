from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import sqlite3

STATUSES = ("Wishlist", "Applied", "Interview", "Offer", "Rejected")


@dataclass
class Job:
    id: int
    company: str
    role: str
    status: str
    url: str
    applied_on: str
    notes: str

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "company": self.company,
            "role": self.role,
            "status": self.status,
            "url": self.url,
            "applied_on": self.applied_on,
            "notes": self.notes,
        }


class JobStore:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT NOT NULL,
                    role TEXT NOT NULL,
                    status TEXT NOT NULL,
                    url TEXT DEFAULT '',
                    applied_on TEXT NOT NULL,
                    notes TEXT DEFAULT ''
                )
                """
            )

    def list_jobs(self) -> list[Job]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM jobs ORDER BY applied_on DESC, id DESC"
            ).fetchall()
        return [Job(**dict(row)) for row in rows]

    def add(
        self,
        company: str,
        role: str,
        status: str = "Applied",
        url: str = "",
        applied_on: str | None = None,
        notes: str = "",
    ) -> Job:
        company, role = company.strip(), role.strip()
        if not company or not role:
            raise ValueError("Company and role are required.")
        if status not in STATUSES:
            status = "Applied"
        applied_on = applied_on or date.today().isoformat()
        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO jobs (company, role, status, url, applied_on, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (company, role, status, url.strip(), applied_on, notes.strip()),
            )
            job_id = int(cur.lastrowid)
        return Job(job_id, company, role, status, url.strip(), applied_on, notes.strip())

    def set_status(self, job_id: int, status: str) -> None:
        if status not in STATUSES:
            raise ValueError("Unknown status.")
        with self._connect() as conn:
            conn.execute("UPDATE jobs SET status = ? WHERE id = ?", (status, job_id))

    def delete(self, job_id: int) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))

    def counts(self) -> dict[str, int]:
        tallies = {name: 0 for name in STATUSES}
        for job in self.list_jobs():
            tallies[job.status] = tallies.get(job.status, 0) + 1
        return tallies


def default_db() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "jobs.sqlite"


def seed_if_empty(store: JobStore) -> None:
    if store.list_jobs():
        return
    store.add("Open Source Corp", "Python intern", "Wishlist", notes="Watching this team.")
    store.add(
        "Local Library",
        "Automation volunteer",
        "Applied",
        applied_on=datetime.now().date().isoformat(),
        notes="Wrote about the file organizer in the note.",
    )
