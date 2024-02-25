#!/usr/bin/env python3
import sys

current_key = None
friends = []




# sorted(set(lst))
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')

    # If the current node is the same as the node we're processing, append the friend
    if current_key == key:
        friends.append(value)
    else:
        if current_key:
            output = str(current_key)
            output = current_key.replace(",", " ")
            print(f'{output}\t{" ".join(sorted(set(friends)))}')
        
        current_key = key
        friends = [value]

# Output the last node if needed
if current_key == key:
    output = str(current_key)
    output = current_key.replace(",", " ")
    print(f'{output}\t{" ".join(sorted(set(friends)))}')
