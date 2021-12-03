import sys, os

f = open("input.txt", "r")
lines = f.readlines()

window_size = 3
windowsSum = list()
values = list()

index = 0

for line in lines :
    values.append(int(line))

for value in values:
    if(index+2 < len(values)):
        sum = value
        sum += values[index+1]
        sum += values[index+2]
        print(index, ": ", sum)
        windowsSum.append(sum)
    index += 1

isFirst = True
cValue = 0
counter = 0

for value in windowsSum :
    if isFirst:
        isFirst = False
    else:
        if cValue < value :
            counter += 1
    cValue = value

print("Total increment = ", counter) 
f.close()


