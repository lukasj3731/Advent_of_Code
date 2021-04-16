def solve13():
    gates = [(int(l.split(': ')[0]), int(l.split(': ')[1])) for l in open('inputs/day13.txt').read().split('\n')]
    print('Task 1:', sum([g[0] * g[1] for g in gates if not (g[1] - 1) - abs((g[0] % (2 * g[1] - 2)) - g[1] + 1)]))
    skip = 0
    while caught(skip, gates):
        skip += 1
    print('Task 2:', skip)


def caught(offset, gates):
    for g in gates:
        if not (g[1] - 1) - abs(((g[0] + offset) % (2 * g[1] - 2)) - g[1] + 1):
            return True
    return False
