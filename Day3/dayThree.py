import time

curr_ms = lambda: time.time() * 1000

file = open('input.txt', 'r')
inputs = file.read().strip().split()
file.close()

def partOne() :
    start = curr_ms()

    print("Time Taken: " + str(curr_ms() - start) + "ms\n")

def partTwo() :
    start = curr_ms()
    
    print("Time Taken: " + str(curr_ms() - start) + "ms\n")

partOne()
partTwo()