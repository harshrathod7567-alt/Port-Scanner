# Port Scanner

A beginner Python project that scans a target for open network ports — 
useful for understanding network exposure and basic reconnaissance, a foundational security skill.

## What it does
- Scans a range of ports (default: 1–1024, the "well-known ports") on a target
- Reports which ports are open
- Times the scan and saves results to a report file

## ⚠️ Legal note
Only scan systems you own or have explicit permission to scan. 
This project defaults to scanning `127.0.0.1` (localhost — your own machine) for safe practice.

## Files
- `port_scanner.py` — the main script
- `scan_report.txt` — generated report (created after running the script)

## How to run it
1. Run: `python port_scanner.py`
2. Check the terminal output and `scan_report.txt` for results

## Example output
Scanning 127.0.0.1 from port 1 to 1024...
Port 445 is OPEN

Scan finished in 8.42 seconds
Report saved to scan_report.txt

## What I learned
- How TCP sockets work in Python (`socket` module)
- The basics of what "open" vs "closed" ports mean
- How reconnaissance tools like Nmap work at a conceptual level

## Next steps
- Add multithreading to speed up scans significantly
- Add command-line arguments for custom target/port range
- Map common port numbers to their known services (e.g., 22 = SSH, 80 = HTTP)
