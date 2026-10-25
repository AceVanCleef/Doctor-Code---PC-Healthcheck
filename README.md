# Python Packaging & Installer Demo (PyInstaller + Inno Setup)

## Purpose of the Project

This repository serves as a hands-on reference project to explore and demonstrate how to bundle a Python application into a standalone Windows executable (`.exe`) using **PyInstaller** and package it into a professional Windows installer (`Setup.exe`) using **Inno Setup**.

## Tooling Overview: PyInstaller vs. Inno Setup

To convert a Python project into a distributable Windows application, two distinct tools are used:

| Tool                  | Primary Role                                                                                                                                                                                | Output                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **PyInstaller** | Compiles Python script files (`.py`), dependencies, and the Python runtime into a self-contained executable directory.                                                                    | `dist/` folder containing `.exe` and `_internal/` dependencies. |
| **Inno Setup**  | Packages the compiled executable folder into a single, user-friendly Windows Installation wizard (`Setup.exe`). Handles Start Menu shortcuts, uninstallation entries, and registry setup. | `Setup.exe` installer file.                                         |

### How They Work Together

1. **PyInstaller** freezes the application so that end users do not need Python installed on their machines.
2. **Inno Setup** takes the output of PyInstaller and creates a clean installation experience for end-user distribution.

> **Note on Version Control (`.gitignore`):**
> For educational and reference purposes, the `dist/` and `installer/` folders are intentionally tracked in this repository to showcase the compiled outputs. In production environments, built artifacts and binary outputs should **always be excluded** via `.gitignore` to keep repositories lightweight and clean.

## Useful Links

* **Inno Setup Downloads:** [jrsoftware.org/isdl.php](https://jrsoftware.org/isdl.php)
* **Inno Setup Documentation:** [jrsoftware.org/ishelp](https://jrsoftware.org/ishelp/)
* **PyInstaller Documentation:** [pyinstaller.org](https://pyinstaller.org/)

## Setup & Build Instructions

### 1. Prerequisites & Environment Setup

Clone the repository and set up a virtual environment:

```
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

### 2. Installing PyInstaller

PyInstaller can be installed via `pip`:

```
pip install pyinstaller

```

### 3. Building the Executable

Generate the standalone application using PyInstaller:

```
pyinstaller --noconsole src/doctor_check.py

```

### 4. Creating the Installer

1. Install **Inno Setup** on your Windows system.
2. Open the `installer/doctor_checker.iss` file in Inno Setup Compiler.
3. Click **Compile** (or press `F9`).
4. The generated installer will be placed in the `installer/` directory.
