# Advent of Code 2022, Day 8, d3vyce

import numpy as np

matrix = np.genfromtxt('input/day8.txt', delimiter=1, dtype=int)
result = np.zeros(matrix.shape, dtype=int)
best_score = 0

print(matrix.shape)

for i in range(matrix.shape[0]):
	max = matrix[i][0]
	result[i][0] = 1
	result[i][-1] = 1
	for y in range(1, matrix.shape[0]-1):
		if matrix[i][y] > max: 
			result[i][y] = 1
			max = matrix[i][y]
	max = matrix[i][-1]
	for y in range(matrix.shape[0]-1, 0, -1):
		if matrix[i][y] > max: 
			result[i][y] = 1
			max = matrix[i][y]

for y in range(matrix.shape[0]):
	max = matrix[0][y]
	result[0][y] = 1
	result[-1][y] = 1
	for i in range(1, matrix.shape[0]-1):
		if matrix[i][y] > max: 
			result[i][y] = 1
			max = matrix[i][y]
	max = matrix[-1][y]
	for i in range(matrix.shape[0]-1, 0, -1):
		if matrix[i][y] > max: 
			result[i][y] = 1
			max = matrix[i][y]

for i in range(matrix.shape[0]):
	for y in range(matrix.shape[0]):
		score = 1
		if i == matrix.shape[0]-1: nb = 0
		else: nb = 1
		while i+nb < matrix.shape[0]-1 and matrix[i][y] > matrix[i+nb][y]:
			nb += 1
		score *= nb
		if i == 0: nb = 0
		else: nb = 1
		while i-nb > 0 and matrix[i][y] > matrix[i-nb][y]:
			nb += 1
		score *= nb
		if y == matrix.shape[0]-1: nb = 0
		else: nb = 1
		while y+nb < matrix.shape[0]-1 and matrix[i][y] > matrix[i][y+nb]:
			nb += 1
		score *= nb
		if y == 0: nb = 0
		else: nb = 1
		while y-nb > 0 and matrix[i][y] > matrix[i][y-nb]:
			nb += 1
		score *= nb

		if score > best_score:
			best_score = score

print(f'Answer 1: {result.sum()}')

print(f'Answer 2: {best_score}')
