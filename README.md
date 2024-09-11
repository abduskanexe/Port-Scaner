# 🔍 Port Scanner

## Description
This project is a simple **port scanner** developed in **Python** to enhance my programming skills and automate security tools like **Nmap**. The scanner helps identify open ports on a specified IP address or range of IPs, allowing users to evaluate the exposure of services on a networked machine.

## Features
- Scans for open ports in a specified range or defaults to common ports.
- Basic integration with **Nmap** for detailed port information.
- Easy to use via command-line interface.
- Supports multiple IP addresses or ranges of IPs.

## Requirements
- **Python 3.x**
- The `socket` library (included with Python installation).
- Optional: [Nmap](https://nmap.org/) for advanced port scanning.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/abduskanexe/Port-Scanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Port-Scanner
    ```    
3. Make sure you have all the necessary dependencies installed. If you wish to use Nmap, install it following the official [Nmap installation guide](https://nmap.org/book/inst-windows.html).

## Usage

### Basic Execution
To run the basic port scanner:
```bash
python port_scanner.py -t <IP/Host> -p <port_range>
```

