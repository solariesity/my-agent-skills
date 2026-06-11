from __future__ import annotations

import shutil
import subprocess
import sys
import unittest
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
TEST_TMP_ROOT = ROOT / ".tmp-tests"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from memrouter_core import recall_memory, remember_memory, resolve_route  # noqa: E402
from memrouter_core import decide_memory_action  # noqa: E402


class TempVaultTestCase(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TMP_ROOT.mkdir(exist_ok=True)
        self.vault_root = str(TEST_TMP_ROOT / f"vault-{uuid.uuid4().hex}")
        Path(self.vault_root).mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.vault_root, ignore_errors=True)


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    cmd = [sys.executable, "-B", str(SCRIPTS_DIR / "memrouter_cli.py"), *args]
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


__all__ = [
    "TempVaultTestCase",
    "decide_memory_action",
    "recall_memory",
    "remember_memory",
    "resolve_route",
    "run_cli",
]
