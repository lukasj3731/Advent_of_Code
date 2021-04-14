def solve11():
    pos = (0, 0)
    max_dist = 0
    for step in open('inputs/day11.txt').read().split(','):
        pos = step_dir(pos, step)
        max_dist = max(dist(pos), max_dist)
    print('Task 1:', dist(pos))
    print('Task 2:', max_dist)


def step_dir(pos, step):
    x, y = pos
    x += (step in ['n', 'ne']) - (step in ['s', 'sw'])
    y += (step in ['ne', 'se']) - (step in ['nw', 'sw'])
    return x, y


def dist(point):
    x, y = point
    return abs(x)+abs(y) if x*y < 0 else max(abs(x), abs(y))
