import time

def day7():
    positions = []
    with open("input.txt", "r") as f:
        positions = [int(e) for e in f.readline().split(',')]

    distance = [0 for e in positions]
    distance2 = distance.copy()
    for i in range(0, len(positions)):
        for x in range(0, len(positions)):
            counter = abs(positions[x]-positions[i])
            distance[i] += counter
            distance2[i] += int(counter*(counter+1)/2)

    print("#Day7 - Part1:", min(distance))
    print('#Day7 - Part2:', min(distance2))   

times = []
for i in range(0, 10):
    start = time.time()
    day7()
    stop = time.time() - start
    times.append(stop)
    print("Time of execution[{}]: {}".format(i, stop))

print("Average time of execution:", sum(times)/len(times))