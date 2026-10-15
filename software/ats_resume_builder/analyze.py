from __future__ import annotations

import re

from .keywords import HEADINGS, KNOWN_SKILLS


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9+#./ ]+", " ", text.lower())


def extract_skills(text: str) -> list[str]:
    blob = _norm(text)
    found = []
    for skill in KNOWN_SKILLS:
        if re.search(rf"(?<![a-z]){re.escape(skill)}(?![a-z])", blob):
            found.append(skill)
    extras = re.findall(r"\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2})\b", text)
    skip = {"The", "This", "And", "With", "Job", "Role", "You", "Our"}
    for phrase in extras:
        if phrase in skip or len(phrase) < 3:
            continue
        key = phrase.lower()
        if key not in found and key in blob:
            found.append(key)
    # unique, stable
    seen = []
    for item in found:
        if item not in seen:
            seen.append(item)
    return seen[:40]


def has_heading(text: str, names: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(re.search(rf"(?m)^\s*{re.escape(name)}\s*$", lower) or name in lower for name in names)


def score_resume(resume: str, jd: str, designation: str, company: str) -> dict:
    jd_skills = extract_skills(jd) or extract_skills(designation + " " + jd)
    resume_skills = extract_skills(resume)
    jd_set = set(jd_skills)
    have = sorted(jd_set.intersection(resume_skills))
    missing = sorted(jd_set.difference(resume_skills))
    cover = (len(have) / len(jd_set) * 100) if jd_set else 70.0

    structure = 0
    structure += 8 if has_heading(resume, ("summary", "objective", "profile")) else 0
    structure += 8 if has_heading(resume, ("experience", "employment", "work")) else 0
    structure += 7 if has_heading(resume, ("skills",)) else 0
    structure += 7 if has_heading(resume, ("education",)) else 0
    blob = resume.lower()
    structure += 5 if "@" in resume else 0
    structure += 5 if re.search(r"\d{3}", resume) else 0
    # max 40

    formatting = 15
    if "<table" in blob or "|" in resume and resume.count("|") > 8:
        formatting -= 6
    words = len(resume.split())
    if words < 80:
        formatting -= 6
    if words > 900:
        formatting -= 4
    formatting = max(0, formatting)

    targeting = 0
    targeting += 5 if designation and designation.lower() in blob else 0
    targeting += 5 if company and company.lower() in blob else 0

    keyword_pts = round(cover / 100 * 45, 1)
    total = round(keyword_pts + structure + formatting + targeting, 1)
    total = min(99.0, total)
    return {
        "total": total,
        "keyword_pts": keyword_pts,
        "structure": structure,
        "formatting": formatting,
        "targeting": targeting,
        "coverage": round(cover, 1),
        "jd_skills": jd_skills,
        "resume_skills": resume_skills,
        "matched": have,
        "missing": missing,
        "word_count": words,
    }
