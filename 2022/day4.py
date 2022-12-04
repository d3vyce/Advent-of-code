# Advent of Code 2022, Day 4, d3vyce

count = 0
count2 = 0

with open('input/day4.txt') as f:
	for line in f.read().splitlines():
		line = line.split(',')
		liste1 = [i for i in range(int(line[0].split('-')[0]), int(line[0].split('-')[1])+1)]
		liste2 = [i for i in range(int(line[1].split('-')[0]), int(line[1].split('-')[1])+1)]
		if len(set(liste1).intersection(liste2)) == len(liste1) or len(set(liste1).intersection(liste2)) == len(liste2):
			count += 1

		if len(set(liste1).intersection(liste2)) > 0 or len(set(liste1).intersection(liste2)) > 0:
			count2 += 1

print(f'Answer 1: {count}')

print(f'Answer 2: {count2}')