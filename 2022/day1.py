# Advent of Code 2022, Day 1, d3vyce

count = 0
tab = []

with open('input/day1.txt') as f:
    for line in f.read().splitlines():
        if line == '':
            tab.append(count)
            count = 0
        else:
            count += int(line)

print(f'Answer 1: {max(tab)}')

tab.sort(reverse=True)

print(f'Answer 2: {sum(tab[0:3])}')