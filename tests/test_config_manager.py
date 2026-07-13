from pathlib import Path

import pytest

from leetcode_automation.managers.config_manager import ConfigManager

DATA_DIR = Path("tests/data")


def test_load_valid_config():
    config = ConfigManager(DATA_DIR / "valid_config.json")
    assert config.get("project.name") == "LeetCode Automation"


def test_missing_config_file():
    with pytest.raises(FileNotFoundError):
        ConfigManager(DATA_DIR / "does_not_exist.json")


def test_invalid_json():
    with pytest.raises(ValueError):
        ConfigManager(DATA_DIR / "invalid_json.json")


def test_missing_project_section():
    with pytest.raises(KeyError):
        ConfigManager(DATA_DIR / "missing_project.json")


def test_missing_repository_section():
    with pytest.raises(KeyError):
        ConfigManager(DATA_DIR / "missing_repository.json")


def test_missing_logging_section():
    with pytest.raises(KeyError):
        ConfigManager(DATA_DIR / "missing_logging.json")


def test_missing_watcher_section():
    with pytest.raises(KeyError):
        ConfigManager(DATA_DIR / "missing_watcher.json")


def test_invalid_key():
    config = ConfigManager(DATA_DIR / "valid_config.json")

    with pytest.raises(KeyError):
        config.get("project.invalid_key")


def test_reload():
    config = ConfigManager(DATA_DIR / "valid_config.json")
    config.reload()

    assert config.get("project.name") == "LeetCode Automation"
