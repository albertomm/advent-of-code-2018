#!/usr/bin/env python3

from itertools import chain
import string

# Example data for testing
DATAS = (
    open('day05.txt', 'r').read().strip(),
)


def solve_slow(original_data):
    """
    This is a brute force solution which subtracts all the possible reaction
    pairs again and again until nothing changes. As now we have to get a result
    for every unit type, it takes almost 7 seconds.
    """

    # Generate all the possible reaction pairs
    pairs = tuple(map(''.join, zip(
        chain(string.ascii_uppercase, string.ascii_lowercase),
        chain(string.ascii_lowercase, string.ascii_uppercase),
    )))

    # Find all distinct types present in the data
    types = sorted(set(original_data.lower()))

    # Calculate everything removing types
    result = len(original_data)
    for t in types:
        data = original_data.replace(t.lower(), '').replace(t.upper(), '')

        # Remove the reaction unit pairs from the sequence until no more are found
        prev_len = None
        while len(data) != prev_len:
            prev_len = len(data)
            for pair in pairs:
                data = data.replace(pair, '')

        # Keep only the lowest value
        result = min(len(data), result)
        print(t, len(data), result)

    return result


def solve_fast(original_data):
    """
    This solution attempts to remove all the reaction pairs in a single pass. It
    shouldn't take more than 50 milliseconds.
    """

    # Find all distinct types present in the data
    types = sorted(set(original_data.lower()))

    result = len(original_data)
    for t in types:

        data = original_data.replace(t.lower(), '').replace(t.upper(), '')

        cur = 0
        pos = 1
        jumps = [1]

        while (pos < len(data)):

            if data[cur].swapcase() != data[pos]:
                jumps.append(pos - cur)
                cur = pos
            else:
                if jumps:
                    cur -= jumps.pop()
                else:
                    jumps.append(pos - cur)
                    cur = pos

            pos += 1

        result = min(len(jumps), result)

    return result


if __name__ == '__main__':
    for data in DATAS:
        print(solve_fast(data))
