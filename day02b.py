#!/usr/bin/env python3

from itertools import combinations

def solve(fd):
	
	pairs = combinations(map(str.strip, fd), 2)
	
	for a, b in pairs:

		sa = set(enumerate(a))
		sb = set(enumerate(b))
		
		if len(sa - sb) == 1:
			return ''.join(x for _, x in sorted(sa & sb))

if __name__ == '__main__':	
	with open('day02_input.txt', 'r') as fd:
		print(solve(fd))
