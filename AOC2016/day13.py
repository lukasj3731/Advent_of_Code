def get_wall(pos, fave):
    x, y = pos
    return "{0:b}".format(x * x + 3 * x + 2 * x * y + y + y * y + fave).count('1') % 2 != 0


def iterate(condition, result, fave):
    pos = (1, 1)
    dist = 1
    map = dict()
    curr = [pos]
    while condition(map, dist):
        nxt = []
        for pos in curr:
            for adjacient in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]:
                if adjacient[0] >= 0 and adjacient[1] >= 0 and not get_wall(adjacient, fave) and adjacient not in nxt:
                    map[adjacient] = dist
                    nxt.append(adjacient)
        curr = nxt
        dist += 1
    return result(map)


def solve13():
    fave = int(open('inputs/day13.txt').read())
    print('Task 1:', iterate(lambda m, dist: not (31, 39) in m.keys(), lambda m: m[(31, 39)], fave))
    print('Task 2:', iterate(lambda m, dist: dist <= 50, lambda m: len(m), fave))
