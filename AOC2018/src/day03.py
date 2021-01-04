import os.path
import re


f = open(os.path.dirname(__file__) + '/../inputs/input03.txt')
s = f.read().split('\n')
Map = dict()
currentSum1 = 0
for x in s:
    numbers = re.match('#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', x)
    startA = int(numbers.group(1))
    startB = int(numbers.group(2))
    for a in range(0, int(numbers.group(3))):
        for b in range(0, int(numbers.group(4))):
            val = Map.get(" ".join([str(startA+a), str(startB+b)]), 0)
            Map[" ".join([str(startA+a), str(startB+b)])] = val+1
total = 0
for line in Map:
    total += Map[line] > 1
print('Task 1: ', total)

for x in s:
    numbers = re.match('#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', x)
    startA = int(numbers.group(1))
    startB = int(numbers.group(2))
    noOverlap = True
    for a in range(0, int(numbers.group(3))):
        for b in range(0, int(numbers.group(4))):
            noOverlap = Map.get(" ".join([str(startA+a), str(startB+b)]), 0) == 1 and noOverlap

    if noOverlap:
        print('Task 2: ', re.match('#([0-9]+) @.*', x).group(1))

