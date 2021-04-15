def solve12():
    connections = dict()
    for connection in open('inputs/day12.txt').read().split('\n'):
        components = connection.split(' <-> ')
        connections[components[0]] = components[1].split(', ')
    groups = []
    while len(connections) > 0:
        curr_grp = connect_group(connections)
        groups.append(curr_grp)
    print('Task 1:', len(groups[0]))
    print('Task 2:', len(groups))


def connect_group(connections):
    total = []
    curr = [list(connections.keys())[0]]
    while len(curr) > 0:
        nxt = []
        for item in curr:
            for candidate in connections[item]:
                if candidate not in total:
                    total.append(candidate)
                    nxt.append(candidate)
        curr = nxt
    for elem in total:
        connections.pop(elem)
    return total
