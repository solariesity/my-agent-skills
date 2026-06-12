#!/usr/bin/env python3
"""Unified remember/recall CLI for the core memory-router skill."""

from __future__ import annotations

import argparse
import json
from memrouter_core import decide_memory_action, recall_memory, remember_memory, resolve_route


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    remember = subparsers.add_parser("remember", help="Store a memory entry in a routed markdown note.")
    add_common_route_args(remember)
    remember.add_argument("--vault-root", required=True, help="Filesystem path to the vault root.")
    remember.add_argument("--text", required=True, help="Memory content to store.")
    remember.add_argument("--topic", help="Short stable topic label for the entry. Required with --dedupe-mode topic.")
    remember.add_argument("--source", default="chat", help="Source label for the entry.")
    remember.add_argument(
        "--created-at",
        help="Optional ISO 8601 timestamp for the memory entry. Defaults to the current local time.",
    )
    remember.add_argument(
        "--dedupe-mode",
        default="exact",
        choices=("none", "exact", "topic"),
        help="Whether to always append, suppress exact duplicates, or upsert by explicit topic+source.",
    )

    recall = subparsers.add_parser("recall", help="Recall memory from a routed note or subtree.")
    add_common_route_args(recall)
    recall.add_argument("--vault-root", required=True, help="Filesystem path to the vault root.")
    recall.add_argument("--query", required=True, help="Non-empty case-insensitive text query to search for.")
    recall.add_argument("--limit", type=int, default=5, help="Maximum matches to return.")

    inspect_cmd = subparsers.add_parser("inspect", help="Inspect the routed note path without writing or searching.")
    add_common_route_args(inspect_cmd)

    decide = subparsers.add_parser("decide", help="Classify whether a memory should be stored and how.")
    decide.add_argument("--text", required=True, help="Memory candidate text to classify.")
    decide.add_argument("--user-id", help="Stable user identifier if known.")
    decide.add_argument("--project", help="Project name or slug if known.")
    decide.add_argument("--source", default="chat", help="Source label for the candidate memory.")
    decide.add_argument("--kind", help="Optional context kind such as meeting or summary.")

    args = parser.parse_args()
    if args.command == "remember" and args.dedupe_mode == "topic" and not (args.topic and args.topic.strip()):
        parser.error("--topic is required when --dedupe-mode topic is used.")
    if args.command == "recall" and not (args.query and args.query.strip()):
        parser.error("--query must be non-empty.")
    return args


def add_common_route_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--memory-type", required=True, help="Memory type to route.")
    parser.add_argument("--user-id", default="default-user", help="Stable user identifier.")
    parser.add_argument("--project", help="Project name or slug.")
    parser.add_argument("--date", help="Date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--root", default="memory-router", help="Vault-relative root folder.")

def inspect(args: argparse.Namespace) -> dict[str, object]:
    return {
        "command": "inspect",
        "route": resolve_route(
            memory_type=args.memory_type,
            user_id=args.user_id,
            project=args.project,
            date=args.date,
            root=args.root,
        ),
    }


def main() -> None:
    args = parse_args()
    if args.command == "remember":
        payload = remember_memory(
            vault_root=args.vault_root,
            memory_type=args.memory_type,
            text=args.text,
            user_id=args.user_id,
            project=args.project,
            date=args.date,
            root=args.root,
            topic=args.topic,
            source=args.source,
            dedupe_mode=args.dedupe_mode,
            created_at=args.created_at,
        )
    elif args.command == "recall":
        payload = recall_memory(
            vault_root=args.vault_root,
            query=args.query,
            memory_type=args.memory_type,
            user_id=args.user_id,
            project=args.project,
            date=args.date,
            root=args.root,
            limit=args.limit,
        )
    elif args.command == "decide":
        context = {
            "source": args.source,
            "kind": args.kind,
        }
        payload = decide_memory_action(
            text=args.text,
            user_id=args.user_id,
            project=args.project,
            context=context,
        )
    else:
        payload = inspect(args)

    print(json.dumps(payload, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
