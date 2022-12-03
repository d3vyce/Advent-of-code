# Advent of Code 2022, Day 2, d3vyce

score = 0
score2 = 0
list = []

def add_score(input):
	if input.islower():
		return ord(input) - 96
	else:
		return ord(input) - 38

with open('input/day3.txt') as f:
	for line in f.read().splitlines():
		score += add_score(''.join(set(line[:int(len(line)/2)]).intersection(line[int(len(line)/2):])))
		list.append(line)
		if len(list) ==3 :
			score2 += add_score(''.join(set(list[0]).intersection(list[1], list[2])))
			list = []

print(f'Answer 1: {score}')

print(f'Answer 2: {score2}')
