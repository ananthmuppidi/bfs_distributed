#!/usr/bin/env python3
import sys

INF = sys.maxsize

def emit(node, distance, neighbors):
    # Emit the node with its distance and its adjacency list
    print(f"{node}\t{distance}|{','.join(neighbors)}")

current_node = None
current_distance = INF
current_neighbors = []
neighbors = None

for line in sys.stdin:
    line = line.strip()
    node_id, value = line.split('\t', 1)
    
    if '@' in value:
        new_distance = int(value.rstrip('@'))
    else:
        distance, neighbors_str = value.split('|', 1)
        new_distance = int(distance)
        neighbors = neighbors_str.split(',') if neighbors_str else []

    if current_node is None or current_node != node_id:
        if current_node is not None:
            emit(current_node, current_distance, current_neighbors)
        current_node = node_id
        current_distance = new_distance
        current_neighbors = neighbors if neighbors else []
    else:
        current_distance = min(current_distance, new_distance)
        if '@' not in value:
            current_neighbors = neighbors

if current_node is not None:
    emit(current_node, current_distance, current_neighbors)
