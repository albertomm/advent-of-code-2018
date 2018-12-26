#!/usr/bin/env python3
from unittest.case import TestCase


def solve(fd):
    serial = _parse_input(fd)
    return _calculate_grid(serial, 300, 300)


def _parse_input(fd):
    for line in fd:
        return int(line.strip())


def _calculate_grid(serial, size, area):
    """
    Solve a grid with the specified serial, size and area.
    """
    base = _calculate_base_grid(serial, size)
    grid = _expand_base_grid(base, area)
    return _find_biggest_power(grid)


def _calculate_base_grid(serial, size):
    """
    The base grid is the values of every individual cell, without adding the
    values of its area.
    """
    return [
        [
            _calculate_power_level(serial, x + 1, y + 1)
            for y in range(size)
        ]
        for x in range(size)
    ]


def _calculate_power_level(serial, x, y):
    """
    Calculate the power level for an individual cell.
    """
    result = (((x + 10) * y) + serial) * (x + 10)
    result = int(str(result)[-3])
    result -= 5
    return result


def _expand_base_grid(base_x, max_area):
    """
    Using the precalculated levels for an area of 1, calculate the rest of the
    possible areas until max_area.
    """

    size_x = len(base_x)
    size_y = len(base_x[0])

    # Rotate the base levels, changing columns per row and vice-versa.
    # This will allow avoiding many iterations when calculating the real values.
    base_y = [
        [base_x[x][y] for x in range(size_x)]
        for y in range(size_y)
    ]

    # The current grid, starting with a copy of the base grid
    current = [
        list(col)
        for col in base_x
    ]

    # Area of 1x1
    yield current

    # Modify the current grid for the rest of the areas
    for n in range(2, max_area + 1):

        if not n % 10:
            print('Level ', n)

        for x in range(size_x):
            for y in range(size_y):

                col_x = x + n - 1
                row_y = y + n - 1

                plus = 0

                # This is the slow part
                if col_x < size_x:
                    plus += sum(base_x[col_x][y: row_y + 1])
                if row_y < size_x:
                    plus += sum(base_y[row_y][x: col_x])
                current[x][y] += plus

        yield current


def _find_biggest_power(grid):
    """
    Iterate all the cell and area combinations and find the one with the highest
    power level.
    """

    big_x = None
    big_y = None
    big_z = None
    power = None

    for z, level in enumerate(grid, 1):
        for x, col in enumerate(level, 1):
            for y, cell in enumerate(col, 1):
                if power is None or cell > power:
                    power = cell
                    big_x = x
                    big_y = y
                    big_z = z

    return big_x, big_y, big_z, power


if __name__ == '__main__':
    with open('day11.txt', 'r') as fd:
        print(solve(fd))


class Tests(TestCase):

    def test_calculate_power_level(self):

        cases = (
            (3, 5, 8, 4),
            (122, 79, 57, -5),
            (217, 196, 39, 0),
            (101, 153, 71, 4),
        )

        for x, y, serial, expected in cases:
            result = _calculate_power_level(serial, x, y)
            self.assertEqual(result, expected)

    def test_integration(self):

        size = 300
        levels = 3
        cases = (
            (18, 33, 45, 3, 29),
            (42, 21, 61, 3, 30),
        )

        for serial, *expected in cases:
            result = _calculate_grid(serial, size, levels)
            self.assertSequenceEqual(result, expected)
