import os.path


f = open(os.path.dirname(__file__) + '/../inputs/input22.txt').read().split('\n')
depth = int(f[0].split(' ')[1])
target = f[1].split(' ')[1].split(',')
tx = int(target[0])
ty = int(target[1])
#depth = 510
#tx = 10
#ty = 10

def geoindex(x, y, cave):
    if x == tx and y == ty:
        return 0
    if y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return cave[(x-1,y)] * cave[(x, y-1)]


cave = dict()
cave[(0, 0)] = 0

for y in range(max(tx, ty) + 1000):
    for x in range(max(tx, ty) + 1000):
        cave[(x, y)] = ((geoindex(x, y, cave) + depth) % 20183)

sum = 0
for y in range(ty+1):
    for x in range(tx+1):
        sum += cave[(x, y)] % 3
print('task 1:', sum)


def possible(x, y):
    return ['ct', 'cn', 'tn'][cave[(x, y)] % 3]


queue = [(0, 't', 0, 0)]
mindist = dict()
directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

import heapq

while True:
    #curr = queue.pop(0)
    curr = heapq.heappop(queue)
    #print(curr)
    dist, tool, x, y = curr
    mindistkey = (tool, x, y)
    if x == tx and y == ty and tool == 't':
        print('task2:', dist)
        break
    if mindistkey in mindist and mindist[mindistkey] <= dist:
        continue
    mindist[mindistkey] = dist

    for t in list('tnc'):
        if t != tool and t in possible(x, y):
            heapq.heappush(queue, (dist + 7, t, x, y))

    for i in range(0, 4):
        dx, dy = directions[i]
        newx = x + dx
        newy = y + dy
        if newx < 0 or newy < 0 or tool not in possible(newx, newy):
            continue
        heapq.heappush(queue, (dist+1, tool, newx, newy))
