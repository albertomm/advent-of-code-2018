#!/usr/bin/env python3

def solve(fd):
	return sum(map(int, fd))
	
if __name__ == '__main__':	
	with open('day01.txt', 'r') as fd:
		print(solve(fd))
