#!/usr/bin/env python3
import sys

def emit(key, value):
    print(f"{key}\t{value}")
try:
    for _line in sys.stdin:
        line = _line.strip()
        node_id, value = line.split(' ', 1)
        distance, neighbours = value.split('|', 1)
        distance = int(distance)
        emit(node_id, distance)
except Exception as e:
    sys.stderr.write(f"ERROR: {str(e)}\n")
    quit(127)
    