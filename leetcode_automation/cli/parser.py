"""Argument parser for the LeetCode Automation Engine."""

from __future__ import annotations

import argparse

from leetcode_automation.cli.commands import (
    commit_command,
    config_command,
    init_command,
    stats_command,
    version_command,
    watch_command,
)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="lae",
        description="LeetCode Automation Engine",
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        required=True,
    )

    init_parser = subparsers.add_parser(
        "init",
        help="Initialize the application",
    )
    init_parser.set_defaults(func=init_command)

    watch_parser = subparsers.add_parser(
        "watch",
        help="Watch for new LeetCode solutions",
    )
    watch_parser.set_defaults(func=watch_command)

    stats_parser = subparsers.add_parser(
        "stats",
        help="Generate repository statistics",
    )
    stats_parser.set_defaults(func=stats_command)

    commit_parser = subparsers.add_parser(
        "commit",
        help="Commit repository changes",
    )
    commit_parser.set_defaults(func=commit_command)

    config_parser = subparsers.add_parser(
        "config",
        help="Show configuration",
    )
    config_parser.set_defaults(func=config_command)

    version_parser = subparsers.add_parser(
        "version",
        help="Show application version",
    )
    version_parser.set_defaults(func=version_command)

    return parser


def main() -> None:
    """Parse CLI arguments and execute the selected command."""

    parser = create_parser()
    args = parser.parse_args()
    args.func()
