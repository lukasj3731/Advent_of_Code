import os.path
from copy import deepcopy


def iter(forrest):
    target = deepcopy(forrest)
    for x in range(len(forrest)):
        for y in range(len(forrest[0])):
            surroundings = ''
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx != 0 or dy != 0) and 0 <= x+dx < len(forrest) and 0 <= y+dy < len(forrest[0]):
                        surroundings += forrest[x+dx][y+dy]
            if forrest[x][y] == '.' and surroundings.count('|') >= 3:
                target[x][y] = '|'
            elif forrest[x][y] == '|' and surroundings.count('#') >= 3:
                target[x][y] = '#'
            elif forrest[x][y] == '#' and not (surroundings.__contains__('#') and surroundings.__contains__('|')):
                target[x][y] = '.'
    return target


def getResourceValue(forrest):
    lumber = tree = 0
    for a in range(len(forrest)):
        for b in range(len(forrest[a])):
            lumber += forrest[a][b] == '#'
            tree += forrest[a][b] == '|'
    return lumber * tree


f = open(os.path.dirname(__file__) + '/../inputs/input18.txt').read().split('\n')
forrest = []
for line in f:
    forrest.append([c for c in line])

for i in range(10):
    forrest = iter(forrest)
print('task 1:', getResourceValue(forrest))

seen = dict()
i = 10
while i < 1000000000:
    forrest = iter(forrest)
    curr = str(forrest)
    if seen.__contains__(curr):
        i += ((1000000000-i)//(i-seen[curr]))*(i-seen[curr])
    else:
        seen[curr] = i
    i += 1
print('task 2:', getResourceValue(forrest))

