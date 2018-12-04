from collections import defaultdict


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

targetGuard = max(timeslots, key=timeslots.get)

targetMin = None
greatest = 0
for k,v in guards.items():
    if k[0] == targetGuard:
        if targetMin is None or v > greatest:
            targetMin = k[1]
            greatest = v

print(targetGuard, "*", targetMin, "=",(targetGuard * targetMin))

# note: minute 40 should (maybe?) have 14 sleeps, only has 13 now. According to
# Amy's output anyways

target = None
for key, val in guards.items():
    if target is None or val > guards[target]:
        target = key

print(target[0], '*', target[1], '=', (target[0] * target[1]))