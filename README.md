# python-portfolio

Personal site for Standley David. Flask serves the pages, three live Python tools, a JSON API, and a contact form.

## Selected software (live on this site)

| App | Page | Package | Future GitHub repo |
| --- | --- | --- | --- |
| Smart File Organizer | `/apps/organizer` | `software/smart_file_organizer` | `github.com/standley-bob/smart-file-organizer` |
| Job Application Tracker | `/apps/jobs` | `software/job_application_tracker` | `github.com/standley-bob/job-application-tracker` |
| ATS Analyzer & Resume Builder | `/apps/ats` | `software/ats_resume_builder` | `github.com/standley-bob/ats-resume-builder` |

Each package has its own README and CLI so it can be copied into a **separate GitHub repository** after this portfolio is pushed. They stay in this repo until then so the site can run them.

## InvoiceFlow (separate app)

`invoiceflow/` is a standalone Flask product (online invoices). It is **not** mounted on this portfolio site. Run it on port 5001; see [`invoiceflow/README.md`](invoiceflow/README.md). Phase 1 is the public website and database setup only.

## Run locally

```powershell
cd C:\Users\Bob\python-portfolio
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

```powershell
python -m pytest
py -3 -m software.smart_file_organizer
py -3 -m software.job_application_tracker list
```

Health: http://127.0.0.1:5000/api/health  
Catalog: http://127.0.0.1:5000/api/projects

## Contact form → Gmail

The form emails `stunningstanley@gmail.com` and also saves a copy in `data/messages.json`.

1. Copy `.env.example` to `.env`.
2. In Google Account → Security → [App passwords](https://myaccount.google.com/apppasswords) (2-Step Verification must be on), make a password for Mail.
3. Put that 16-character password in `MAIL_PASSWORD`. Do not use your normal Gmail password.
4. Restart Flask. `/api/health` should show `"mail": true`.

On Render, set the same values as environment variables. Never commit `.env`.

## Put it live (Render)

Flask needs a Python host, not GitHub Pages.

1. Create a GitHub repo for **this** folder (`python-portfolio`) and push.
2. On [Render](https://render.com), New → Web Service. Build: `pip install -r requirements.txt`. Start: `gunicorn app:app --bind 0.0.0.0:$PORT`.

After the portfolio is on GitHub, split the tools into their own repos by copying each `software/...` folder. Ask in chat if you want those GitHub repos created and pushed.
