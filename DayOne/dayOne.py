import time

file = open('input.txt', 'r')
inputs = file.read().strip().split()
file.close()

def sum() :
    start = time.time()
    freq = 0

    for i in inputs: 
        if i[0] == '+' : 
                freq = freq + int(i[1:])
        elif i[0] == '-' :
            freq = freq - int(i[1:])
    
    print("Part One: " + str(freq))
    print("time taken: " + str(time.time() - start))

def solve() :
    start = time.time()
    freq = 0
    seen = set([freq])
    done = False
    iteration = 0

    while not done :
        for i in inputs :
            iterTime = time.time()
            if i[0] == '+' : 
                freq = freq + int(i[1:])
            elif i[0] == '-' :
                freq = freq - int(i[1:])
        
            if freq in seen :
                print("Part Two: " + str(freq) + "\ntime taken: " + str(time.time() - start))
                done = True
                return
            seen.add(freq)

        elapsed = time.time() - iterTime
        print("iteration " + str(iteration) + "\t|freq: " + str(freq) + "\t|time: " + str(elapsed))
        iteration = iteration + 1

solve()
sum()
