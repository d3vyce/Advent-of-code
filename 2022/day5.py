# Advent of Code 2022, Day 5, d3vyce

next = False
Crate = [[] for i in range(3)]
result = ''

with open('input/day5.txt') as f:
	file = f.read()
	
for line in file.splitlines():
	if line == '':
		for i in range(len(Crate)):
			Crate[i].reverse()
		next = True
		continue
	if not next:
		if '1' in line:
			continue
		offset = 1
		for i in range(len(line)):
			if line[offset] != ' ':
				Crate[i].append(line[offset])
			if offset+4 > len(line)-1:
				break
			offset += 4
	else:
		line = line.split(' ')
		for _ in range(int(line[1])):
			Crate[int(line[5])-1].append(Crate[int(line[3])-1].pop())

for i in range(len(Crate)):
	result += Crate[i][-1]

print(f'Answer 1: {result}')

next = False
Crate = [[] for i in range(3)]
result2 = ''

for line in file.splitlines():
	if line == '':
		for i in range(len(Crate)):
			Crate[i].reverse()
		next = True
		continue
	if not next:
		if '1' in line:
			continue
		offset = 1
		for i in range(len(line)):
			if line[offset] != ' ':
				Crate[i].append(line[offset])
			if offset+4 > len(line)-1:
				break
			offset += 4
	else:
		line = line.split(' ')
		move = int(line[1])
		while move != 0:
			if move >= 3:
				for y in range(3, 0, -1):
					Crate[int(line[5])-1].append(Crate[int(line[3])-1].pop(Crate[int(line[3])-1].index(Crate[int(line[3])-1][-y])))
				move -= 3
			elif move == 2:
				for y in range(2, 0, -1):
					Crate[int(line[5])-1].append(Crate[int(line[3])-1].pop(Crate[int(line[3])-1].index(Crate[int(line[3])-1][-y])))
				move -= 2
			else:
				Crate[int(line[5])-1].append(Crate[int(line[3])-1].pop())
				move -= 1

for i in range(len(Crate)):
	result2 += Crate[i][-1]

print(f'Answer 2: {result2}')

# CQQBBJFCS