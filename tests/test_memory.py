"""Unit tests for memory.py — doctor profile merge logic and commands."""

from __future__ import annotations

import json
import os
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture(autouse=True)
def _inject_memory(memory, request):
    """Inject the memory module as `self.memory` for all test class methods."""
    if request.cls is not None:
        request.cls.memory = memory


class TestNormalizeProfile:
    def test_missing_fields_filled(self):
        data = {"schema_version": 1, "game": "Arknights"}
        profile = self.memory.normalize_profile(data)
        assert profile["doctor"]["name"] is None
        assert profile["account"]["progress"] == {}
        assert profile["operators"] == {}
        assert profile["pending_confirmations"] == []

    def test_invalid_schema_version_rejected(self):
        data = {"schema_version": 99, "game": "Arknights"}
        with pytest.raises(ValueError, match="Unsupported schema_version"):
            self.memory.normalize_profile(data)

    def test_non_dict_input_rejected(self):
        with pytest.raises(ValueError, match="JSON object"):
            self.memory.normalize_profile("not a dict")


class TestLoadAndSave:
    def test_empty_profile_first_write(self, isolated_memory_dir: Path):
        profile, created = self.memory.load_profile()
        assert created is True
        assert profile["schema_version"] == 1
        self.memory.save_profile(profile, touch_updated_at=False)
        assert (isolated_memory_dir / "doctor-profile.json").exists()

    def test_roundtrip(self):
        profile = self.memory.empty_profile()
        profile["doctor"]["name"] = "TestDoctor"
        self.memory.save_profile(profile, touch_updated_at=False)
        loaded, created = self.memory.load_profile()
        assert created is False
        assert loaded["doctor"]["name"] == "TestDoctor"


