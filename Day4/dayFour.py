from collections import defaultdict, Counter


with open("input.txt") as file:
    inputs = file.read().splitlines()

i = 0
for x in inputs:
    inputs[i] = x.split(' ')
    inputs[i][0] = (inputs[i][0])[1:]
    inputs[i][1] = (inputs[i][1])[:-1]
    inputs[i][1] = (inputs[i][1])[3:]
    i += 1

inputs.sort(key=lambda x: ((x[1])[0:2] + (x[1])[3:5]))
inputs.sort(key=lambda x: x[0])

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
    target = None
    for key, val in guards.items():
        if target is None or val > guards[target]:
            target = key
    
    targetGuard, targetMin = target
    print(targetGuard, "*", targetMin, "=",(targetGuard * targetMin))

def partTwo():
    return


partOne()
# partTwo()
