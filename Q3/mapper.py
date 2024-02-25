#!/usr/bin/env python3
import sys

SOURCE_NODE = '1'  # Define the source node
MAX_DISTANCE = sys.maxsize

def emit(key, value):
    print(f"{key}\t{value}")
try:
    for _line in sys.stdin:
        line = _line.strip()
        if '|' in line:
            node_id, value = line.split('\t', 1)
            distance, neighbours = value.split('|', 1)
            distance = int(distance)
        else:
            parts = line.split()
            node_id = parts[0]
            neighbours = parts[1:]
            distance = 0 if node_id == SOURCE_NODE else MAX_DISTANCE
            neighbours = ','.join(neighbours)


        emit(node_id, f"{distance}|{neighbours}")

    # If this is not the initial input, also check and emit updates for neighbours
        if distance < MAX_DISTANCE:
            for neighbour in neighbours.split(','):
            # Emit potential distance update for each neighbour
                emit(neighbour, f"{distance + 1}@")
except Exception as e:
    sys.stderr.write(f"ERROR: {str(e)}\n")
    quit(127)