# Advent of Code 2022, Day 10, d3vyce

X = 1
i = 0
result = []

print(f'Answer 2: ')

def test(X, i):
	liste = [20, 60, 100, 140, 180, 220, 260]
	if i in liste:
		return i*X
	return 0

def print_operations(X, i):
	liste = [41, 81, 121, 161, 201, 241]
	if i in liste:
		print()
	if abs(X-((i-1)%40)) <= 1:
		print("#", end="")
	else:
		print(" ", end="")

with open('input/day10.txt') as f:
	for line in f.read().splitlines():
		line = line.split(' ')
		if line[0] == 'addx':
			i += 1
			print_operations(X, i)
			result.append(test(X, i))
			i += 1
			print_operations(X, i)
			result.append(test(X, i))
			X += int(line[1])
		else:
			i += 1
			print_operations(X, i)
			result.append(test(X, i))

print()
print(f'Answer 1: {sum(result)}')
