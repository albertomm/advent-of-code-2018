#!/usr/bin/env python3

"""
Example input:

[1518-09-02 00:00] Guard #2137 begins shift
[1518-05-01 00:45] falls asleep
[1518-08-15 00:47] wakes up
"""

from collections import Counter
from collections import defaultdict
import re


class Solver(object):

    GUARD_EXPR = r'\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] Guard #(\d+) begins shift'
    SLEEP_EXPR = r'\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] falls asleep'
    AWAKE_EXPR = r'\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] wakes up'

    def __init__(self, fd):
        """Set up the initial state and begin processing the input data."""

        # Registry of the guards and the minutes in which they sleep
        self.guards = defaultdict(Counter)

        # Current shift's guard
        self.guard = None

        # Current guard's sleep minute start
        self.sleep_minute = None

        self.event_processors = (
            (self.GUARD_EXPR, self._begin_shift),
            (self.SLEEP_EXPR, self._fall_asleep),
            (self.AWAKE_EXPR, self._wake_up),
        )

        # Parse the input
        for event in sorted(fd):
            self._process_event(event)

    def __str__(self):
        """Return the answer."""
        worst_guard = self.find_worst_guard()
        best_minute = self.find_best_minute(worst_guard)
        return str(worst_guard * best_minute)

    def _process_event(self, event):
        """Parse the event, find and apply the related action method."""

        for expr, processor in self.event_processors:
            match = re.match(expr, event)
            if match:
                return processor(match)

    def _begin_shift(self, match):
        """Process a shift guard change."""

        _, _, _, _, _, self.guard = map(int, match.groups())
        self.sleep_minute = None

    def _fall_asleep(self, match):
        """The current guard falls asleep."""

        _, _, _, _, self.sleep_minute = map(int, match.groups())

    def _wake_up(self, match):
        """The current guard wakes up."""

        _, _, _, _, awake_minute = map(int, match.groups())
        minutes_asleep = range(self.sleep_minute, awake_minute)
        self.guards[self.guard].update(minutes_asleep)
        self.sleep_minute = None

    def find_worst_guard(self):
        """Find the guard which has been asleep the most."""

        _, worst_guard = max(
            (sum(minutes.values()), guard)
            for guard, minutes in self.guards.items()
        )
        return worst_guard

    def find_best_minute(self, guard=None):
        """Find the minute with the highest probability of a guard being asleep.
        If a guard is not provided, the worst guard will be used.
        """
        guard = guard or self._find_worst_guard()
        (best_minute, _), = self.guards[guard].most_common(1)
        return best_minute


if __name__ == '__main__':
    with open('day04.txt', 'r') as fd:
        print(Solver(fd))
