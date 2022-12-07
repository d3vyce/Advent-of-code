# Advent of Code 2022, Day 7, d3vyce
from collections import defaultdict

Size = defaultdict(int)
Path = []
Count1 = 0

with open('input/day7.txt') as f:
	for line in f.read().splitlines():
		line = line.split(' ')
		if line[1] == 'cd':
			if line[2] == '..':
				Path.pop()
			else:
				Path.append(line[2])
		elif line[1] == 'ls' or line[0] == 'dir':
			continue
		else:
			file_size = int(line[0])
			for i in range(1, len(Path)+1):
				Size['/'.join(Path[:i])] += file_size

need_space = 30000000 - (70000000 - Size['/'])
Count2 = Size['/']

for size in Size:
	if Size[size] <= 100000:
		Count1 += Size[size]
	if Size[size] > need_space and Size[size] - need_space < Count2:
		Count2 = Size[size]

print(f'Answer 1: {Count1}')

print(f'Answer 1: {Count2}')
