#!/usr/bin/env python3

from itertools import accumulate
from itertools import cycle


def solve(fd):

	# Calculate all the steps
	results = accumulate(
		int(line)
		for line in cycle(fd)
		if line
	)
	
	# Set to detect duplicates
	memory = set()
	
	# Stop when a duplicate is found
	for result in results:
		if result in memory:
			return result
		memory.add(result)


if __name__ == '__main__':	
	with open('day01.txt', 'r') as fd:
		print(solve(fd))
