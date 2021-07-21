def solve21():
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)]
    rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0)]
    loadouts = []
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r1 == r2 and r1[0] != 0:
                        continue
                    else:
                        loadouts.append((w[0]+a[0]+r1[0]+r2[0], w[1]+a[1]+r1[1]+r2[1], w[2]+a[2]+r1[2]+r2[2]))
    loadouts.sort()
    min_money = max_money = -1
    enemy = [int(x.split(' ')[-1]) for x in open('inputs/day21.txt').read().split('\n')]
    for loadout in loadouts:
        if fight((100, loadout[1], loadout[2]), enemy):
            if min_money == -1:
                min_money = loadout[0]
        else:
            max_money = loadout[0]
    return min_money, max_money


def fight(player, enemy):
    return player[0] // max(1, player[1]-enemy[2]) <= enemy[0] // max(1, enemy[1]-player[2])
