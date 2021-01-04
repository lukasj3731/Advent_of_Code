import os.path
from string import ascii_lowercase

f = open(os.path.dirname(__file__) + '/../inputs/input02.txt')
s = f.read().split('\n')
c2 = c3 = 0
for x in s:
    twos = threes = False
    for c in ascii_lowercase:
        twos = twos or x.count(c) == 2
        threes = threes or x.count(c) == 3
    c2 += twos
    c3 += threes
print("Task 1: ", c2*c3)

ret = ""
for x in s:
    for y in s:
        diff = ""
        for i in range(0, len(y)):
            diff += x[i] if x[i] == y[i] else ""
        if len(diff)+1 == len(y):
            print("Task 2: ", diff)
            exit(0)
