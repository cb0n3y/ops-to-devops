# 🖥️ Bash Scripts

This folder contains Bash scripts used across various experiments, prototypes, and utilities under the `lab/` workspace. These scripts are written to solve practical problems, assist in daily system tasks, and support DevOps workflows.

## 🎯 Purpose

- Provide reusable, easy-to-understand automation scripts.
- Support daily tasks and system operations.
- Facilitate experimentation and testing in a controlled environment.
- Serve as a library of useful Bash utilities developed over time.

## 🗂️ Directory Structure

Each script in this directory serves a distinct purpose:

```bash
lab/scripts/bash
└── README.md
```

Scripts can be executed directly or adapted into larger automation workflows.

## 🚀 Usage

1. Ensure the script has execute permissions:
    ```bash
    chmod +x script-name.sh
    ```
2. Run the script from the terminal:
    ```bash
    ./script-name.sh
    ```
3. Scripts are designed to be adapted to your local environment or integrated into broader workflows.

## 🧩 Adding New Scripts

When contributing new Bash scripts to this directory, please follow these guidelines for consistency and clarity:

### ✅ File Naming

- Use **descriptive, lowercase file names**.
- Separate words with hyphens (`-`), not underscores (`_`), for better readability and consistency with Unix conventions.

**Preferred:**
- ✅ `export-keys.sh`
- 🚫 `export_keys.sh`

> Hyphens are more idiomatic in shell script naming (just like command-line tools: `systemctl`, `apt-get`, etc.).

## 🛠️ Script Structure
Each script must include:

1. Shebang line at the top:

```bash
#!/bin/bash
```

2. Header comment block documenting the script:
```bash
#!/bin/bash
#
# Description: Export system SSH or GPG keys to a secure location
# Usage: ./export-keys.sh [destination_directory]
# Author: cb0n3y
# Created: 2025-06-25
```
3. Meaningful, readable code with inline comments if necessary.