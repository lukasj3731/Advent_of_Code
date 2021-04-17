from day10 import scramble_list, condense


def hash(input):
    inputs = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    list = [x for x in range(256)]
    scramble_list(list, inputs, 64)
    return condense(list)


def hex_to_bin(hex_input):
    for i in range(16):
        hex_input = hex_input.replace(hex(i)[2:], bin(i)[2:].zfill(4))
    return hex_input


def adj(p):
    return [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]


def solve14():
    input = open('inputs/day14.txt').read()
    memory = []
    for i in range(128):
        memory.append(hex_to_bin(hash(input+'-'+str(i))))
    print('Task 1:', sum([line.count('1') for line in memory]))
    used = set()
    for i in range(128):
        for j in range(128):
            if memory[i][j] == '1':
                used.add((i, j))
    groups = []
    while len(used) > 0:    # as long as we have ungrouped elements
        curr = [used.pop()]
        group = []
        while len(curr) > 0:    # as long as the group has still found new neighbours
            nxt = []
            for elem in curr:   # for every element in curr
                for item in adj(elem):  # for every neighbour in curr
                    if item in used and item not in group:  # if not seen yet
                        nxt.append(item)
                        used.remove(item)
                group.append(elem)
            curr = nxt
        groups.append(group)
    print('Task 2:', len(groups))
