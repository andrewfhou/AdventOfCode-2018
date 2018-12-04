import time


def curr_ms(): return time.time() * 1000


with open("input.txt") as file:
    inputs = file.read().splitlines()


def partOne():
    start = curr_ms()

    i = 0
    for x in inputs:
        inputs[i] = x.split(" ")
        i += 1
    
    inputs.sort(key = lambda x:((x[1])[0:2] + (x[1])[3:5]))
    inputs.sort(key = lambda x:x[0])

    for x in inputs:
        print(x)

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


def partTwo():
    start = curr_ms()

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


partOne()
# partTwo()
