def solve03():
    path = open('inputs/day03.txt').read()
    houses = set()
    houses_next_year = set()
    walk_way(path, houses)
    walk_way(path[1::2], houses_next_year)
    walk_way(path[::2], houses_next_year)
    return len(houses), len(houses_next_year)


def walk_way(path, houses):
    x = y = 0
    for char in path:
        if (x, y) not in houses:
            houses.add((x, y))
        if char == '<':
            x -= 1
        elif char == '>':
            x += 1
        elif char == 'v':
            y -= 1
        else:
            y += 1
