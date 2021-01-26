import os.path


def sumpotts(potts):
    total = 0
    for pot in potts.keys():
        if potts[pot] == '#':
            total += pot
    return total


f = open(os.path.dirname(__file__) + '/../inputs/input12.txt').read().split("\n")
initialState = f[0].split(": ")[1]
potts = dict()
for i in range(0, len(initialState)):
    potts[i] = initialState[i]
rules = dict()
for i in range(2, len(f)):
    r = f[i].split(" => ")
    rules[r[0]] = r[1]

pottLines = dict()
for generation in range(0, 10000):
    newPotts = dict()
    pottLines[generation] = sumpotts(potts)

    for pot in range(min(potts.keys())-3, max(potts.keys())+3):
        line = ''
        for m in range(-2, 3):
            line += potts.get(pot+m, '.')
        if rules.get(line, '.') == '#':
            newPotts[pot] = '#'
    potts = newPotts

print('task 1:', pottLines[20])
print('task 2:', (50000000000-9999) * (pottLines[9999]-pottLines[9998])+pottLines[9999])

