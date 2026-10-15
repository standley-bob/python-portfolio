from __future__ import annotations

import argparse

from .store import STATUSES, JobStore, default_db, seed_if_empty


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Track job applications in SQLite.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    add = sub.add_parser("add")
    add.add_argument("--company", required=True)
    add.add_argument("--role", required=True)
    add.add_argument("--status", default="Applied", choices=STATUSES)
    args = parser.parse_args(argv)

    store = JobStore(default_db())
    seed_if_empty(store)
    if args.cmd == "list":
        jobs = store.list_jobs()
        if not jobs:
            print("No applications yet.")
            return 0
        for job in jobs:
            print(f"[{job.status}] {job.company} — {job.role} ({job.applied_on})")
        return 0
    job = store.add(args.company, args.role, args.status)
    print(f"Added #{job.id}: {job.company} — {job.role}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
