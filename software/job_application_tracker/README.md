# Job Application Tracker

SQLite-backed tracker for roles you want, applied to, interviewed for, or closed.

This folder is written to become its own GitHub repo (`job-application-tracker`) later. On the portfolio it also runs as a live page at `/apps/jobs`.

## CLI

```powershell
py -3 -m software.job_application_tracker list
py -3 -m software.job_application_tracker add --company "Acme" --role "Python developer"
```

Database file: `data/jobs.sqlite` (gitignored).
