import time

curr_ms = lambda: time.time() * 1000

file = open('input.txt', 'r')
inputs = file.read().strip().split()
file.close()

def partOne() :
    start = curr_ms()
    freq = 0

    for i in inputs: 
        if i[0] == '+' : 
                freq = freq + int(i[1:])
        elif i[0] == '-' :
            freq = freq - int(i[1:])
    
    print("Part One: " + str(freq))
    print("Time Taken: " + str(curr_ms() - start) + "ms\n")

def partTwo() :
    start = curr_ms()
    freq = 0
    seen = set([freq])
    done = False

    while not done :
        for i in inputs :
            freq = freq + int(i[:])
        
            if freq in seen :
                print("Part Two: " + str(freq))
                print("Time Taken: " + str(curr_ms() - start) + "ms\n")
                done = True
                return
            seen.add(freq)

partOne()
partTwo()