from __future__ import annotations

from tests.support import run_cli
import unittest


class CliTests(unittest.TestCase):
    def test_cli_rejects_topic_mode_without_topic(self) -> None:
        result = run_cli(
            "remember",
            "--vault-root",
            ".",
            "--memory-type",
            "preferences",
            "--user-id",
            "alice",
            "--dedupe-mode",
            "topic",
            "--text",
            "missing topic",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--topic is required", result.stderr)

    def test_cli_rejects_blank_query(self) -> None:
        result = run_cli(
            "recall",
            "--vault-root",
            ".",
            "--memory-type",
            "preferences",
            "--user-id",
            "alice",
            "--query",
            "   ",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--query must be non-empty", result.stderr)

    def test_cli_rejects_invalid_created_at(self) -> None:
        result = run_cli(
            "remember",
            "--vault-root",
            ".",
            "--memory-type",
            "preferences",
            "--user-id",
            "alice",
            "--created-at",
            "not-a-datetime",
            "--text",
            "prefers concise replies",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("created_at must be an ISO 8601 datetime", result.stderr)
