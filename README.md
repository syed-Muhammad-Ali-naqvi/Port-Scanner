# Port Scanner in Python

This is a basic port scanner built using Python and the `socket` library. The tool allows you to scan a specified range of ports on one or more target systems to determine if the ports are open or closed.

## Features
- Scans up to 65,535 TCP ports.
- Handles both single and multiple target IP addresses (separated by commas).
- Configurable timeout for each connection attempt.
- Validates user input for targets and port range.

## Requirements
- Python 3.x
- No additional libraries required (uses built-in `socket` module).

## Installation
1. Ensure Python 3.x is installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the project directory using a terminal or command prompt.

## Usage

1. Open a terminal in the directory where the script is located.
2. Run the script using the command:

    ```bash
    python port_scanner.py
    ```

3. You will be prompted to enter the target IP(s) to scan and the number of ports to scan (between 1 and 65,535). For multiple targets, separate the IPs with commas.

Example:

```bash
[*] Enter targets to scan (separated by commas): 192.168.1.1, 192.168.1.2
[*] Enter the number of ports to scan (1–65535): 1024
