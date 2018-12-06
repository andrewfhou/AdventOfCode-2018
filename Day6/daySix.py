from collections import defaultdict

with open("input.txt") as file:
    inputs = file.read().splitlines()

points = defaultdict(int)

maxX = 0
maxY = 0
count = 0
for a in inputs:
    x = int(a[:a.find(',')])
    y = int(a[a.find(',') + 2:])
    points[count] = (x, y)
    count += 1
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y

grid = [[] * (maxX + 1)] * (maxY + 1)

