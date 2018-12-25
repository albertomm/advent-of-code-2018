#!/usr/bin/env python3

from PIL import Image
from itertools import count
import re


def solve(fd):
    points = _parse_input(fd)
    for frame in count():
        _move_points()
        _draw_points('%06d' % frame, points)
    print('Done')


def _parse_input(fd):
    points = []
    pattern = re.compile("position=<([ \-]\d+), ([ \-]\d+)> velocity=<([ \-]\d+), ([ \-]\d+)>")
    for line in fd:
        match = pattern.match(line)
        points.append(list(map(int, match.groups())))
    return points


def _move_points(points):
    """
    Advance in time applying the velocity to every point.
    """
    for point in points:
        point[0] += point[2]
        point[1] += point[3]


def _draw_points(frame, points):
    """
    Draw an image with the points.

    * Limit the size of the image to a small viewport in the center.

    * Don't create the image if any point is still outside of the viewport.
    """

    points_to_draw = []
    for x, y, *_ in points:
        if -250 < x < 250 and -250 < y < 250:
            points_to_draw.append((
                x,
                y,
            ))
        else:
            print(x, y)
            break
    else:
        image = Image.new('1', (500, 500))
        for x, y in points_to_draw:
            image.putpixel((x, y), 1)
        image.save('frame_%s.png' % frame)


if __name__ == '__main__':
    with open('day10.txt', 'r') as fd:
        print(solve(fd))
