"""Test configuration: import memory.py from arknights-skill/scripts/ and provide fixtures."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]
_MEMORY_PY = _REPO_ROOT / "arknights-skill" / "scripts" / "memory.py"


def _import_memory():
    spec = importlib.util.spec_from_file_location("memory", str(_MEMORY_PY))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["memory"] = mod
    spec.loader.exec_module(mod)
    return mod


_mod = _import_memory()


@pytest.fixture()
def memory():
    """Provide the memory module to test functions."""
    return _mod


@pytest.fixture(autouse=True)
def isolated_memory_dir(tmp_path):
    """Redirect memory storage to a temporary directory for every test."""
    env_dir = tmp_path / "memory"
    env_dir.mkdir()
    with patch.dict(os.environ, {"ARKNIGHTS_MEMORY_DIR": str(env_dir)}):
        yield env_dir
