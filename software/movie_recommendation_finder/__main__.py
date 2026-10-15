from __future__ import annotations

import argparse

from .recommend import recommend


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Find a movie from a local catalog.")
    parser.add_argument("--like", default="", help="A film you already enjoy")
    parser.add_argument("--genre", action="append", default=[])
    parser.add_argument("--mood", default="")
    args = parser.parse_args(argv)
    rows = recommend(args.like, args.genre, args.mood)
    if not rows:
        print("No matches. Try a genre like comedy, or a mood like cozy.")
        return 0
    for row in rows:
        genres = ", ".join(row["genres"])
        print(f"{row['title']} ({row['year']}) — {genres} [{row['mood']}] score={row['score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
