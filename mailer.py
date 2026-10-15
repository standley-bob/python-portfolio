from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage

from data.site import EMAIL


class MailNotConfigured(RuntimeError):
    """SMTP username or app password is missing."""


def mail_settings() -> dict:
    username = (os.environ.get("MAIL_USERNAME") or EMAIL).strip()
    return {
        "host": os.environ.get("MAIL_SERVER", "smtp.gmail.com").strip(),
        "port": int(os.environ.get("MAIL_PORT", "587")),
        "username": username,
        "password": (os.environ.get("MAIL_PASSWORD") or "").strip(),
        "to": (os.environ.get("MAIL_TO") or EMAIL).strip(),
        "use_tls": os.environ.get("MAIL_USE_TLS", "1") not in {"0", "false", "False"},
    }


def mail_ready() -> bool:
    settings = mail_settings()
    return bool(settings["username"] and settings["password"] and settings["to"])


def send_contact(payload: dict) -> None:
    settings = mail_settings()
    if not settings["password"] or not settings["username"] or not settings["to"]:
        raise MailNotConfigured("Set MAIL_PASSWORD (Gmail app password) in .env")

    visitor = payload["email"]
    body = (
        f"From: {payload['name']} <{visitor}>\n"
        f"At: {payload['at']}\n\n"
        f"{payload['message']}\n"
    )
    msg = EmailMessage()
    msg["Subject"] = f"Portfolio contact from {payload['name']}"
    msg["From"] = settings["username"]
    msg["To"] = settings["to"]
    msg["Reply-To"] = visitor
    msg.set_content(body)

    with smtplib.SMTP(settings["host"], settings["port"], timeout=20) as smtp:
        if settings["use_tls"]:
            smtp.starttls()
        smtp.login(settings["username"], settings["password"])
        smtp.send_message(msg)
