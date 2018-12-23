#!/usr/bin/env python3


def solve(fd):
    # Open and parse the input data stream
    data = map(int, fd.readline().split())
    
    # Walk all the nodes adding all the metadata
    metadata_sum = _walk_data(data)
    
    return metadata_sum


def _walk_data(data):
    """
    Recursively walk all the nodes, returning the children metadata sum.
    """

    num_nodes = next(data)
    num_metadata = next(data)

    # Add the metadata sums from the children nodes
    children_metadata_sum = 0
    for _ in range(num_nodes):
        children_metadata_sum += _walk_data(data)

    # Calculate this node's metadata
    metadata = tuple(next(data) for _ in range(num_metadata))

    return sum(metadata) + children_metadata_sum


if __name__ == '__main__':
    with open('day08.txt', 'r') as fd:
        print(solve(fd))
