# LeetCode Automation Engine

A Python project that automates the repetitive work involved in maintaining a LeetCode repository.

Instead of manually updating your README, generating statistics, writing commit messages, and pushing changes to GitHub, this project handles those tasks automatically so you can focus on solving problems.

The project follows a modular architecture, making it easy to maintain and extend with new features.

---

## Why I Built This

While solving LeetCode problems, I noticed that keeping my GitHub repository updated required the same manual steps every time. This project was created to automate those repetitive tasks and keep the repository organized with minimal effort.

It also serves as a practical project to improve my Python skills and learn about automation, software design, and developer tooling.

---

## Features

- Automatically detect newly solved LeetCode problems
- Update the repository README
- Generate solution statistics
- Parse problem information
- Detect repository changes
- Automate Git operations (add, commit, push)
- JSON-based configuration
- Centralized logging
- Modular and extensible architecture
- Unit tests for core components

---

## Project Structure

```text
leetcode-automation/
│
├── assets/
├── config/
├── docs/
├── leetcode_automation/
│   ├── core/
│   ├── managers/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── data/
│
├── templates/
├── tests/
│
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/bhola910/leetcode-automation.git
```

Move into the project directory:

```bash
cd leetcode-automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Update the configuration file:

```text
config/config.json
```

Run the application:

```bash
python -m leetcode_automation
```

---

## Configuration

The project uses a JSON configuration file located in:

```text
config/config.json
```

You can configure options such as:

- Repository location
- Git settings
- Automation preferences
- Statistics generation

---

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_git_manager.py
```

---

## Project Architecture

## Project Architecture

The overall architecture is documented in:

> **docs/architecture.md**

This document explains the project components and how they interact.

---

## Roadmap

### v1.1.0 (Current)

- Improve project documentation
- Repository cleanup
- Professional README
- Better project structure

### v1.2.0

- GitHub Actions (CI)
- Issue templates
- Pull request template
- Improved test coverage

### v2.0.0

- Command Line Interface (CLI)

Example commands:

```bash
lae init
lae watch
lae stats
lae commit
```

### Future Plans

- Background automation service
- VS Code extension
- AI-assisted commit messages
- Analytics dashboard

---

## Contributing

Contributions are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add or update tests if needed.
5. Submit a Pull Request.

Please read the `CONTRIBUTING.md` file before contributing.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## Author

**Bhola Kumar**

B.Tech Computer Science student passionate about Python, automation, and developer tools.

---

If you find this project useful, consider giving it a ⭐ on GitHub.
