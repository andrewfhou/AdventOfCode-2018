import time
from collections import defaultdict


def curr_ms(): return time.time() * 1000


with open("input.txt") as file:
    inputs = file.read().splitlines()

i = 0
for x in inputs:
    inputs[i] = x.split(' ')
    inputs[i][0] = (inputs[i][0])[1:]
    inputs[i][1] = (inputs[i][1])[:-1]
    i += 1

inputs.sort(key=lambda x: ((x[1])[0:2] + (x[1])[3:5]))
inputs.sort(key=lambda x: x[0])

i = 0
for x in inputs:
    inputs[i][1] = (inputs[i][1])[3:]
    i += 1

guards = defaultdict(int)
timeslots = defaultdict(int)

for x in inputs:
    currTime = int(x[1])
    if x[2] == 'Guard':
        guardID = int(x[3][1:])
    elif x[2] == 'falls':
        asleep = currTime
    elif x[2] == 'wakes':
        for tt in range(asleep, currTime):
            guards[(guardID, tt)] += 1
            timeslots[guardID] += 1


def partOne():
    start = curr_ms()

    targetGuard = max(timeslots, key=timeslots.get)

    targetMin = None
    greatest = 0
    for k, v in guards.items():
        if k[0] == targetGuard:
            if targetMin is None or v > greatest:
                targetMin = k[1]
                greatest = v

    print("Part One:", targetGuard, "*", targetMin, "=", (targetGuard * targetMin))
    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


def partTwo():
    start = curr_ms()

    target = None
    for key, val in guards.items():
        if target is None or val > guards[target]:
            target = key

    print("Part Two:", target[0], '*', target[1], '=', (target[0] * target[1]))
    print("Time Taken: " + str(curr_ms() - start) + "ms")

partOne()
partTwo()
