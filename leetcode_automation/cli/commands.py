"""Command handlers for the LeetCode Automation Engine CLI."""

from leetcode_automation.managers.config_manager import ConfigManager
from leetcode_automation import __version__


def init_command() -> None:
    """Initialize the application."""
    print("Initializing LeetCode Automation Engine...")


def watch_command() -> None:
    """Watch for new LeetCode solutions."""
    print("Watching for new LeetCode solutions...")


def stats_command() -> None:
    """Generate repository statistics."""
    print("Generating repository statistics...")


def commit_command() -> None:
    """Commit and push repository changes."""
    print("Committing repository changes...")


def config_command() -> None:
    """Display the current application configuration."""

    config = ConfigManager()

    print("\nLeetCode Automation Engine Configuration")
    print("=" * 50)

    print("\nProject")
    print("-" * 50)
    print(f"Name       : {config.get('project.name')}")
    print(f"Version    : {config.get('project.version')}")

    print("\nRepository")
    print("-" * 50)
    print(f"Path       : {config.get('repository.path')}")
    print(f"Branch     : {config.get('repository.branch')}")
    print(f"Remote     : {config.get('repository.remote')}")

    print("\nWatcher")
    print("-" * 50)
    print(f"Directory  : {config.get('watcher.directory')}")
    print(f"Extensions : {', '.join(config.get('watcher.extensions', []))}")
    print(f"Debounce   : {config.get('watcher.debounce_seconds')} seconds")

    print("\nLogging")
    print("-" * 50)
    print(f"File       : {config.get('logging.file')}")
    print(f"Level      : {config.get('logging.level')}")


def version_command() -> None:
    """Display application version."""
    print(f"LeetCode Automation Engine v{__version__}")
