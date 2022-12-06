# Advent of Code 2022, Day 6, d3vyce

with open('input/day6.txt') as f:
	line = f.read()
	for letter in range(4, len(line), 1):
		liste_tmp = line[letter-4:letter]
		if len(liste_tmp) == len(set(liste_tmp)):
			result = letter
			break

	for letter in range(14, len(line), 1):
		liste_tmp = line[letter-14:letter]
		if len(liste_tmp) == len(set(liste_tmp)):
			result2 = letter
			break

print(f'Answer 1: {result}')

print(f'Answer 2: {result2}')