import time
from collections import defaultdict


def curr_ms(): return time.time() * 1000


with open("input.txt") as file:
    inputs = file.read().replace(" ", "").splitlines()


def partOne():
    start = curr_ms()

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
    for l, t, w, h in data:
        for a in range(w):
            for b in range(h):
                overlaps[(a+l, b+t)] += 1

    dupes = 0
    for x in overlaps.values():
        if x > 1:
            dupes += 1

    print("Part One: " + str(dupes))

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


def partTwo():
    start = curr_ms()

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


partOne()
partTwo()
