import os.path
import re


f = open(os.path.dirname(__file__) + '/../inputs/input04.txt')
f = f.read().split('\n')
f.sort()
Map = dict()

guard = 0
asleep = -1
for line in f:
    if line.__contains__('#'):
        guard = int(re.match('.*#([0-9]+).*', line).group(1))
    else:
        if line.__contains__('falls') and asleep == -1:
            asleep = int(re.match('.*:([0-9]+).*', line).group(1))
        else:
            if guard not in Map:
                Map[guard] = dict()
            for i in range(asleep, int(re.match('.*:([0-9]+).*', line).group(1))):
                Map[guard][i] = Map[guard].get(i, 0) + 1
            asleep = -1


maximum = 0
result = 0
for guard in Map:
    slept = 0
    for i in range(0, 60):
        slept += Map[guard].get(i, 0)
    if slept > maximum:
        maximum = slept
        maxVal = -1
        maxPos = 0
        for i in range(0, len(Map[guard])):
            if Map[guard].get(i, 0) > maxVal:
                maxVal = Map[guard].get(i, 0)
                maxPos = i
        result = guard * maxPos
print('Task 1:', result)

maximum = 0
guardNum = 0
minuteNum = 0
for guard in Map:
    for i in range(0, 60):
        if Map[guard].get(i, 0) > maximum:
            maximum = Map[guard].get(i, 0)
            minuteNum = i
            guardNum = guard
print('Task 2:', minuteNum*guardNum)

