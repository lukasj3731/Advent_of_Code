import re
from copy import deepcopy


def solve22():
    nodes = []
    for line in open('inputs/day22.txt').read().split('\n')[2:]:
        nodes.append([int(x) for x in re.findall('[0-9]+', line)])
    valid_pairs = 0
    for i in range(len(nodes)):
        A = nodes[i]
        for B in nodes:
            if A[3] != 0 and A != B and A[3] <= B[4]:
                valid_pairs += 1
    print('Task 1:', valid_pairs)
    map = dict()
    max_x = max_y = -1
    for line in open('inputs/day22.txt').read().split('\n')[2:]:
        numbers = [int(x) for x in re.findall('[0-9]+', line)]
        max_x = max(max_x, numbers[0])
        max_y = max(max_y, numbers[1])
        char = '.'
        if numbers[3] == 0:
            char = '_'
        if numbers[3] > 200:
            char = '#'
        map[(numbers[0], numbers[1])] = char
    map[max_x, 0] = 'G'
    total = 0
    while explore(map, search(map, 'G'), (0, 0)):
        nxt = explore(map, search(map, 'G'), (0, 0))[1]
        path = explore(map, search(map, '_'), nxt)
        map[search(map, 'G')] = '_'
        map[path[0]] = '.'
        map[path[-1]] = 'G'
        total += len(path)
    print('Task 2:', total)


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
            if labyrinth.get(point, 'E') == '.':  # move there next if free
                nxt.append(point)
                labyrinth[point] = dist
        curr_list = nxt
        dist += 1
    path = [goal]
    while len(curr_list) > 0:
        if start in adj(goal):
            path.append(start)
            return path
        goal = min([point for point in adj(goal) if isinstance(labyrinth.get(point, 'E'), int)],
                   key=lambda point: labyrinth[point])
        labyrinth[goal] = '.'
        path.append(goal)
    return path


def search(labyrinth, char):
    for key in labyrinth.keys():
        if labyrinth[key] == char:
            return key
    return None
