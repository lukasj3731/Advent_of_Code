import os.path

f = open(os.path.dirname(__file__) + '/../inputs/input01.txt')
s = f.read().split('\n')
currentSum1 = 0
for x in s:
    currentSum1 += int(x)
print("Task 1: ", currentSum1)

currentSum = 0
seenNumbers = set()
i = 0
while currentSum not in seenNumbers:
    seenNumbers.add(currentSum)
    currentSum += int(s[i])
    i += 1
    i = i % (len(s))
print("Task 2: ", currentSum)
