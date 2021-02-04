import os.path
import re


def source(x, y, maxy, ground):
    while not '#~'.__contains__(ground.get(str(x)+','+str(y+1), '.')):
        ground[str(x)+','+str(y+1)] = '|'
        y += 1
        if y > maxy:
            return
    edgeFound = False
    while not edgeFound:
        left = right = 0
        while '~#'.__contains__(ground.get(str(x-left)+','+str(y+1), '.')) \
                and '.|'.__contains__(ground.get(str(x-left-1)+','+str(y), '.')):       #move left till edge or wall
            left += 1
        while '~#'.__contains__(ground.get(str(x+right)+','+str(y+1), '.')) \
                and '.|'.__contains__(ground.get(str(x+right+1)+','+str(y), '.')):      #move right till edge or wall
            right += 1
        if ground.get(str(x-left)+','+str(y+1), '.') == '.':    #if edge left, new source left
            source(x - left, y, maxy, ground)
        if ground.get(str(x+right)+','+str(y+1), '.') == '.':   #if edge right, new source right
            source(x + right, y, maxy, ground)
        overflow = 0
        overflow += '.|'.__contains__(ground.get(str(x-left)+','+str(y+1), '.'))            #still overflowing on left side?
        overflow += '.|'.__contains__(ground.get(str(x + right) + ',' + str(y + 1), '.'))   #still overflowing on right side?
        edgeFound = overflow > 0    #if overflowing, end loop
        for i in range(x-left, x+right+1):
            ground[str(i)+','+str(y)] = '|' if edgeFound else '~'   #also fill layer with '|'. if not overflowing, fill with '~'
        y -= 1


f = open(os.path.dirname(__file__) + '/../inputs/input17.txt').read().split('\n')
minx = miny = 99999
maxx = maxy = 0
ground = dict()

for line in f:
    numbers = [int(x) for x in re.findall('[0-9]+', line)]
    if line[0] == 'x':
        for i in range(numbers[1], numbers[2]+1):
            ground[str(numbers[0]) + ',' + str(i)] = '#'
        minx = min(minx, numbers[0])
        maxx = max(maxx, numbers[0])
        miny = min(miny, numbers[1])
        maxy = max(maxy, numbers[2])
    else:
        for i in range(numbers[1], numbers[2]+1):
            ground[str(i) + ',' + str(numbers[0])] = '#'
        minx = min(minx, numbers[1])
        maxx = max(maxx, numbers[2])
        miny = min(miny, numbers[0])
        maxy = max(maxy, numbers[0])

source(500, 0, maxy, ground)
t1 = 0
t2 = 0

for point in ground:
    coords = point.split(',')
    x = int(coords[0])
    y = int(coords[1])
    if minx-1 <= x <= maxx+1 and miny <= y <= maxy:
        t1 += '|~'.__contains__(ground[point])
        t2 += ground[point] == '~'
print('task 1:',t1, '\ntask 2:', t2)

