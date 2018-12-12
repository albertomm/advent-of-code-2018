#!/usr/bin/env python3
from collections import defaultdict
import re


def solve(fd):
    dependencies = _parse_input(fd)
    steps = _expand_dependencies(dependencies)
    sorted_steps = _sort_steps(steps)
    return ''.join(sorted_steps)


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


def _expand_dependencies(dependencies):
    """
    Calculate the complete dependencies for every step.
    """

    return {
        step: set(_get_all_step_dependencies(step, dependencies))
        for step in dependencies.keys()
    }


def _get_all_step_dependencies(step, dependencies):
    """
    Generate all the dependencies for a given step.
    """

    for dep in dependencies[step]:
        yield dep
        for x in _get_all_step_dependencies(dep, dependencies):
            yield x


def _sort_steps(steps):
    """
    Sort the steps with the given criteria.
    """

    pending = set(steps.keys())
    result = []
    done = set()

    while pending:

        next_step = sorted(filter(
            lambda x: steps[x] <= done,
            pending,
        ))[0]

        pending.remove(next_step)
        done.add(next_step)
        result.append(next_step)

    return result


if __name__ == '__main__':
    with open('day07.txt', 'r') as fd:
        print(solve(fd))
