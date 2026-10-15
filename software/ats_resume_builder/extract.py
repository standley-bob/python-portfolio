from __future__ import annotations

from pathlib import Path
import io
import re


def from_upload(filename: str, data: bytes) -> str:
    name = (filename or "").lower()
    if name.endswith(".txt") or name.endswith(".md"):
        return data.decode("utf-8", errors="ignore")
    if name.endswith(".docx"):
        from docx import Document

        doc = Document(io.BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs)
    if name.endswith(".pdf"):
        from pypdf import PdfReader

        reader = PdfReader(io.BytesIO(data))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages)
    return data.decode("utf-8", errors="ignore")


def contact_bits(text: str) -> dict[str, str]:
    email = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, re.I)
    phone = re.search(r"(\+?\d[\d\s().-]{8,}\d)", text)
    first = next((line.strip() for line in text.splitlines() if line.strip()), "Your Name")
    if "@" in first or re.search(r"\d", first):
        first = "Your Name"
    return {
        "name": first[:80],
        "email": email.group(0) if email else "",
        "phone": phone.group(0).strip() if phone else "",
    }


def read_path(path: Path) -> str:
    return from_upload(path.name, path.read_bytes())
