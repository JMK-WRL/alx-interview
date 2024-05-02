#!/usr/bin/python3

import sys

def print_stats(status_codes, total_file_size):
    """
    Print statistics
    Args:
        status_codes: dictionary of status codes
        total_file_size: total size of files
    Returns:
        None
    """
    print("Total File Size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))

total_file_size = 0
counter = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()[::-1]  # Splitting and reversing the line

        if len(parts) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parts[0])  # File size
                code = parts[1]  # Status code

                if code in status_codes:
                    status_codes[code] += 1

            if counter == 10:
                print_stats(status_codes, total_file_size)
                counter = 0

finally:
    print_stats(status_codes, total_file_size)
