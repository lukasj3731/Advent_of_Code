from copy import deepcopy
import itertools


def solve24():
    points = dict()
    labyrinth = dict()
    file = open('inputs/day24.txt').read().split('\n')
    connections = dict()
    for i in range(len(file)):
        for j in range(len(file[i])):
            labyrinth[(i, j)] = '#' if file[i][j] == '#' else '.'
            if '0' <= file[i][j] <= '9':
                points[file[i][j]] = (i, j)
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                dist = explore(labyrinth, points[p2], points[p1])
                connections[(p1, p2)] = dist
                connections[(p2, p1)] = dist
    paths = [(0, '0')]
    while len(paths[0][1]) < len(points):
        paths.sort()
        shortest = paths.pop(0)
        for connection in connections:
            if connection[0] == shortest[1][-1] and not shortest[1].__contains__(connection[1]):
                paths.append((shortest[0]+connections[connection], shortest[1]+connection[1]))
    paths.sort()
    print('Task 1:', paths[0][0])
    min_len = 99999
    for trip in list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7'])):
        trip_len = 0
        for i in range(8):
            trip_len += connections[(trip[i-1], trip[i])]
        min_len = min(min_len, trip_len)
    print('Task 2:', min_len)


def adj(p):     # given a point p returns adjacent points in an array
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]


def explore(labyrinth, end, start):  # explores labyrinth, marking visited spaces with their distance from S and
    if end == start:
        return []
    dist = 1                    # marking the final path with '.'
    curr_list = [start]
    labyrinth = deepcopy(labyrinth)
    goal = None
    while len(curr_list) > 0 and goal is None:
        nxt = []
        for point in list(set().union(*[adj(p) for p in curr_list])):
            if point == end:  # return if goal
                goal = point
            if labyrinth.get(point, 'E') != '#':  # move there next if free
                nxt.append(point)
                labyrinth[point] = dist
        curr_list = nxt
        dist += 1
    return dist - 1
