import time


def curr_ms(): return time.time() * 1000


with open("input.txt") as file:
    inputs = file.read().splitlines()


def partOne():
    start = curr_ms()

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


def partTwo():
    start = curr_ms()

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")


partOne()
# partTwo()
