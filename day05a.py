#!/usr/bin/env python3

from itertools import chain
import string

# Example data for testing
DATAS = (
    'cdeEDCBA',
    'abBA',
    'abAB',
    'aabAAB',
    'dabAcCaCBAcCcaDA',
    'adcCDeEa',
    open('day05.txt', 'r').read().strip(),
)


def solve_slow(data):
    """
    This is a brute force solution which subtracts all the possible reaction
    pairs again and again until nothing changes. As a result, it takes a quarter
    of a second to solve.
    """

    # Generate all the possible reaction pairs
    pairs = tuple(map(''.join, zip(
        chain(string.ascii_uppercase, string.ascii_lowercase),
        chain(string.ascii_lowercase, string.ascii_uppercase),
    )))

    # Remove the reaction unit pairs from the sequence until no more are found
    prev_len = None
    while len(data) != prev_len:
        prev_len = len(data)
        for pair in pairs:
            data = data.replace(pair, '')

    # Count the units that survive the reaction
    return len(data)


def solve_fast(data):
    """
    This solution attempts to remove all the reaction pairs in a single pass. It
    shouldn't take more than 50 milliseconds.
    """

    cur = 0
    pos = 1
    jumps = [1]

    while (pos < len(data)):

        if data[cur].swapcase() != data[pos]:
            jumps.append(pos - cur)
            cur = pos
        else:
            cur -= jumps.pop()

        pos += 1

    return len(jumps)


if __name__ == '__main__':
    for data in DATAS:
        print(solve_fast(data))
