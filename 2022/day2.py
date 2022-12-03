# Advent of Code 2022, Day 2, d3vyce

with open('input/day2.txt') as f:
    file = [i for i in f.read().splitlines()]

score = 0
score2 = 0

for line in file:
	line = line.split()
	# Part 1
	if (ord(line[1]) - ord(line[0]))%3 == 0:
		score += 6 + (ord(line[1])%4) + 1
	elif (ord(line[1]) - ord(line[0]))%3 == 2:
		score += 3 + (ord(line[1])%4) + 1
	else:
		score += (ord(line[1])%4) + 1

	# Part 2
	if line[1] == 'Z':
		score2 += 6 + ((ord(line[0])-1)%3)+1
	elif line[1] == 'Y':
		score2 += 3 + ord(line[0])%4
	else:
		score2 += ((ord(line[0]))%3)+1


print(f'Answer 1: {score}')

print(f'Answer 2: {score2}')
