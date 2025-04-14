# WMIDriveShadow

A Python script to create Volume Shadow Copies for specified drives using Windows Management Instrumentation (WMI) and log the process.

## Overview

**WMIDriveShadow** is a lightweight Python tool that automates the creation of shadow copies (snapshots) for multiple drives on a Windows system. Leveraging the `Win32_ShadowCopy` WMI class, it generates persistent shadow copies and logs all operations to a file for easy tracking of successes or errors. Designed for backup automation, this script is particularly powerful when scheduled to run on Windows 10 and 11, making it ideal for recurring backup tasks.

## Features

- Creates shadow copies for multiple drives.
- Logs all operations with timestamps to a specified log file.
- Handles errors gracefully with detailed error messages.
- Simple and customizable drive list configuration.
- Easily schedulable on Windows 10 and 11 for automated backups.

## Requirements

- **Operating System**: Windows 10 or 11.
- **Python**: Version 3.x.
- **Python Module**: `wmi` (install via `pip install wmi`).
- **Permissions**: Must be run with administrative privileges.

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/WMIDriveShadow.git

   
