from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from file_router_core import (
    capture_output,
    decide_route,
    find_files,
    intake_file,
    organize_file,
    route_file,
    scaffold,
    store_chat_text,
)  # noqa: E402


class FileRouterTests(unittest.TestCase):
    def test_decide_screenshot_defaults_to_media(self) -> None:
        decision = decide_route(source="Screenshot 2026-06-08.png", context="聊天截图", origin="incoming")
        self.assertEqual(decision["domain"], "media")
        self.assertEqual(decision["role"], "screenshot")

    def test_route_research_project_code(self) -> None:
        route = route_file(
            workspace_root="D:\\",
            domain="research",
            role="code",
            filename="train.py",
            project="Sea Ice Detection",
            project_type="research",
            date="2026-06-08",
        )
        self.assertIn("files/Research/Projects/sea-ice-detection/03_Code/train.py", route["relative_path"])

    def test_scaffold_and_organize_copy(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            scaffold(workspace_root=tmpdir, template="workspace")
            scaffold(workspace_root=tmpdir, template="research-project", project="Bird Detector")
            source = Path(tmpdir) / "figure.png"
            source.write_bytes(b"png-data")

            result = organize_file(
                workspace_root=tmpdir,
                source=str(source),
                domain="research",
                role="output",
                project="Bird Detector",
                project_type="research",
                origin="generated",
            )
            self.assertTrue(result["changed"])
            target = Path(result["target"])
            self.assertTrue(target.exists())
            self.assertTrue(source.exists())
            self.assertIn("files", target.parts)
            self.assertIn("06_Output", result["route"]["relative_path"])

    def test_find_returns_routed_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            scaffold(workspace_root=tmpdir, template="workspace")
            scaffold(workspace_root=tmpdir, template="general-project", project="helper-tool")
            source = Path(tmpdir) / "helper_notes.md"
            source.write_text("notes", encoding="utf-8")

            organize_file(
                workspace_root=tmpdir,
                source=str(source),
                domain="dev",
                role="work",
                project="helper-tool",
                project_type="general",
                origin="generated",
            )
            found = find_files(workspace_root=tmpdir, query="helper_notes", domain="dev", project="helper-tool")
            self.assertEqual(len(found["matches"]), 1)
            self.assertIn("files", found["matches"][0]["relative_path"])
            self.assertIn("03_Work", found["matches"][0]["relative_path"])

    def test_cli_decide_outputs_json(self) -> None:
        cli = SCRIPT_DIR / "file_router_cli.py"
        result = subprocess.run(
            [sys.executable, str(cli), "decide", "--source", "resume.docx", "--context", "personal resume"],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["domain"], "docs")

    def test_intake_dry_run_flags_ambiguous_files_for_review(self) -> None:
        result = intake_file(
            workspace_root=".",
            source="mystery.bin",
            context="",
            dry_run=True,
        )
        self.assertEqual(result["command"], "intake")
        self.assertTrue(result["needs_review"])
        self.assertEqual(result["recommended_next_step"], "ask-user")

    def test_capture_places_generated_report_under_files_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            source = Path(tmpdir) / "report.docx"
            source.write_bytes(b"docx")
            result = capture_output(
                workspace_root=tmpdir,
                source=str(source),
                project="helper-tool",
                project_type="general",
                context="generated project report",
            )
            target = Path(result["target"])
            self.assertTrue(target.exists())
            self.assertIn("files", target.parts)
            self.assertEqual(result["command"], "capture")

    def test_store_chat_text_creates_default_reminder_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            result = store_chat_text(
                workspace_root=tmpdir,
                text="\u5f88\u91cd\u8981\uff0c\u5b58\u5728\u6587\u4ef6\u4e2d\u5427\uff1a\u660e\u5929\u65e9\u4e0a 9 \u70b9\u63d0\u9192\u6211\u5f00\u4f1a",
                created_at="2026-06-09T08:00:00+08:00",
            )
            note_path = Path(result["path"])
            self.assertTrue(result["stored"])
            self.assertTrue(result["created_file"])
            self.assertTrue(note_path.exists())
            self.assertEqual(result["relative_path"], "files/Docs/Personal/\u63d0\u9192.md")
            content = note_path.read_text(encoding="utf-8")
            self.assertIn("# \u63d0\u9192", content)
            self.assertIn("## \u6761\u76ee", content)
            self.assertIn("\u660e\u5929\u65e9\u4e0a 9 \u70b9\u63d0\u9192\u6211\u5f00\u4f1a", content)

    def test_store_chat_text_appends_when_note_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            first = store_chat_text(
                workspace_root=tmpdir,
                text="\u5f88\u91cd\u8981\uff0c\u5b58\u5728\u6587\u4ef6\u4e2d\u5427\uff1a\u8bb0\u5f55\u4eca\u5929\u8981\u4ea4\u4ee3\u7801",
                created_at="2026-06-09T09:00:00+08:00",
            )
            second = store_chat_text(
                workspace_root=tmpdir,
                text="\u8bb0\u4e00\u4e0b\uff1a\u665a\u4e0a\u56de\u987e\u9879\u76ee\u8fdb\u5c55",
                created_at="2026-06-09T20:00:00+08:00",
            )
            note_path = Path(first["path"])
            content = note_path.read_text(encoding="utf-8")
            self.assertTrue(first["stored"])
            self.assertTrue(second["stored"])
            self.assertFalse(second["created_file"])
            self.assertEqual(first["path"], second["path"])
            self.assertEqual(content.count("| source: chat"), 2)
            self.assertIn("\u8bb0\u5f55\u4eca\u5929\u8981\u4ea4\u4ee3\u7801", content)
            self.assertIn("\u665a\u4e0a\u56de\u987e\u9879\u76ee\u8fdb\u5c55", content)

    def test_store_chat_text_requires_explicit_signal_unless_forced(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            skipped = store_chat_text(
                workspace_root=tmpdir,
                text="Tomorrow we should probably revisit the plan.",
            )
            self.assertFalse(skipped["stored"])
            self.assertFalse(Path(skipped["path"]).exists())
            forced = store_chat_text(
                workspace_root=tmpdir,
                text="Tomorrow we should probably revisit the plan.",
                created_at="2026-06-09T21:00:00+08:00",
                force=True,
            )
            self.assertTrue(forced["stored"])
            self.assertTrue(Path(forced["path"]).exists())

    def test_store_chat_text_supports_custom_target_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            result = store_chat_text(
                workspace_root=tmpdir,
                text="save this: track the weekly lab sync agenda",
                target_file="Lab/Tasks/weekly-sync.md",
                section="Inbox",
                source="daily-checkin",
                created_at="2026-06-09T07:30:00+08:00",
            )
            note_path = Path(result["path"])
            self.assertTrue(result["stored"])
            self.assertTrue(note_path.exists())
            self.assertEqual(result["relative_path"], "files/Lab/Tasks/weekly-sync.md")
            content = note_path.read_text(encoding="utf-8")
            self.assertIn("# weekly-sync", content)
            self.assertIn("## Inbox", content)
            self.assertIn("| source: daily-checkin", content)


if __name__ == "__main__":
    unittest.main()
