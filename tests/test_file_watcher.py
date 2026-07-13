from leetcode_automation.core.automation_controller import AutomationController
from leetcode_automation.services.file_watcher import FileWatcher


def main():
    controller = AutomationController()

    watcher = FileWatcher(
        controller.process_solution
    )

    watcher.start()


if __name__ == "__main__":
    main()