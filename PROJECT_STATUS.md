# PROJECT_STATUS

Handoff for future chats. Read this before changing code.

## A. Overview

Personal Flask site for **Standley David** (`python-portfolio`): portfolio pages plus three live Python tools. Primary user is Standley; visitors see work and can run the tools.

**Stage:** local working app, not on GitHub/Render yet. No git commits (repo exists, all files untracked).

**Stack:** Python 3.14.5 locally (`runtime.txt` still says 3.12.8). Flask 3.1.2, gunicorn, pytest, pypdf, python-docx. Jinja templates, static CSS/JS.

## B. Architecture

| Path | Role |
| --- | --- |
| `app.py` | Entry: Flask app, blueprints, `/`, `/projects/<slug>`, `/api/*`, `/contact` |
| `data/site.py` | Name, bio, email, GitHub, LinkedIn |
| `data/projects.py` | Catalog of selected software |
| `software/smart_file_organizer/` | Sandbox file sorter; `/apps/organizer` |
| `software/job_application_tracker/` | SQLite jobs; `/apps/jobs`; DB `data/jobs.sqlite` (gitignored) |
| `software/ats_resume_builder/` | JD/resume analysis, rebuild, download; `/apps/ats` |
| `templates/` | Portfolio site only |
| `software/*/templates` + `static` | Each tool’s own HTML/CSS (independent look) |
| `tests/` | Flask routes + tool unit tests |

Each `software/*` package has CLI (`python -m software.<pkg>`) and is meant to become its own GitHub repo later. Tools stay in this repo so the site can import them.

**Contact:** form emails `stunningstanley@gmail.com` via SMTP (`mailer.py`) when `MAIL_PASSWORD` is set; also saves `data/messages.json`. Icons → `mailto:`, GitHub, LinkedIn.

**Separate work (do not mix):** Bible / YouTube / Instagram automation lives only at `D:\bible-history-studio`. It is not a portfolio tool and must not use this GitHub remote.

## C. Environment

```powershell
cd C:\Users\Bob\python-portfolio
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
python -m pytest
```

Site: http://127.0.0.1:5000  
Contact mail: `MAIL_USERNAME`, `MAIL_PASSWORD` (Gmail app password), optional `MAIL_TO`. Copy `.env.example` → `.env`. Optional later: `SECRET_KEY`.

**Copy on disk:** `D:\python-portfolio` (source copy of this portfolio only; recreate `.venv` there). C: is the Cursor workspace for the **portfolio**.

## D. Implementation status

**Done:**

- Portfolio UI (violet/black, Standley David, S mark until real logo)
- Three tools: **own HTML/CSS files**, same tokens and site nav as the portfolio, slightly different inner layouts. Homepage cards stay on portfolio CSS.
- ATS builder downloads
- Pretty JSON `/api/health`, `/api/projects`
- Contact form → `data/messages.json` (gitignored)
- ATS improved resume scores ≥ 90 on the sample JD when suggested keywords are included (tool score, not Workday)

**Not done:**

- GitHub push (portfolio + remaining tool repos)
- Render/live host
- Real logo file (`static/img/logo.svg` is a placeholder S)
- Real project write-ups beyond these three tools
- First git commit (user has not asked)

**Constraints:** Organizer web UI only touches its sandbox. ATS score is this app’s heuristic. Do not invent job history; suggested skills must be real. Do not add Bible History Studio back into this repo. Do not commit unless asked. Do not push unless asked.

## E. Quality and maintenance

- Tests: `tests/test_app.py`, `test_tools.py`, `test_ats.py`
- Git: `master`, **zero commits**, everything untracked. Checkpoint: first commit when you ask, plus keep D: copy; sqlite/messages/sandbox are gitignored and need their own backup if they matter.
- `runtime.txt` vs local 3.14.5 mismatch for Render later.

## Next useful step (pick one)

1. First git commit (no push) as a checkpoint.  
2. Push portfolio to GitHub / deploy Render.  
3. Split tools into separate GitHub repos.  
4. Replace logo; tighten ATS or another tool.

Wait for the next explicit development request before changing application code.

## InvoiceFlow (started 26 Oct 2026)

Self-contained app at `invoiceflow/`. Own venv, own README, port **5001**. Do not wire it into portfolio `app.py`.

**Phase 1 done:** Flask factory, SQLite + Flask-Migrate, public marketing pages, contact form, tests.

**Phase 2 next:** registration/login, business profile, customers, products.

Do not describe invoices/PDFs/payments as complete until those phases ship.
