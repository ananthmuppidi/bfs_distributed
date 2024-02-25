#!/usr/bin/env python3
import sys
import itertools

def emit(key, value):
    print(f"{key}\t{value}")

def main():
    for line in sys.stdin:
        node, neighbors_str = line.strip().split('\t', 1)
        neighbors = neighbors_str.split(',')

        for neighbor1, neighbor2 in itertools.combinations(neighbors, 2):
            sorted_pair = tuple(sorted((neighbor1, neighbor2)))
            emit(",".join(sorted_pair), node)

if __name__ == "__main__":
    main()
