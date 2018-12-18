#!/usr/bin/env python3
from collections import defaultdict
from itertools import zip_longest
from string import ascii_uppercase
import re

TIMES = {
    letter: 60 + index
    for index, letter in enumerate(ascii_uppercase, 1)
}


def solve(fd):
    dependencies = _parse_input(fd)
    return _do_work(dependencies, 5)


def _parse_input(fd):
    """
    Extract the dependencies from the input data, as a dictionary of
    step: set(dependencies).
    """

    expr = r'Step (\w) must be finished before step (\w) can begin.'
    dependencies = defaultdict(set)
    for line in fd:
        match = re.match(expr, line)
        if match:
            dependency, step = match.groups()
            dependencies[step].add(dependency)
            dependencies[dependency]
    return dependencies


def _do_work(dependencies, num_workers):

    workers = [[] for _ in range(num_workers)]

    steps_pending = set(dependencies)
    timeline = []

    loops = 0
    while steps_pending:
        loops += 1

        # Get the first idle worker
        current_worker = sorted(workers, key=lambda x: len(x))[0]

        # Calculate the steps already done when this worker gets idle
        done = set(
            step
            for t, step in timeline
            if t <= len(current_worker)
        )

        # Find the next step that can be done
        doable = (
            step
            for step in steps_pending
            if dependencies[step] <= done
        )

        try:
            step = next(doable)
        except StopIteration:
            # Nothing can be done for now, so we advance in time all idle
            # workers

            # Find the next event time
            next_event = min(
                t
                for t, _ in timeline
                if t > len(current_worker)
            )

            # Advance all workers to the next event time
            for w in workers:
                if len(w) <= len(current_worker):
                    w.extend(['.'] * (next_event - len(w)))
        else:
            # Make the current worker do the step
            print('Step:', step, ''.join(sorted(dependencies[step])))
            current_worker.extend([step] * TIMES[step])

            # Set the current step as done
            steps_pending.remove(step)

            # Remember when this step will be completed
            timeline.append((len(current_worker), step))

    # Print a visual representation of the workers
    for second, jobs in enumerate(zip_longest(*workers, fillvalue='.')):
        print(str(second).ljust(2), ' '.join(jobs))

    print('Loops:', loops)
    return max(map(len, workers))


if __name__ == '__main__':
    with open('day07.txt', 'r') as fd:
        print(solve(fd))
