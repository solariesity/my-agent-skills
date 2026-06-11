from __future__ import annotations

from tests.support import TempVaultTestCase, recall_memory, remember_memory


class RecallTests(TempVaultTestCase):
    def test_project_recall_does_not_scan_sessions(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="project-facts",
            project="demo",
            text="project uses sqlite",
        )
        remember_memory(
            vault_root=self.vault_root,
            memory_type="session-summary",
            project="demo",
            text="concise replies were discussed",
        )

        result = recall_memory(
            vault_root=self.vault_root,
            memory_type="project-facts",
            project="demo",
            query="concise",
        )

        self.assertEqual(result["matches"], [])
        self.assertEqual(result["scanned_files"], 1)

    def test_recall_finds_unicode_project_memory(self) -> None:
        remember_memory(
            vault_root=self.vault_root,
            memory_type="project-facts",
            project="研究项目",
            text="使用 sqlite",
        )

        result = recall_memory(
            vault_root=self.vault_root,
            memory_type="project-facts",
            project="研究项目",
            query="sqlite",
        )

        self.assertEqual(len(result["matches"]), 1)
        self.assertEqual(result["matches"][0]["match_source"], "direct-note")

    def test_recall_rejects_blank_query(self) -> None:
        with self.assertRaisesRegex(ValueError, "query cannot be empty"):
            recall_memory(
                vault_root=self.vault_root,
                memory_type="preferences",
                user_id="alice",
                query="   ",
            )
