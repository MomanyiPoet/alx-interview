#!/usr/bin/python3

import sys
import signal

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
counts = {status: 0 for status in status_codes}
total_size = 0
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for status, count in sorted(counts.items()):
        if count > 0:
            print("{}: {}".format(status, count))

def reset_stats():
    global counts, total_size, line_count
    counts = {status: 0 for status in status_codes}
    total_size = 0
    line_count = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    # Parse the line
    try:
        parts = line.split()
        if len(parts) != 7:
            continue
        status = int(parts[5])
        size = int(parts[6])
        if status not in status_codes:
            continue
    except ValueError:
        continue

    # Update metrics
    counts[status] += 1
    total_size += size
    line_count += 1

    # Print stats
    if line_count % 10 == 0:
        print_stats()
