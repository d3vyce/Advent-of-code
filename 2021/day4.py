# Advent of Code 2021, Day 4, d3vyce

def create_matrix(raw):
	lines = raw.strip().splitlines()
	return list(list(map(int, l.split())) for l in lines)

def win_check(matrix):
    for row in matrix:
        if sum(y == 0 for y in row) == 5: return True

    for i in range(len(matrix[0])):
        if sum(row[i] == 0 for row in matrix) == 5: return True
    return False

def nb_write(matrix, nb):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if(val == nb): 
                matrix[i][j] = 0
                if win_check(matrix): return True
    
    return False

def score_calcule(matrix, nb):
    score = 0
    for row in matrix:
        for val in row:
            score += val
    score *= nb
    
    return score
            
# Part 1&2
with open('input/day4.txt') as f:
    number = map(int, f.readline().split(','))
    l_matrix = list(map(create_matrix, f.read().split('\n\n')))

NB_WIN = 0

for nb in number:
    for i, matrix in enumerate(l_matrix):
        if(matrix == None): continue
        
        RESULT = nb_write(matrix, nb)
        if RESULT:
            NB_WIN += 1
            if(NB_WIN == 1): score_1 = score_calcule(matrix, nb)
            elif(NB_WIN == len(l_matrix)): score_last = score_calcule(matrix, nb)
            l_matrix[i] = None

print("Part 1 : ",score_1)
print("Part 2 : ",score_last)
