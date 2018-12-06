from collections import defaultdict

with open("input.txt") as file:
    inputs = file.read().splitlines()

xPoints = defaultdict(int)
yPoints = defaultdict(int)

maxX = 0
maxY = 0
count = 0
for a in inputs:
    x = int(a[:a.find(',')])
    y = int(a[a.find(',') + 2:])
    xPoints[count] = x
    yPoints[count] = y
    count += 1
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y

grid = [[None for x in range(maxX + 1)] for y in range(maxY + y)]
areas = defaultdict(int)

for x in range(maxX):
    for y in range(maxY):
        shortest = maxX + maxY
        best = -1

        for i in range(count): # Given (x,y), find the distance to the closest point
            ptX = xPoints[i]
            ptY = yPoints[i]

            dist = abs(x - ptX) + abs(y - ptY)
            if dist < shortest:
                shortest = dist
                best = i
            elif dist == shortest:
                best = -1
        
        grid[x][y] = best
        total = areas[best]
        if total == 0:
            total = 1
        else:
            total += 1
        areas[best] = total

for x in range(maxX): # delete values with x out-of-bounds/inf area
    target = grid[x][0]
    areas.pop(target, None)
    target = grid[x][maxY]
    areas.pop(target, None)

for y in range(maxY): # delete values with y out-of-bounds/inf area
    target = grid[0][y]
    areas.pop(target, None)
    target = grid[maxX][y]
    areas.pop(target, None)

largest = 0
for a in areas:
    if a > largest:
        largest = a

print("Largest:", largest)