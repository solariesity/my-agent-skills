from __future__ import annotations

from tests.support import decide_memory_action
import unittest


class DecideTests(unittest.TestCase):
    def test_decide_skips_trivial_chatter(self) -> None:
        result = decide_memory_action("thanks")

        self.assertFalse(result["should_persist"])
        self.assertIsNone(result["memory_type"])

    def test_decide_skips_trivial_chatter_in_chinese(self) -> None:
        result = decide_memory_action("好的，明白了。")

        self.assertFalse(result["should_persist"])
        self.assertIsNone(result["memory_type"])

    def test_decide_detects_preference_and_topic_upsert(self) -> None:
        result = decide_memory_action("The user prefers concise Chinese answers.", user_id="alice")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "preferences")
        self.assertEqual(result["topic"], "language")
        self.assertEqual(result["dedupe_mode"], "topic")

    def test_decide_detects_preference_and_topic_upsert_in_chinese(self) -> None:
        result = decide_memory_action("我更喜欢中文回复，尽量简洁一点。", user_id="alice")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "preferences")
        self.assertEqual(result["topic"], "language")
        self.assertEqual(result["dedupe_mode"], "topic")

    def test_decide_prefers_preference_over_project_fallback_in_chinese(self) -> None:
        result = decide_memory_action("以后都用中文回答。", user_id="alice", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "preferences")
        self.assertEqual(result["topic"], "language")

    def test_decide_does_not_treat_generic_project_comment_as_fact(self) -> None:
        result = decide_memory_action("这个项目不错。", user_id="alice", project="demo")

        self.assertFalse(result["should_persist"])
        self.assertIsNone(result["memory_type"])

    def test_decide_detects_project_fact(self) -> None:
        result = decide_memory_action("The project uses sqlite for local storage.", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "project-facts")
        self.assertEqual(result["topic"], "storage")

    def test_decide_routes_personal_interests_to_profile(self) -> None:
        result = decide_memory_action("The user likes these singers: Avril Lavigne and G.E.M.", user_id="alice")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "profile")
        self.assertEqual(result["topic"], "personal-interests")

    def test_decide_routes_workspace_paths_to_project_facts(self) -> None:
        result = decide_memory_action("Project path: D:\\work\\demo. All work must stay inside this workspace.", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "project-facts")
        self.assertEqual(result["topic"], "environment")

    def test_decide_routes_workspace_rules_to_project_decisions(self) -> None:
        result = decide_memory_action("From now on, always use vibe-talk in this workspace and store the mechanism in MemRouter.", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "project-decisions")
        self.assertEqual(result["topic"], "policy")

    def test_decide_rejects_sensitive_credentials(self) -> None:
        result = decide_memory_action("Password: Hyj123456@", user_id="alice")

        self.assertFalse(result["should_persist"])
        self.assertIsNone(result["memory_type"])
        self.assertIn("Sensitive credential-like information", result["reason"])

    def test_decide_detects_task(self) -> None:
        result = decide_memory_action("Next step: verify the recall flow and update docs.", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "task")
        self.assertEqual(result["topic"], "testing")
        self.assertEqual(result["dedupe_mode"], "exact")

    def test_decide_detects_task_in_chinese(self) -> None:
        result = decide_memory_action("下一步：补上测试，并更新文档。", project="demo")

        self.assertTrue(result["should_persist"])
        self.assertEqual(result["memory_type"], "task")
        self.assertEqual(result["topic"], "testing")
        self.assertEqual(result["dedupe_mode"], "exact")
