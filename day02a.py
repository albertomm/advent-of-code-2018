#!/usr/bin/env python3

from collections import Counter

def solve(fd):
	
	twos = 0
	threes = 0
	
	for line in fd:
		c = Counter(line)
		twos += 2 in c.values()
		threes += 3 in c.values()
	
	return twos * threes
		
		
		

if __name__ == '__main__':	
	with open('day02_input.txt', 'r') as fd:
		print(solve(fd))
