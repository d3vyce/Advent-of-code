# Advent of Code 2022, Day 1, d3vyce

with open('input/day1.txt') as f:
    file = [i for i in f.read().splitlines()]

count = 0
tab = []

for line in file:
    if line == '':
        tab.append(count)
        count = 0
    else:
        count += int(line)

print(f'Answer 1: {max(tab)}')

tab.sort(reverse=True)

print(f'Answer 2: {sum(tab[0:3])}')