#!/usr/bin/env python3

from pprint import pprint
from string import ascii_letters

# Set to true to paint a crude map of the grid (big!)
PAINT_GRID = False


def solve(fd):

    # Parse the data and get the locations as X, Y
    locations = []
    for line in fd:
        if line:
            x, _, y = line.partition(',')
            x = int(x)
            y = int(y)
            locations.append((x, y))
    pprint(locations)

    # Calculate the grid limits
    limit_x = max(x for x, y in locations)
    limit_y = max(y for x, y in locations)
    print('Limits:', limit_x, limit_y)

    # Prepare an empty grid
    grid = [
        [0] * limit_x
        for _ in range(limit_y)
    ]

    # Calculate each point's sum of distances
    print('Calculating scores...')
    for grid_x, column in enumerate(grid):
        for grid_y, _ in enumerate(column):

            score = sum(
                abs(grid_x - location_x) + abs(grid_y - location_y)
                for location_x, location_y in locations
            )

            grid[grid_x][grid_y] = score

    print('Done.')

    area = 0
    for x, column in enumerate(grid):
        for y, score in enumerate(column):
            if score < 10000:
                area += 1
                grid[x][y] = '#'
            else:
                grid[x][y] = '.'

    if PAINT_GRID:
        paint_grid(grid, locations)

    return area


def paint_grid(grid, locations):
    # Paint the grid
    for x, col in enumerate(grid):
        for y, char in enumerate(col[:400]):
            if (x, y) in locations:
                char = ascii_letters[locations.index((x, y))]
            print(char, end='')
        print()


if __name__ == '__main__':
    with open('day06.txt', 'r') as fd:
        print(solve(fd))
