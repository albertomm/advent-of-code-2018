#!/usr/bin/env python3
from unittest.case import TestCase


def solve(fd):
    serial = _parse_input(fd)
    return _calculate_grid(serial, 300)


def _parse_input(fd):
    for line in fd:
        return int(line.strip())


def _calculate_grid(serial, size):
    """
    Solve a grid with the specified serial and size.
    """
    grid = _build_empty_grid(size)

    for x in range(size):
        for y in range(size):
            level = _calculate_power_level(serial, x + 1, y + 1)
            _add_to_grid(grid, level, x, y)

    return _find_biggest_power(grid)


def _build_empty_grid(size):
    return [[0] * size for _ in range(size)]


def _calculate_power_level(serial, x, y):
    """
    Calculate the power level for a pair of coordinates.
    """
    result = (((x + 10) * y) + serial) * (x + 10)
    result = int(str(result)[-3])
    result -= 5
    return result


def _add_to_grid(grid, power, x, y):
    """
    Apply the calculated power level to the cells affected.
    """
    for a in range(max(0, x - 2), x + 1):
        for b in range(max(0, y - 2), y + 1):
            grid[a][b] += power


def _find_biggest_power(grid):

    big_x = None
    big_y = None
    power = None

    for x, col in enumerate(grid, 1):
        for y, cell in enumerate(col, 1):
            if power is None or cell > power:
                power = cell
                big_x = x
                big_y = y

    return big_x, big_y, power


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
        cases = (
            (18, 33, 45, 29),
            (42, 21, 61, 30),
        )

        for serial, *expected in cases:
            result = _calculate_grid(serial, size)
            self.assertSequenceEqual(result, expected)
