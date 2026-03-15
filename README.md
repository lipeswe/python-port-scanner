# Python Port Scanner

A simple **multithreaded TCP port scanner written in Python** to practice networking and cybersecurity fundamentals.

This project demonstrates how port scanning works at a low level using Python sockets.

---

## Features

- TCP port scanning
- Custom port range
- Configurable number of threads
- Hostname resolution
- Scan duration measurement

---

## How It Works

The script attempts to establish TCP connections to a range of ports on a target host.

If a connection succeeds, the port is considered **open**.

The scanner uses:

- Python `socket` module for network connections
- `threading` for parallel scanning
- `argparse` for command-line arguments

---

## Usage

Run the script:

```bash
python scanner.py <target>