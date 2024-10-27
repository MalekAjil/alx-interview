#!/usr/bin/python3
"""Log Parsing"""

import sys
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip, _, _, date, _, request, status, size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        try:
            status = int(status)
            size = int(size)
        except ValueError:
            continue
        if status in status_codes:
            status_codes[status] += 1
        total_size += size
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