class TestMergeMonotonicInt:
    def test_normal_upgrade(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_monotonic_int(profile, target, "level", 40, "test.level", "t")
        self.memory.merge_monotonic_int(profile, target, "level", 60, "test.level", "t")
        assert target["level"] == 60
        assert len(profile["pending_confirmations"]) == 0

    def test_downgrade_creates_pending(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_monotonic_int(profile, target, "level", 60, "test.level", "t")
        self.memory.merge_monotonic_int(profile, target, "level", 40, "test.level", "t")
        assert target["level"] == 60
        assert len(profile["pending_confirmations"]) == 1
        assert profile["pending_confirmations"][0]["incoming"] == 40

    def test_same_value_no_change(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_monotonic_int(profile, target, "level", 50, "test.level", "t")
        changed = self.memory.merge_monotonic_int(profile, target, "level", 50, "test.level", "t")
        assert changed is False
        assert target["level"] == 50


class TestMergeTextScalar:
    def test_first_write(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        changed = self.memory.merge_text_scalar(profile, target, "name", "Alice", "doc.name", "t")
        assert changed is True
        assert target["name"] == "Alice"

    def test_conflict_goes_to_pending(self):
        profile = self.memory.empty_profile()
        target: dict = {"name": "Alice"}
        changed = self.memory.merge_text_scalar(profile, target, "name", "Bob", "doc.name", "t")
        assert changed is True
        assert target["name"] == "Alice"
        assert len(profile["pending_confirmations"]) == 1


class TestMergeOwned:
    def test_false_to_true(self):
        profile = self.memory.empty_profile()
        op = {"owned": False}
        changed = self.memory.merge_owned(profile, op, True, "op.owned", "t")
        assert changed is True
        assert op["owned"] is True
        assert len(profile["pending_confirmations"]) == 0

    def test_true_to_false_pending(self):
        profile = self.memory.empty_profile()
        op = {"owned": True}
        changed = self.memory.merge_owned(profile, op, False, "op.owned", "t")
        assert changed is True
        assert op["owned"] is True
        assert len(profile["pending_confirmations"]) == 1


class TestMergeEliteAndLevel:
    def test_elite_upgrade_with_level(self):
        profile = self.memory.empty_profile()
        op = {"elite": 1, "level": 40}
        self.memory.merge_elite_and_level(profile, op, {"elite": 2, "level": 1}, "op", "t")
        assert op["elite"] == 2
        assert op["level"] == 1

    def test_elite_downgrade_creates_pending(self):
        profile = self.memory.empty_profile()
        op = {"elite": 2, "level": 50}
        self.memory.merge_elite_and_level(profile, op, {"elite": 1, "level": 40}, "op", "t")
        assert op["elite"] == 2
        assert op["level"] == 50
        pending_fields = [p["field"] for p in profile["pending_confirmations"]]
        assert "op.elite" in pending_fields
        assert "op.level" in pending_fields

    def test_same_elite_level_downgrade(self):
        profile = self.memory.empty_profile()
        op = {"elite": 2, "level": 50}
        self.memory.merge_elite_and_level(profile, op, {"level": 30}, "op", "t")
        assert op["level"] == 50
        assert any(p["field"] == "op.level" for p in profile["pending_confirmations"])


class TestMergeMasteries:
    def test_mastery_upgrade(self):
        profile = self.memory.empty_profile()
        op = self.memory.default_operator("t")
        self.memory.merge_masteries(profile, op, {"3": 2}, "op", "t")
        assert op["masteries"]["3"] == 2

    def test_mastery_downgrade_pending(self):
        profile = self.memory.empty_profile()
        op = self.memory.default_operator("t")
        op["masteries"] = {"3": 3}
        self.memory.merge_masteries(profile, op, {"3": 2}, "op", "t")
        assert op["masteries"]["3"] == 3
        assert any("masteries.3" in p["field"] for p in profile["pending_confirmations"])


class TestMergeMappingLatest:
    def test_numeric_monotonic(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_mapping_latest(profile, target, {"sanity": 100}, "res", "t")
        self.memory.merge_mapping_latest(profile, target, {"sanity": 50}, "res", "t")
        assert target["sanity"] == 100
        assert len(profile["pending_confirmations"]) == 1

    def test_string_overwrite(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_mapping_latest(profile, target, {"chapter": "7"}, "prog", "t")
        self.memory.merge_mapping_latest(profile, target, {"chapter": "8"}, "prog", "t")
        assert target["chapter"] == "8"
        assert len(profile["pending_confirmations"]) == 0

    def test_bool_overwrite(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        self.memory.merge_mapping_latest(profile, target, {"auto": True}, "pref", "t")
        self.memory.merge_mapping_latest(profile, target, {"auto": False}, "pref", "t")
        assert target["auto"] is False

    def test_invalid_type_rejected(self):
        profile = self.memory.empty_profile()
        target: dict = {}
        with pytest.raises(ValueError, match="must be a concise string"):
            self.memory.merge_mapping_latest(profile, target, {"key": [1, 2]}, "field", "t")


class TestApplyPatch:
    def test_full_operator_workflow(self):
        profile = self.memory.empty_profile()
        p1 = self.memory.apply_patch(profile, {"operators": {"SilverAsh": {"owned": True, "elite": 2, "level": 50, "masteries": {"3": 3}}}})
        assert p1["operators"]["SilverAsh"]["elite"] == 2
        assert p1["operators"]["SilverAsh"]["masteries"]["3"] == 3

        p2 = self.memory.apply_patch(p1, {"operators": {"SilverAsh": {"elite": 1, "level": 40}}})
        assert p2["operators"]["SilverAsh"]["elite"] == 2
        assert len(p2["pending_confirmations"]) > 0

    def test_doctor_info(self):
        profile = self.memory.empty_profile()
        p1 = self.memory.apply_patch(profile, {"doctor": {"name": "DoctorK", "server": "CN", "level": 120}})
        assert p1["doctor"]["name"] == "DoctorK"
        assert p1["doctor"]["level"] == 120

    def test_account_resources_monotonic(self):
        profile = self.memory.empty_profile()
        p1 = self.memory.apply_patch(profile, {"account": {"resources": {"lmd": 5000000}}})
        assert p1["account"]["resources"]["lmd"] == 5000000
        p2 = self.memory.apply_patch(p1, {"account": {"resources": {"lmd": 3000000}}})
        assert p2["account"]["resources"]["lmd"] == 5000000
        assert any(p["field"] == "account.resources.lmd" for p in p2["pending_confirmations"])


class TestSetNested:
    def test_simple_path(self):
        data = {"a": {"b": {"c": 1}}}
        self.memory._set_nested(data, "a.b.c", 42)
        assert data["a"]["b"]["c"] == 42

    def test_creates_intermediate_dicts(self):
        data: dict = {}
        self.memory._set_nested(data, "a.b.c", 99)
        assert data["a"]["b"]["c"] == 99

    def test_operator_path(self):
        data = {"operators": {"Exusiai": {"level": 50}}}
        self.memory._set_nested(data, "operators.Exusiai.level", 80)
        assert data["operators"]["Exusiai"]["level"] == 80


class TestCommandConfirm:
    def test_confirm_applies_value(self):
        profile = self.memory.empty_profile()
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 60, "doctor.level", "t")
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 40, "doctor.level", "t")
        assert profile["doctor"]["level"] == 60
        self.memory.save_profile(profile, touch_updated_at=False)

        args = SimpleNamespace(field="doctor.level", apply=True)
        rc = self.memory.command_confirm(args)
        assert rc == 0
        loaded, _ = self.memory.load_profile()
        assert loaded["doctor"]["level"] == 40
        assert len(loaded["pending_confirmations"]) == 0

    def test_confirm_no_match_returns_1(self, capsys):
        profile = self.memory.empty_profile()
        self.memory.save_profile(profile, touch_updated_at=False)
        args = SimpleNamespace(field="nonexistent.field", apply=True)
        rc = self.memory.command_confirm(args)
        assert rc == 1


class TestCommandDismiss:
    def test_dismiss_removes_pending(self):
        profile = self.memory.empty_profile()
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 60, "doctor.level", "t")
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 40, "doctor.level", "t")
        self.memory.save_profile(profile, touch_updated_at=False)

        args = SimpleNamespace(field="doctor.level")
        rc = self.memory.command_dismiss(args)
        assert rc == 0
        loaded, _ = self.memory.load_profile()
        assert loaded["doctor"]["level"] == 60
        assert len(loaded["pending_confirmations"]) == 0

    def test_dismiss_no_match_returns_1(self):
        profile = self.memory.empty_profile()
        self.memory.save_profile(profile, touch_updated_at=False)
        args = SimpleNamespace(field="nonexistent.field")
        rc = self.memory.command_dismiss(args)
        assert rc == 1


class TestCommandRead:
    def test_read_shows_pending(self, capsys):
        profile = self.memory.empty_profile()
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 60, "doctor.level", "t")
        self.memory.merge_monotonic_int(profile, profile["doctor"], "level", 40, "doctor.level", "t")
        self.memory.save_profile(profile, touch_updated_at=False)

        args = SimpleNamespace()
        self.memory.command_read(args)
        captured = capsys.readouterr()
        assert "pending confirmation" in captured.err
        assert "doctor.level" in captured.err


class TestMigration:
    def test_migration_copies_legacy(self, isolated_memory_dir: Path, tmp_path: Path):
        legacy_dir = tmp_path / "legacy" / ".arknights-memory"
        legacy_dir.mkdir(parents=True)
        legacy_profile = {
            "schema_version": 1,
            "game": "Arknights",
            "metadata": {"created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z"},
            "doctor": {"name": "LegacyDoctor", "server": None, "level": None, "uid": None},
            "account": {"progress": {}, "resources": {}, "goals": [], "preferences": []},
            "operators": {},
            "pending_confirmations": [],
        }
        (legacy_dir / "doctor-profile.json").write_text(
            json.dumps(legacy_profile, ensure_ascii=False), encoding="utf-8"
        )
        new_path = isolated_memory_dir / "doctor-profile.json"
        assert not new_path.exists()

        import unittest.mock as mock
        with (
            mock.patch.object(self.memory, "skill_root", return_value=tmp_path / "legacy"),
            mock.patch.dict(os.environ, {"ARKNIGHTS_MEMORY_DIR": ""}, clear=False),
            mock.patch.object(self.memory, "profile_path", return_value=new_path),
        ):
            self.memory.migrate_legacy_if_needed()

        assert new_path.exists()
        loaded = json.loads(new_path.read_text(encoding="utf-8"))
        assert loaded["doctor"]["name"] == "LegacyDoctor"
        assert (legacy_dir / ".migrated").exists()

    def test_migration_skipped_when_env_set(self, isolated_memory_dir: Path, tmp_path: Path):
        self.memory.migrate_legacy_if_needed()
        new_path = isolated_memory_dir / "doctor-profile.json"
        assert not new_path.exists()


class TestEnvOverride:
    def test_env_override(self, tmp_path: Path):
        custom_dir = tmp_path / "custom"
        custom_dir.mkdir()
        os.environ["ARKNIGHTS_MEMORY_DIR"] = str(custom_dir)
        assert self.memory.memory_dir() == custom_dir.resolve()
        assert self.memory.profile_path() == custom_dir.resolve() / "doctor-profile.json"
