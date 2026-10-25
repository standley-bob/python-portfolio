from app import app
from mailer import MailNotConfigured


def test_home_ok():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Selected software" in response.data
    assert b"Standley David" in response.data
    assert b"stunningstanley@gmail.com" in response.data
    assert b"https://github.com/standley-bob" in response.data
    assert b"https://www.linkedin.com/in/standley-david-/" in response.data


def test_project_page():
    client = app.test_client()
    response = client.get("/projects/smart-file-organizer")
    assert response.status_code == 200
    assert b"Smart File Organizer" in response.data


def test_live_apps():
    client = app.test_client()
    assert client.get("/apps/organizer/").status_code == 200
    check = client.get("/apps/organizer/check.json")
    assert check.status_code == 200
    payload = check.get_json()
    assert payload["ok"] is True
    assert payload["moved"] == payload["expected"]
    live = client.post("/apps/organizer/", data={"action": "live-check"})
    assert live.status_code == 200
    assert b"Live check passed" in live.data
    assert b"holiday.jpg" in live.data
    assert client.get("/apps/jobs/").status_code == 200
    assert client.get("/apps/ats/").status_code == 200
    assert client.get("/apps/movies/").status_code == 404


def test_missing_project():
    client = app.test_client()
    assert client.get("/projects/does-not-exist").status_code == 404


def test_health_and_api():
    client = app.test_client()
    health = client.get("/api/health").get_json()
    catalog = client.get("/api/projects").get_json()
    assert health["ok"] is True
    assert "mail" in health
    assert len(catalog["projects"]) >= 1
    pretty = client.get("/api/projects").get_data(as_text=True)
    assert "\n" in pretty
    assert pretty.strip().startswith("{")


def test_contact_requires_fields():
    client = app.test_client()
    response = client.post("/contact", data={"name": "", "email": "", "message": ""})
    assert response.status_code == 400


def test_contact_emails_and_saves(monkeypatch, tmp_path):
    sent = {}

    def fake_send(payload):
        sent["payload"] = payload

    monkeypatch.setattr("app.send_contact", fake_send)
    monkeypatch.setattr("app.MESSAGES", tmp_path / "messages.json")
    client = app.test_client()
    response = client.post(
        "/contact",
        data={"name": "David", "email": "standleydavid02@gmail.com", "message": "Hello Test Message"},
    )
    assert response.status_code == 302
    assert sent["payload"]["message"] == "Hello Test Message"
    saved = (tmp_path / "messages.json").read_text(encoding="utf-8")
    assert "Hello Test Message" in saved


def test_contact_without_mail_config(monkeypatch, tmp_path):
    def boom(_payload):
        raise MailNotConfigured("missing password")

    monkeypatch.setattr("app.send_contact", boom)
    monkeypatch.setattr("app.MESSAGES", tmp_path / "messages.json")
    client = app.test_client()
    response = client.post(
        "/contact",
        data={"name": "David", "email": "a@b.co", "message": "still save me"},
    )
    assert response.status_code == 503
    assert b"not set up yet" in response.data
    assert "still save me" in (tmp_path / "messages.json").read_text(encoding="utf-8")
