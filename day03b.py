#!/usr/bin/env python3

import re


def solve(fd):

    claims = {}

    # Parse the input
    for claim in fd:
        match = re.match(r'#(\d+) @ (\d+)\,(\d+): (\d+)x(\d+)', claim)
        claim_id, offset_x, offset_y, size_x, size_y = map(int, match.groups())

        # Keep every claim as a vector
        claims[claim_id] = (
            (offset_x, offset_x + size_x),
            (offset_y, offset_y + size_y),
        )

    # Compare every claim with the others
    for claim_id, claim in claims.items():

        (ax1, ax2), (ay1, ay2) = claim

        for other_id, other in claims.items():

            # Don't compare a claim with itself
            if claim_id == other_id:
                continue

            (bx1, bx2), (by1, by2) = other

            # If some of these are true it means that the two claims don't overlap
            if ax1 >= bx2:
                continue
            if ax2 < bx1:
                continue
            if ay1 >= by2:
                continue
            if ay2 < by1:
                continue

            # The two claims share some fabric area
            break

        else:
            # The current claim don't overlap with any other
            return claim_id


if __name__ == '__main__':
    with open('day03.txt', 'r') as fd:
        print(solve(fd))
