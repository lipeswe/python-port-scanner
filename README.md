# Python Port Scanner

A simple TCP port scanner written in Python to practice networking and cybersecurity fundamentals.

## Features

- Scan common TCP ports
- Timeout handling
- Simple terminal output

## How it works

The script uses Python's `socket` module to attempt TCP connections to a list of common ports.  
If the connection succeeds, the port is considered **open**.

## Usage

Run the script:

python scanner.py

Then enter a target host:

scanme.nmap.org

## Example Output

Scanning scanme.nmap.org

[OPEN] Port 80  
[CLOSED] Port 21  

## Technologies

- Python
- Socket library
- TCP networking

## Learning Goals

This project was created to practice:

- Network programming
- Basic reconnaissance techniques
- Python scripting for cybersecurity

## Project Evolution

Version 1
Basic TCP port scanner using Python sockets

Version 2
Added command-line arguments and custom port ranges

Version 3
Implemented multithreading to significantly improve scan speed