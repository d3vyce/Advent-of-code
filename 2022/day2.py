# Advent of Code 2022, Day 2, d3vyce

with open('input/day2.txt') as f:
    file = [i for i in f.read().splitlines()]

score = 0
dic = {'X': 1, 'Y': 2, 'Z': 3}
#WIN
dic2 = {'A': 'Y', 'B': 'Z', 'C': 'X'}
#DRAW
dic3 = {'A': 'X', 'B': 'Y', 'C': 'Z'}
#LOSE
dic4 = {'A': 'Z', 'B': 'X', 'C': 'Y'}

for line in file:
	line = line.split()
	if dic2[line[0]] == line[1]:
		score += 6 + dic[line[1]]
	elif dic3[line[0]] == line[1]:
		score += 3 + dic[line[1]]
	else:
		score += dic[line[1]]

print(f'Answer 1: {score}')

score2 = 0

for line in file:
	line = line.split()
	if line[1] == 'Z':
		score2 += 6 + dic[dic2[line[0]]]
	elif line[1] == 'Y':
		score2 += 3 + dic[dic3[line[0]]]
	else:
		score2 += dic[dic4[line[0]]]

print(f'Answer 2: {score2}')