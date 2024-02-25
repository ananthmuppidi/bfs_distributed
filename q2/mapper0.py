#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    node1, node2 = line.split(' ', 1)
    print(f'{node1}\t{node2}')
    print(f'{node2}\t{node1}')
