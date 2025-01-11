#!/usr/bin/python3
"""Log Parsing"""


import sys


def print_stats(total_size, status_codes):
    """
    Prints the computed metrics.
    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary with the count of each status code.
    Returns:
        None
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip, _, _, date, _ = parts[0], parts[1], parts[2], parts[3], parts[4]
        request, status_code, file_size = parts[5], parts[6], parts[7]

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1

        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise


print_stats(total_size, status_codes)
