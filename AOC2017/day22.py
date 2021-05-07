def solve22():
    dir0 = dir1 = (-1, 0)
    map0 = dict()
    map1 = dict()
    file = open('inputs/day22.txt').read().split('\n')
    for i in range(len(file)):
        for j in range(len(file[i])):
            map0[(i, j)] = file[i][j]
            map1[(i, j)] = file[i][j]
    pos0 = pos1 = (len(file)//2, len(file[0])//2)
    infected0 = infected1 = 0
    for i in range(10000):
        infected0, map0, pos0, dir0 = burst(infected0, map0, pos0, dir0)
    print('Task 1:', infected0)
    for i in range(10000000):
        infected1, map1, pos1, dir1 = burst_alt(infected1, map1, pos1, dir1)
    print('Task2:', infected1)


def burst(infected, map, pos, dir):
    if map.get(pos, '.') == '#':
        dir = turn(dir, True)
        map[pos] = '.'
    else:
        dir = turn(dir, False)
        map[pos] = '#'
        infected += 1
    pos = move(pos, dir)
    return infected, map, pos, dir


def burst_alt(infected, map, pos, dir):
    node = map.get(pos, '.')
    if node == '#':
        dir = turn(dir, True)
        map[pos] = 'F'
    elif node == 'W':
        map[pos] = '#'
        infected += 1
    elif node == 'F':
        dir = turn(turn(dir, True), True)
        map[pos] = '.'
    else:   # clean
        dir = turn(dir, False)
        map[pos] = 'W'
    pos = move(pos, dir)
    return infected, map, pos, dir


def move(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


def turn(dir, bool):
    return (dir[1], -dir[0]) if bool else (-dir[1], dir[0])
