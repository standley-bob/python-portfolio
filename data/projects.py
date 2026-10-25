"""Live Python tools shown on the site. Each folder under software/ can become its own GitHub repo."""

PROJECTS = [
    {
        "slug": "smart-file-organizer",
        "title": "Smart File Organizer",
        "status": "live",
        "year": "2026",
        "stack": ["Python", "pathlib", "Flask"],
        "demo": "organizer.home",
        "blurb": "Sorts a messy inbox by type — images, documents, code, audio, video — with a dry-run first so nothing moves until you say so.",
        "problem": "Downloads and desktop folders turn into junk drawers. I wanted a Python sorter I could trust, not a blind auto-move.",
        "approach": "Extension maps, a sandbox inbox, and apply as a second step. The same engine runs as a CLI and as a page on this site.",
        "highlights": [
            "Dry-run plan before any shutil.move",
            "Sandbox only — it will not touch your real Downloads folder from the website",
            "Live check on /apps/organizer and /apps/organizer/check.json so visitors can see pass/fail",
            "CLI: py -3 -m software.smart_file_organizer",
            "Meant to split later into github.com/standley-bob/smart-file-organizer",
        ],
        "signature": "def plan(inbox: Path) -> list[Move]:",
    },
    {
        "slug": "job-application-tracker",
        "title": "Job Application Tracker",
        "status": "live",
        "year": "2026",
        "stack": ["Python", "SQLite", "Flask"],
        "demo": "jobs.home",
        "blurb": "A local tracker for roles: wishlist, applied, interview, offer, rejected — stored in SQLite, not a spreadsheet tab.",
        "problem": "Applications vanish into notes apps. I wanted one Python store with statuses I can update in a click.",
        "approach": "sqlite3, a small JobStore, and a Flask board. Same store powers the CLI.",
        "highlights": [
            "Add company, role, date, link, and notes",
            "Move a row through Wishlist → Applied → Interview → Offer / Rejected",
            "CLI: py -3 -m software.job_application_tracker list",
            "Meant to split later into github.com/standley-bob/job-application-tracker",
        ],
        "signature": "def add(company: str, role: str, status: str = 'Applied') -> Job:",
    },
    {
        "slug": "ats-resume-builder",
        "title": "ATS Analyzer & Resume Builder",
        "status": "live",
        "year": "2026",
        "stack": ["Python", "Flask", "pypdf", "python-docx"],
        "demo": "ats.home",
        "blurb": "Paste a designation, company, job post, and resume. See skill gaps, an ATS-style score, then download a rebuilt file aimed at 90+.",
        "problem": "Job boards parse plain text. Fancy layouts disappear. I wanted a Python pass that reads the posting and rewrites the resume so a tracker can see the keywords.",
        "approach": "Extract skills from the JD and the resume, score headings and targeting, then emit a standard-heading resume you can download as txt, html, or docx.",
        "highlights": [
            "Job description + resume analysis and skill-gap list",
            "ATS-style score with coverage, structure, and company/designation targeting",
            "Rebuilt resume aimed at 90+ when job keywords are mirrored",
            "Download .txt, .html, or .docx",
        ],
        "signature": "def build_resume(resume: str, jd: str, designation: str, company: str) -> dict:",
    },
]


def all_projects():
    return PROJECTS


def get_project(slug: str):
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    return None
