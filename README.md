# LeetCode Automation Engine

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/bhola910/leetcode-automation)
![Last Commit](https://img.shields.io/github/last-commit/bhola910/leetcode-automation)
![Issues](https://img.shields.io/github/issues/bhola910/leetcode-automation)
![Stars](https://img.shields.io/github/stars/bhola910/leetcode-automation?style=social)

A Python project that automates the repetitive work involved in maintaining a LeetCode repository.

Instead of manually updating your README, generating statistics, writing commit messages, and pushing changes to GitHub, this project automates those tasks so you can focus on solving coding problems. The project is built with a modular architecture that is easy to maintain, extend, and scale as new features are added.

---

# Why I Built This

While solving LeetCode problems, I realized that keeping my GitHub repository updated involved repeating the same manual steps after every solution. I wanted a tool that could automatically organize my repository, generate statistics, update documentation, and handle Git operations.

This project also serves as a practical way to strengthen my Python skills while learning software architecture, automation, developer tooling, and best engineering practices.

---

# Features

## Current Features

- Detect newly solved LeetCode problems
- Automatically update the project README
- Generate solution statistics
- Parse LeetCode problem information
- Detect repository changes
- Automate Git operations (add, commit, push)
- JSON-based configuration
- Centralized logging
- Modular architecture
- Unit testing support
- GitHub Actions (CI)
- Issue Templates
- Pull Request Template
- CODEOWNERS support

---

# Project Structure

```text
leetcode-automation/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   ├── workflows/
│   └── CODEOWNERS
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
├── templates/
├── tests/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

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

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Configure the project by editing:

```text
config/config.json
```

Run the application:

```bash
python -m leetcode_automation
```

---

# Configuration

The application uses a JSON configuration file located at:

```text
config/config.json
```

Configuration options include:

- Repository location
- Git settings
- Automation preferences
- Statistics generation
- Logging options

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_git_manager.py
```

---

# Project Architecture

The complete system architecture is documented in:

```text
docs/architecture.md
```

The document explains:

- Project layers
- Module responsibilities
- Data flow
- Design decisions
- Future scalability

---

# Roadmap

## v1.1.0 ✅ Repository Foundation

Completed:

- Professional README
- Project documentation
- CHANGELOG
- CONTRIBUTING guide
- MIT License
- GitHub Actions (CI)
- Issue Templates
- Pull Request Template
- CODEOWNERS
- Repository cleanup
- Professional Git workflow

---

## v2.0.0 🚧 Automation Engine

Planned features:

- Command Line Interface (CLI)
- Configuration manager
- File watcher
- Git automation
- Statistics engine
- README generator
- LeetCode parser

Example commands:

```bash
lae init
lae watch
lae stats
lae commit
```

---

## Future Roadmap

- Background automation service
- AI-assisted commit messages
- VS Code extension
- Analytics dashboard
- Plugin support
- Multi-platform installer

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Add or update tests where appropriate.
5. Submit a Pull Request.

Please read **CONTRIBUTING.md** before contributing.

---

# License

This project is licensed under the MIT License.

See the **LICENSE** file for complete details.

---

# Author

**Bhola Kumar**

B.Tech Computer Science student passionate about Python, automation, developer tools, and building practical software projects.

---

If you find this project useful, consider giving it a ⭐ on GitHub. Your support helps the project grow and motivates future development.
