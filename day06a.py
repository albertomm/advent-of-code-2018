#!/usr/bin/env python3

from collections import Counter
from pprint import pprint
from string import ascii_letters

# Set to true to paint a crude map of the areas (big!)
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
        [None] * limit_x
        for _ in range(limit_y)
    ]

    # Calculate the closest location for each point of the grid
    # TODO: optimize this
    print('Calculating distances...')
    for grid_x, column in enumerate(grid):
        for grid_y, _ in enumerate(column):

            distances = sorted(
                (abs(grid_x - location_x) + abs(grid_y - location_y), location_id)
                for location_id, (location_x, location_y) in enumerate(locations)
            )

            if distances[0][0] != distances[1][0]:
                closer = distances[0][1]
                grid[grid_x][grid_y] = closer

    print('Done.')

    # Find the infinite areas by looking at the grid edges
    edges = set()
    edges |= set(grid[0])
    edges |= set(grid[-1])
    edges |= set(col[0] for col in grid)
    edges |= set(col[-1] for col in grid)
    edges.discard(None)  # Seams aren't edges
    print('Edges:', sorted(ascii_letters[x] for x in edges))

    # Sum the grid points to calculate the areas
    areas = Counter()
    for col in grid:
        areas.update(col)

    # Remove edges and seams from the areas
    for edge in edges:
        del areas[edge]
    del areas[None]

    if PAINT_GRID:
        paint_grid(grid, locations)

    print('Areas:', sorted((ascii_letters[x], y) for x, y in areas.items()))
    return areas.most_common(1)


def paint_grid(grid, locations):
    # Paint the grid
    for x, col in enumerate(grid):
        for y, point in enumerate(col[:400]):

            if (x, y) in locations:
                print('*', end='')
            elif point is None:
                print('_', end='')
            else:
                print(ascii_letters[point], end='')
        print()


if __name__ == '__main__':
    with open('day06.txt', 'r') as fd:
        print(solve(fd))
