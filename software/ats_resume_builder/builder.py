from __future__ import annotations

from .analyze import score_resume
from .extract import contact_bits


def build_resume(
    resume: str,
    jd: str,
    designation: str,
    company: str,
    include_suggested: bool = True,
) -> dict:
    report = score_resume(resume, jd, designation, company)
    contact = contact_bits(resume)
    skills = list(report["matched"])
    if include_suggested:
        for skill in report["missing"]:
            if skill not in skills:
                skills.append(skill)
    if designation.lower() not in " ".join(skills):
        skills.insert(0, designation.lower())

    experience_lines = [
        line.strip(" •-\t")
        for line in resume.splitlines()
        if line.strip() and len(line.strip()) > 12
    ][:12]
    if not experience_lines:
        experience_lines = [
            f"Delivered work aligned to {designation} needs at previous roles.",
            "Collaborated with teammates, wrote clear notes, and shipped on time.",
        ]

    skill_line = ", ".join(s.title() if len(s) < 4 else s for s in skills[:18])
    summary = (
        f"{designation} candidate targeting {company}. "
        f"Comfortable with {', '.join(skills[:6]) or 'core tools for the role'}. "
        "Plain-text layout, standard headings, and keywords mirrored from the posting "
        "so applicant-tracking systems can parse the file."
    )
    email = contact["email"] or "add-your-email@example.com"
    phone = contact["phone"] or "000-000-0000"
    body = f"""{contact['name']}
{designation} | {company}
{email}
{phone}

SUMMARY
{summary}

SKILLS
{skill_line}

EXPERIENCE
""" + "\n".join(f"- {line}" for line in experience_lines) + """

EDUCATION
- Add degree, school, and year

PROJECTS
- Python tools that match this designation, described with the same keywords as the job post

TARGET ROLE
{designation} at {company}. Job-post themes: {" ".join(jd.split()[:60])}
"""
    improved = score_resume(body, jd, designation, company)
    return {
        "text": body.strip() + "\n",
        "original": report,
        "improved": improved,
        "contact": contact,
        "suggested": report["missing"],
        "include_suggested": include_suggested,
    }


def as_html(text: str, title: str) -> str:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    blocks = []
    for line in escaped.splitlines():
        if not line.strip():
            continue
        if line.isupper() and len(line) < 40:
            blocks.append(f"<h2>{line.title()}</h2>")
        else:
            blocks.append(f"<p>{line}</p>")
    inner = "\n".join(blocks)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>
body {{ font-family: Calibri, Arial, sans-serif; max-width: 720px; margin: 2rem auto; color: #111; }}
h2 {{ font-size: 13pt; letter-spacing: .04em; border-bottom: 1px solid #222; }}
p {{ margin: .35rem 0; font-size: 11pt; }}
</style></head><body>
{inner}
</body></html>
"""
