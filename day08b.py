#!/usr/bin/env python3


def solve(fd):
    # Open and parse the input data stream
    data = map(int, fd.readline().split())

    # Walk all the nodes adding all the metadata
    metadata_sum = _walk_data(data)

    return metadata_sum


def _walk_data(data):
    """
    Recursively walk all the nodes, returning the value of the current node.
    """

    num_nodes = next(data)
    num_metadata = next(data)

    # Calculate the values from children nodes
    children_values = [0]
    for _ in range(num_nodes):
        children_values.append(_walk_data(data))

    # Get this node's metadata
    metadata = tuple(next(data) for _ in range(num_metadata))

    # Calculate this node's value
    if num_nodes:
        value = sum(
            children_values[x]
            for x in metadata
            if 0 < x < len(children_values)
        )
    else:
        value = sum(metadata)

    return value


if __name__ == '__main__':
    with open('day08.txt', 'r') as fd:
        print(solve(fd))
