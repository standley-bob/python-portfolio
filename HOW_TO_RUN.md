# How to run this project

Use this file whenever you want to start the **python-portfolio** site on this PC.  
If launch steps, the port, or setup commands change, this file must be updated in the same change.

**Project folder:** `C:\Users\Bob\python-portfolio`  
**Local site:** http://127.0.0.1:5000  
**Start file:** `app.py`  
**Python used:** 3.14 on this machine (any 3.10+ is fine)

This is Standley David’s Flask portfolio: home page, three live tools, JSON API, contact form.

InvoiceFlow is a **separate** app. Do not mix it with these commands. See `invoiceflow\HOW_TO_RUN.md` (port **5001**).

---

## A. First time only (install once)

### Command Prompt

```bat
cd /d C:\Users\Bob\python-portfolio
py -3 --version
py -3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Then open a browser: http://127.0.0.1:5000

Leave that window open while you use the site. Stop the server with `Ctrl+C`.

`.env` is optional for browsing the site. Fill `MAIL_PASSWORD` later if you want the contact form to email Gmail. Never commit `.env`.

### PowerShell (Windows)

```powershell
cd C:\Users\Bob\python-portfolio
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python app.py
```

If `Activate.ps1` is blocked:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then run `.\.venv\Scripts\Activate.ps1` again.

### Visual Studio Code

1. File → Open Folder → `C:\Users\Bob\python-portfolio`.
2. Terminal → New Terminal (this is the VS Code prompt; it is PowerShell by default).
3. Click the Python version in the bottom-right status bar → choose  
   `.\.venv\Scripts\python.exe` (this project’s virtual environment).
4. In the VS Code terminal, paste the **PowerShell** commands from above (first time) or the **every day** commands below.
5. When you see `Running on http://127.0.0.1:5000`, Ctrl+click that link, or open it in Chrome/Edge.
6. To stop: click the terminal and press `Ctrl+C`.

You can also start without activating the venv if the interpreter is selected:

```powershell
C:\Users\Bob\python-portfolio\.venv\Scripts\python.exe app.py
```

Do **not** click Run on `invoiceflow\run.py` when you mean this portfolio. That app is port 5001.

---

## B. Every day after install

The `.venv` folder already exists. Do **not** create it again unless you deleted it.

### Command Prompt

```bat
cd /d C:\Users\Bob\python-portfolio
.venv\Scripts\activate.bat
python app.py
```

### PowerShell or VS Code terminal

```powershell
cd C:\Users\Bob\python-portfolio
.\.venv\Scripts\Activate.ps1
python app.py
```

Open: http://127.0.0.1:5000

If the page looks old, hard-refresh: `Ctrl+F5`.

---

## C. Pages to open while testing

| What | Address |
| --- | --- |
| Home | http://127.0.0.1:5000/ |
| Smart File Organizer | http://127.0.0.1:5000/apps/organizer/ |
| Job Application Tracker | http://127.0.0.1:5000/apps/jobs/ |
| ATS Analyzer & Resume Builder | http://127.0.0.1:5000/apps/ats/ |
| Health JSON | http://127.0.0.1:5000/api/health |
| Projects JSON | http://127.0.0.1:5000/api/projects |

There is no Movie Recommendation Finder on this site.

---

## D. Tests

Run tests from the **portfolio root**, and only the `tests` folder (so InvoiceFlow’s tests are not collected).

### Command Prompt

```bat
cd /d C:\Users\Bob\python-portfolio
.venv\Scripts\activate.bat
python -m pytest tests
```

### PowerShell / VS Code

```powershell
cd C:\Users\Bob\python-portfolio
.\.venv\Scripts\Activate.ps1
python -m pytest tests
```

Tool CLIs (optional):

```bat
py -3 -m software.smart_file_organizer
py -3 -m software.job_application_tracker list
```

---

## E. If something fails

| What you see | What to do |
| --- | --- |
| `python` not found | Use `py -3` instead of `python` |
| `Activate.ps1` cannot be loaded | Run the ExecutionPolicy command in section A |
| Port 5000 already in use | Another portfolio window is still running. Close it (`Ctrl+C`) or use that one |
| Page looks old | Hard-refresh the browser (`Ctrl+F5`) |
| Contact form does not email | Copy `.env.example` to `.env` and set a Gmail app password. Browsing still works without it |
| `pytest` errors under `invoiceflow` | You ran `pytest` from the root without `tests`. Use `python -m pytest tests` |

---

## F. What this version includes (and does not)

Includes: portfolio home, organizer, job tracker, ATS tool, `/api/health`, `/api/projects`, contact form (saves locally; emails if `.env` is set).  
Does not include: Movie Recommendation Finder, InvoiceFlow (that is `invoiceflow\`, port 5001).

Those can change later. Edit this file in the same change if how you start the app changes.
