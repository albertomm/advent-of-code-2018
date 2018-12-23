#!/usr/bin/env python3
import re


def solve(fd):
    # Get the game settings from the input
    for num_players, last_marble_points in _parse_input(fd):
        score = _play(num_players, last_marble_points)
        print(num_players, last_marble_points, score)

    return score


def _parse_input(fd):
    for line in fd:
        match = re.match(
            '(\d+) players; last marble is worth (\d+) points', line)
        if match:
            yield map(int, match.groups())


def _play(num_players, last_marble_points):

    scores = [0] * num_players
    circle = [0] # Start with a single marble without value
    current = 0 # Points to the current marble

    for score in range(1, last_marble_points + 1):

        if score % 23:
            # Normal round, add a marble
            current += 2
            current %= len(circle)
            circle.insert(current, score)
        else:
            # Score round
            current -= 7
            current %= len(circle)
            points = score + circle.pop(current)
            player = score % len(scores)
            scores[player] += points

    return max(scores)


if __name__ == '__main__':
    with open('day09.txt', 'r') as fd:
        print(solve(fd))
