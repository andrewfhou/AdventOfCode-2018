import time

curr_ms = lambda: time.time() * 1000

file = open('input.txt', 'r')
inputs = file.read().strip().split()
file.close()

def sum() :
    start = curr_ms()
    freq = 0

    for i in inputs: 
        if i[0] == '+' : 
                freq = freq + int(i[1:])
        elif i[0] == '-' :
            freq = freq - int(i[1:])
    
    print("Part One: " + str(freq))
    print("time taken: " + str(curr_ms() - start) + "ms")

def solve() :
    start = curr_ms()
    freq = 0
    seen = set([freq])
    done = False
    iteration = 0

    while not done :
        for i in inputs :
            iterTime = curr_ms()
            freq = freq + int(i[:])
        
            if freq in seen :
                print("\nPart Two: " + str(freq) + "\ntime taken: " + str(curr_ms() - start) + " ms\n")
                done = True
                return
            seen.add(freq)

        elapsed = curr_ms() - iterTime
        print("iteration " + str(iteration) + "\tfreq: " + str(freq) + "\ttime: " + str(elapsed) + "ms")
        iteration = iteration + 1

solve()
sum()
