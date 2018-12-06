from collections import defaultdict

with open("input.txt") as file:
    inputs = file.read().splitlines()

grid = defaultdict(int)

for a in inputs:
    grid[(a[:a.find(',')], a[a.find(',') + 2:])] = 'X'
