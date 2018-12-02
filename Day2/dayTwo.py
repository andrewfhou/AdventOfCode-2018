import time

curr_ms = lambda: time.time() * 1000

file = open('input.txt', 'r')
inputs = file.read().strip().split()
file.close()

def partOne() :
    start = curr_ms()
    twoCount = 0
    threeCount = 0

    for x in inputs :
        i = 0
        twoFound = False
        threeFound = False

        while i < len(x) :
            if x.count(x[i]) == 2 and not twoFound :
                twoCount += 1
                twoFound = True
            if x.count(x[i]) == 3 and not threeFound :
                threeCount += 1
                threeFound = True
            i = i + 1

    print("Part One: " + str(twoCount) + " * " + str(threeCount) + " = " + str(twoCount * threeCount))
    print("Time Taken: " + str(curr_ms() - start) + "ms\n")

def partTwo() :
    start = curr_ms()
    for x in inputs :
        for y in inputs :
            diffCount = 0
            diffIndex = 0
            for i in range(len(x)) :
                if x[i] != y[i] :
                    diffCount += 1
                    diffIndex = i
                if diffCount > 1 :
                    break
                i += 1
            if diffCount == 1 :
                print("Part Two: " + x[0:diffIndex] + x[diffIndex + 1:])
                print("Time Taken: " + str(curr_ms() - start) + "ms\n")
                return

partOne()
partTwo()