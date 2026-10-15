from software.ats_resume_builder.builder import build_resume


JD = """
We want a Python developer who knows Flask, SQL, git, pytest, REST APIs, and Docker.
Agile teamwork and documentation matter.
"""

RESUME = """
Standley David
hello@example.com
555-0100

I write scripts sometimes.
Worked on a school project.
"""


def test_improved_resume_clears_ninety():
    result = build_resume(RESUME, JD, "Python developer", "Acme", include_suggested=True)
    assert result["original"]["total"] < result["improved"]["total"]
    assert result["improved"]["total"] >= 90
    assert "Python developer" in result["text"]
    assert "Acme" in result["text"]
    assert "SKILLS" in result["text"]


def test_flask_ats_flow():
    from app import app

    client = app.test_client()
    page = client.post(
        "/apps/ats/",
        data={
            "designation": "Python developer",
            "company": "Acme",
            "jd": JD,
            "resume": RESUME,
            "include_suggested": "on",
        },
    )
    assert page.status_code == 200
    assert b"Improved" in page.data
    down = client.post(
        "/apps/ats/download",
        data={
            "designation": "Python developer",
            "company": "Acme",
            "jd": JD,
            "resume": RESUME,
            "include_suggested": "on",
            "fmt": "txt",
        },
    )
    assert down.status_code == 200
    assert b"PROFESSIONAL SUMMARY" in down.data or b"SUMMARY" in down.data
