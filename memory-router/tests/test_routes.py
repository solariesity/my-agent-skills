from __future__ import annotations

from tests.support import resolve_route
import unittest


class RouteTests(unittest.TestCase):
    def test_route_slugifies_ascii_user_id(self) -> None:
        route = resolve_route(memory_type="preferences", user_id="A.L.")
        self.assertEqual(route["user_id"], "a-l")
        self.assertEqual(route["path"], "memory-router/users/a-l/preferences.md")

    def test_route_preserves_unicode_user_id(self) -> None:
        route = resolve_route(memory_type="preferences", user_id="张三")
        self.assertEqual(route["user_id"], "张三")
        self.assertEqual(route["path"], "memory-router/users/张三/preferences.md")

    def test_route_preserves_unicode_project_slug(self) -> None:
        route = resolve_route(memory_type="project-facts", project="研究项目")
        self.assertEqual(route["project_slug"], "研究项目")
        self.assertEqual(route["path"], "memory-router/projects/研究项目/facts.md")

    def test_route_slugifies_ascii_project_name(self) -> None:
        route = resolve_route(memory_type="project-facts", project="Demo Project")
        self.assertEqual(route["project_slug"], "demo-project")
        self.assertEqual(route["path"], "memory-router/projects/demo-project/facts.md")
