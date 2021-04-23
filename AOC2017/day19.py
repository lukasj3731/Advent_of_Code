def t_add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def turn(t):
    return [(1, 0), (-1, 0)] if t[0] == 0 else [(0, 1), (0, -1)]


def solve19():
    map_file = open('inputs/day19.txt').read().split('\n')
    map = dict()
    for i in range(len(map_file)):
        for j in range(len(map_file[i])):
            if map_file[i][j] != ' ':
                map[(i, j)] = map_file[i][j]
    pos = list(map.keys())[0]
    dir = (1, 0)
    word = ''
    steps = 0
    while pos in map.keys():
        steps += 1
        if 'A' <= map.get(pos, ' ') <= 'Z':
            word += map[pos]
        elif map[pos] == '+':
            for dir_candidate in turn(dir):
                if t_add(pos, dir_candidate) in map.keys() and map[t_add(pos, dir_candidate)] != map[pos]:
                    dir = dir_candidate
        pos = t_add(pos, dir)
    print('Task 1:', word)
    print('Task 2:', steps)
