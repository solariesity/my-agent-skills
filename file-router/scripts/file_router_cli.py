#!/usr/bin/env python3
"""CLI entry point for the file-router skill."""

from __future__ import annotations

import argparse
import json

from file_router_core import (
    capture_output,
    decide_route,
    find_files,
    intake_file,
    organize_file,
    route_file,
    scaffold,
    store_chat_text,
)


def add_scope_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--domain", help="Top-level workspace domain such as research, dev, docs, or media.")
    parser.add_argument("--role", help="Artifact role within the selected domain.")
    parser.add_argument("--project", help="Project name when the file belongs to a specific project.")
    parser.add_argument("--project-type", choices=("general", "research"), help="Project template type.")
    parser.add_argument("--course", help="Course name for course-scoped files.")
    parser.add_argument("--term", help="Academic term such as 2026-Spring.")
    parser.add_argument("--date", help="Route date in YYYY-MM-DD format.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    decide = subparsers.add_parser("decide", help="Guess a likely domain and role from a file and context.")
    decide.add_argument("--source", help="Source filename or path.")
    decide.add_argument("--context", help="Free-form context that helps classification.")
    decide.add_argument("--origin", default="incoming", choices=("incoming", "generated", "existing"))
    add_scope_args(decide)

    intake = subparsers.add_parser("intake", help="Handle a user-shared file with incoming-file defaults.")
    intake.add_argument("--workspace-root", default=".", help="Agent working directory. Routed files live under ./files by default.")
    intake.add_argument("--source", required=True, help="Existing file path to organize.")
    intake.add_argument("--context", help="Free-form context that helps classification.")
    intake.add_argument("--target-name", help="Optional target filename override.")
    intake.add_argument("--version", help="Optional version suffix such as v01 or final.")
    intake.add_argument("--date-prefix", action="store_true", help="Prefix the route date to the target filename.")
    intake.add_argument("--mode", default="copy", choices=("copy", "move"))
    intake.add_argument("--collision", default="rename", choices=("rename", "skip", "overwrite"))
    intake.add_argument("--dry-run", action="store_true", help="Resolve and classify without writing the file.")
    add_scope_args(intake)

    capture = subparsers.add_parser("capture", help="Handle an agent-created file with generated-file defaults.")
    capture.add_argument("--workspace-root", default=".", help="Agent working directory. Routed files live under ./files by default.")
    capture.add_argument("--source", required=True, help="Existing file path to organize.")
    capture.add_argument("--context", help="Free-form context that helps classification.")
    capture.add_argument("--target-name", help="Optional target filename override.")
    capture.add_argument("--version", help="Optional version suffix such as v01 or final.")
    capture.add_argument("--date-prefix", action="store_true", help="Prefix the route date to the target filename.")
    capture.add_argument("--mode", default="copy", choices=("copy", "move"))
    capture.add_argument("--collision", default="rename", choices=("rename", "skip", "overwrite"))
    capture.add_argument("--dry-run", action="store_true", help="Resolve and classify without writing the file.")
    add_scope_args(capture)

    route = subparsers.add_parser("route", help="Resolve an explicit deterministic storage path.")
    route.add_argument("--workspace-root", default=".", help="Agent working directory. Routed files live under ./files by default.")
    route.add_argument("--filename", required=True, help="Filename to route.")
    route.add_argument("--target-name", help="Optional target filename override.")
    route.add_argument("--version", help="Optional version suffix such as v01 or final.")
    route.add_argument("--date-prefix", action="store_true", help="Prefix the route date to the target filename.")
    add_scope_args(route)

    organize = subparsers.add_parser("organize", help="Copy or move a file into its routed location.")
    organize.add_argument("--workspace-root", default=".", help="Agent working directory. Routed files live under ./files by default.")
    organize.add_argument("--source", required=True, help="Existing file path to organize.")
    organize.add_argument("--context", help="Free-form context that helps classification.")
    organize.add_argument("--origin", default="incoming", choices=("incoming", "generated", "existing"))
    organize.add_argument("--target-name", help="Optional target filename override.")
    organize.add_argument("--version", help="Optional version suffix such as v01 or final.")
    organize.add_argument("--date-prefix", action="store_true", help="Prefix the route date to the target filename.")
    organize.add_argument("--mode", default="copy", choices=("copy", "move"))
    organize.add_argument("--collision", default="rename", choices=("rename", "skip", "overwrite"))
    add_scope_args(organize)

    find = subparsers.add_parser("find", help="Find files again within a routed scope.")
    find.add_argument("--workspace-root", default=".", help="Agent working directory. Routed files live under ./files by default.")
    find.add_argument("--query", required=True, help="Case-insensitive filename or path query.")
    find.add_argument("--limit", type=int, default=20, help="Maximum matches to return.")
    add_scope_args(find)

    remember = subparsers.add_parser("remember-text", help="Append important chat text into a routed markdown note.")
    remember.add_argument("--workspace-root", default=".", help="Agent working directory. Notes live under ./files by default.")
    remember.add_argument("--text", required=True, help="Chat text to evaluate and optionally store.")
    remember.add_argument("--target-file", help="Optional note path relative to ./files, such as Docs/Personal/提醒.md.")
    remember.add_argument("--project", help="Optional project tag stored with the chat entry.")
    remember.add_argument("--source", default="chat", help="Entry source label, such as chat or daily-checkin.")
    remember.add_argument("--section", help="Markdown section name used for appended entries.")
    remember.add_argument("--created-at", help="Optional ISO timestamp override.")
    remember.add_argument("--force", action="store_true", help="Store even if no explicit importance cue is detected.")

    scaffold_cmd = subparsers.add_parser("scaffold", help="Create workspace or project skeletons.")
    scaffold_cmd.add_argument("--workspace-root", default=".", help="Agent working directory. The scaffold is created under ./files by default.")
    scaffold_cmd.add_argument("--template", required=True, choices=("workspace", "general-project", "research-project"))
    scaffold_cmd.add_argument("--project", help="Project name for project templates.")
    scaffold_cmd.add_argument("--domain", help="Base domain for general-project scaffolds.")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "decide":
        payload = decide_route(
            source=args.source,
            context=args.context,
            origin=args.origin,
            domain=args.domain,
            role=args.role,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
        )
    elif args.command == "intake":
        payload = intake_file(
            workspace_root=args.workspace_root,
            source=args.source,
            domain=args.domain,
            role=args.role,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
            context=args.context,
            date=args.date,
            target_name=args.target_name,
            version=args.version,
            date_prefix=args.date_prefix,
            mode=args.mode,
            collision=args.collision,
            dry_run=args.dry_run,
        )
    elif args.command == "capture":
        payload = capture_output(
            workspace_root=args.workspace_root,
            source=args.source,
            domain=args.domain,
            role=args.role,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
            context=args.context,
            date=args.date,
            target_name=args.target_name,
            version=args.version,
            date_prefix=args.date_prefix,
            mode=args.mode,
            collision=args.collision,
            dry_run=args.dry_run,
        )
    elif args.command == "route":
        if not args.domain or not args.role:
            raise SystemExit("--domain and --role are required for route.")
        payload = route_file(
            workspace_root=args.workspace_root,
            domain=args.domain,
            role=args.role,
            filename=args.filename,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
            date=args.date,
            target_name=args.target_name,
            version=args.version,
            date_prefix=args.date_prefix,
        )
    elif args.command == "organize":
        payload = organize_file(
            workspace_root=args.workspace_root,
            source=args.source,
            origin=args.origin,
            domain=args.domain,
            role=args.role,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
            context=args.context,
            date=args.date,
            target_name=args.target_name,
            version=args.version,
            date_prefix=args.date_prefix,
            mode=args.mode,
            collision=args.collision,
        )
    elif args.command == "find":
        payload = find_files(
            workspace_root=args.workspace_root,
            query=args.query,
            domain=args.domain,
            project=args.project,
            project_type=args.project_type,
            course=args.course,
            term=args.term,
            date=args.date,
            limit=args.limit,
        )
    elif args.command == "remember-text":
        payload = store_chat_text(
            workspace_root=args.workspace_root,
            text=args.text,
            target_file=args.target_file,
            project=args.project,
            source=args.source,
            section=args.section,
            created_at=args.created_at,
            force=args.force,
        )
    else:
        payload = scaffold(
            workspace_root=args.workspace_root,
            template=args.template,
            project=args.project,
            domain=args.domain,
        )

    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
