def solve18():
    file = [[x for x in line] for line in open('inputs/day18.txt').read().split('\n')]
    map1 = dict()
    map2 = dict()
    for i in range(len(file)):
        for j in range(len(file[i])):
            map1[i, j] = file[i][j]
            map2[i, j] = file[i][j]
    turn_on_corners(map2)
    for i in range(100):
        map1 = iterate(map1, False)
        map2 = iterate(map2, True)
    return sum(1 if val == '#' else 0 for val in map1.values()), sum(1 if val == '#' else 0 for val in map2.values())


def iterate(map, edges):
    new_map = dict()
    for entry in map.keys():
        neighbors = count_adj(entry, map)
        new_map[entry] = '#' if map[entry] == '.' and neighbors == 3 or \
                                map[entry] == '#' and 2 <= neighbors <= 3 else '.'
    if edges:
        turn_on_corners(new_map)
    return new_map


def turn_on_corners(map):
    w = int(pow(len(map), 0.5))-1
    map[0, 0] = '#'
    map[0, w] = '#'
    map[w, 0] = '#'
    map[w, w] = '#'


def adj(t):
    x, y = t
    return [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)]


def count_adj(location, map):
    return sum(0 if map.get(item, '.') == '.' else 1 for item in adj(location))
