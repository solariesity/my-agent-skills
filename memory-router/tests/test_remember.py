from __future__ import annotations

from pathlib import Path

from tests.support import TempVaultTestCase, remember_memory


class RememberTests(TempVaultTestCase):
    def test_exact_dedupe_ignores_date_for_same_body(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            date="2026-06-04",
            text="prefers concise replies",
        )
        result = remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            date="2026-06-05",
            text="prefers concise replies",
        )

        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        content = note.read_text(encoding="utf-8")

        self.assertFalse(result["changed"])
        self.assertEqual(content.count("prefers concise replies"), 1)

    def test_exact_dedupe_ignores_created_at_for_same_body(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            date="2026-06-04",
            created_at="2026-06-04T09:00:00+08:00",
            text="prefers concise replies",
        )
        result = remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            date="2026-06-04",
            created_at="2026-06-04T10:15:00+08:00",
            text="prefers concise replies",
        )

        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        content = note.read_text(encoding="utf-8")

        self.assertFalse(result["changed"])
        self.assertIn("created_at: 2026-06-04T09:00:00+08:00", content)
        self.assertNotIn("created_at: 2026-06-04T10:15:00+08:00", content)

    def test_topic_upsert_replaces_same_topic_source(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            dedupe_mode="topic",
            topic="output-style",
            text="prefers Chinese answers",
        )
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            dedupe_mode="topic",
            topic="output-style",
            text="prefers concise replies",
        )

        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        content = note.read_text(encoding="utf-8")

        self.assertNotIn("prefers Chinese answers", content)
        self.assertEqual(content.count("prefers concise replies"), 1)

    def test_topic_upsert_replaces_legacy_entry_without_created_at(self) -> None:
        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text(
            "# Preferences\n\n## Entries\n- 2026-06-04 | topic: output-style | source: chat\n  prefers Chinese answers\n",
            encoding="utf-8",
        )

        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            dedupe_mode="topic",
            topic="output-style",
            created_at="2026-06-05T14:32:10+08:00",
            text="prefers concise replies",
        )

        content = note.read_text(encoding="utf-8")

        self.assertNotIn("prefers Chinese answers", content)
        self.assertIn("created_at: 2026-06-05T14:32:10+08:00", content)
        self.assertEqual(content.count("prefers concise replies"), 1)

    def test_entry_includes_created_at_timestamp(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            date="2026-06-04",
            created_at="2026-06-04T12:34:56+08:00",
            text="prefers concise replies",
        )

        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        content = note.read_text(encoding="utf-8")

        self.assertIn(
            "- 2026-06-04 | created_at: 2026-06-04T12:34:56+08:00 | topic: general | source: chat",
            content,
        )

    def test_created_at_can_drive_route_date(self) -> None:
        result = remember_memory(
            vault_root=self.vault_root,
            memory_type="ephemeral",
            user_id="alice",
            created_at="2026-06-07T22:45:00+08:00",
            text="temporary note",
        )

        self.assertEqual(result["route"]["date"], "2026-06-07")
        self.assertTrue(result["path"].endswith("memory-router/inbox/2026/2026-06-07.md"))

    def test_multiline_entry_stays_single_block(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="preferences",
            user_id="alice",
            dedupe_mode="topic",
            topic="notes",
            text="updated line\n- nested bullet",
        )

        note = Path(self.vault_root) / "memory-router" / "users" / "alice" / "preferences.md"
        content = note.read_text(encoding="utf-8")

        self.assertIn("  updated line\n  - nested bullet", content)
        self.assertNotIn("\n- nested bullet\n", content)
