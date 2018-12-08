#!/usr/bin/env python3

import re


def solve(fd):
    """
    Can this be done without the massive array?
    """

    # Create an square array
    fabric = [
        [0] * 1000
        for _ in range(1000)
    ]

    # Parse the input
    for claim in fd:
        match = re.match(r'#(\d+) @ (\d+)\,(\d+): (\d+)x(\d+)', claim)
        _, offset_x, offset_y, size_x, size_y = map(int, match.groups())

        # Paint the fabric with numbers, counting how many claims will share every square inch
        for x in range(offset_x, offset_x + size_x):
            for y in range(offset_y, offset_y + size_y):
                fabric[x][y] += 1

    # Count the square inches claimed by more than one
    return sum(
        xy > 1
        for x in fabric
        for xy in x
    )


if __name__ == '__main__':
    with open('day03.txt', 'r') as fd:
        print(solve(fd))
