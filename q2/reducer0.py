#!/usr/bin/env python3
import sys

current_node = None
friends = []

# Input comes from STDIN
for line in sys.stdin:
    # Remove whitespace at the start and end
    line = line.strip()

    # Parse the input we got from the mapper
    node, friend = line.split('\t')

    # If the current node is the same as the node we're processing, append the friend
    if current_node == node:
        friends.append(friend)
    else:
        # If it's a new node and not the first line
        if current_node:
            # Write the current node and its friends to STDOUT
            print(f'{current_node}\t{",".join(sorted(set(friends)))}')
        
        # Set the current node to the new node
        current_node = node
        # Start a new friends list
        friends = [friend]

# Output the last node if needed
if current_node == node:
    print(f'{current_node}\t{",".join(sorted(set(friends)))}')
