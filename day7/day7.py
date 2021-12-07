import time

start = time.time()
positions = []
with open("input.txt", "r") as f:
    positions = [int(e) for e in f.readline().split(',')]

distance = [0 for e in positions]
distance2 = distance.copy()
for i in range(0, len(positions)):

    for e in positions:
        counter = abs(e-positions[i])
        distance[i] += counter
        for j in range(1, counter+1):
            distance2[i] += j

print("#Day7 - Part1:", min(distance))
print('#Day7 - Part2:', min(distance2))

print("Time of execution: ", time.time()-start)