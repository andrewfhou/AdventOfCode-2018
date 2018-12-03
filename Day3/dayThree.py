import time
from collections import defaultdict


def curr_ms(): return time.time() * 1000

def partOne():
    start = curr_ms()

    with open("input.txt") as file:
        inputs = file.read().splitlines()

    i = 0
    for x in inputs:
        inputs[i] = x[x.find('@') + 1:]
        i += 1

    data = []
    for x in inputs:
        xPos = int(x[:x.find(',')])
        yPos = int(x[x.find(',') + 1:x.find(':')])
        xDim = int(x[x.find(':') + 1:x.find('x')])
        yDim = int(x[x.find('x') + 1:])

        data.append([xPos, yPos, xDim, yDim])

    overlaps = defaultdict(int)
    for x, y, w, h in data:
        for a in range(w):
            for b in range(h):
                overlaps[(a+x, b+y)] += 1

    dupes = 0
    for x in overlaps.values():
        if x > 1:
            dupes += 1

    print("Part One: " + str(dupes))

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


def partTwo():
    start = curr_ms()

    with open("input.txt") as file:
        inputs = file.read().splitlines()

    data = []
    for x in inputs:
        num = int(x[x.find('#') + 1:x.find('@')])
        xPos = int(x[x.find('@') + 1:x.find(',')])
        yPos = int(x[x.find(',') + 1:x.find(':')])
        xDim = int(x[x.find(':') + 1:x.find('x')])
        yDim = int(x[x.find('x') + 1:])

        data.append([num, xPos, yPos, xDim, yDim])
    
    overlaps = defaultdict(int)
    for i, x, y, w, h in data:
        for a in range(w):
            for b in range(h):
                overlaps[(a+x, b+y)] += 1
    
    for i, x, y, w, h in data:
        unique = True
        for a in range(w):
            for b in range(h):
                if overlaps[(a+x, b+y)] > 1:
                    unique = False
        if(unique):
            print("Part Two: " + str(i))

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


partOne()
partTwo()
