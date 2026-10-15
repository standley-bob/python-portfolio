from __future__ import annotations

import argparse
from pathlib import Path

from .builder import build_resume
from .extract import read_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ATS-style resume analysis and rewrite.")
    parser.add_argument("--resume", required=True)
    parser.add_argument("--jd", required=True)
    parser.add_argument("--designation", required=True)
    parser.add_argument("--company", required=True)
    parser.add_argument("--out", default="ats-resume.txt")
    args = parser.parse_args(argv)
    result = build_resume(
        read_path(Path(args.resume)),
        read_path(Path(args.jd)),
        args.designation,
        args.company,
        include_suggested=True,
    )
    Path(args.out).write_text(result["text"], encoding="utf-8")
    print(f"Original ATS-style score: {result['original']['total']}")
    print(f"Improved ATS-style score: {result['improved']['total']}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
