import os
import sys

f = open("input.txt", "r")
lines = f.readlines()

isFirst = True
cValue = 0
counter = 0

for line in lines:
    line = line.strip()
    if isFirst:
        isFirst = False
    else:
        if cValue < int(line) :
            counter +=1
    cValue = int(line)

print("Total increment = ", counter)    
f.close()