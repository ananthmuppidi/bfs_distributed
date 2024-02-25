#!/usr/bin/env python3
import sys

INF = sys.maxsize

def emit(node, distance):
    print(f"{node}\t{distance}")

for _line in sys.stdin:
    line = _line.strip()
    node_id, value = line.split('\t', 1)
    if int(value) <= 10:
        emit(node_id, value)