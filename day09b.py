#!/usr/bin/env python3
import re


def solve(fd):
    # Get the game settings from the input
    for num_players, last_marble_points in _parse_input(fd):
        last_marble_points *= 100
        score = _play(num_players, last_marble_points)
        print(
            "With %s players, until marble %s, the winner score is %s." % (
                num_players, 
                last_marble_points, 
                score
            )
        )

    return score


def _parse_input(fd):
    for line in fd:
        match = re.match(
            '(\d+) players; last marble is worth (\d+) points', line)
        if match:
            yield map(int, match.groups())


def _play(num_players, last_marble_points):

    scores = [0] * num_players
    circle = Marble(0)
    current = circle  # Points to the current marble

    for score in range(1, last_marble_points + 1):

        if score % 23:
            # Normal round
            current = current.nex.insert(score)
        else:
            # Score round
            current = current.pre.pre.pre.pre.pre.pre.pre
            points = score + current.value
            player = (score % num_players)
            scores[player] += points
            current = current.remove()

    return max(scores)


class Marble:

    def __init__(self, value):
        self.value = value
        self.nex = self
        self.pre = self

    def insert(self, value):
        """
        Insert a new marble between this and the next.
        """
        new = Marble(value)
        new.pre = self
        new.nex = self.nex
        self.nex.pre = new
        self.nex = new
        return new

    def remove(self):
        """
        Remove this marble from the circle.
        """
        self.pre.nex = self.nex
        self.nex.pre = self.pre
        return self.nex


if __name__ == '__main__':
    with open('day09.txt', 'r') as fd:
        print(solve(fd))
