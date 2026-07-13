"""
config_manager.py

Handles loading and accessing the application's configuration.
"""

import json
from pathlib import Path
from typing import Any


class ConfigManager:
    """Loads and provides access to configuration settings."""

    def __init__(self, config_path: Path | None = None) -> None:
        """
        Initialize the configuration manager.

        Args:
            config_path: Optional path to a configuration file.
                         If not provided, the default config/config.json
                         file is used.
        """

        self._config_path = config_path or Path("config/config.json")
        self._config: dict[str, Any] = {}

        self.load()
        self.validate()

    def load(self) -> None:
        """Load configuration from the JSON file."""

        try:
            with self._config_path.open("r", encoding="utf-8") as file:
                self._config = json.load(file)

        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"Configuration file not found: {self._config_path}"
            ) from error

        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON in configuration file: {error}") from error

    def validate(self) -> None:
        """Validate required configuration sections."""

        required_sections = (
            "project",
            "repository",
            "watcher",
            "logging",
        )

        for section in required_sections:
            if section not in self._config:
                raise KeyError(f"Missing required configuration section: '{section}'")

    def get(self, key: str) -> Any:
        """
        Return a configuration value using dot notation.

        Example:
            config.get("project.name")
        """

        current: Any = self._config

        for part in key.split("."):
            current = current[part]

        return current

    def reload(self) -> None:
        """Reload and validate the configuration."""

        self.load()
        self.validate()
