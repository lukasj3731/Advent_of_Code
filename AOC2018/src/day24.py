import os
import re
from copy import deepcopy


def togroup(line, team, boost):
    numbers = re.findall('[0-9]+', line)
    numUnits = numbers[0]
    hp = numbers[1]
    dmg = numbers[2]
    initiative = numbers[3]
    dmgtype = (re.findall('([a-z]+) damage', line))[0]
    immune = (re.findall('immune to ([a-z, ]+)', line)+[''])[0]
    weak = (re.findall('weak to ([a-z, ]+)', line)+[''])[0]
    return int(initiative), int(numUnits), int(hp), int(dmg)+boost, dmgtype, weak, immune, team


def effectivepower(unit):
    initiative, numunits, hp, dmg, dmgtype, weak, immune, team = unit
    return numunits * dmg


def initiative(unit):
    return unit[0]


def dealtdamage(attacker, defender):
    initiative, numunits, hp, dmg, dmgtype, weak, immune, team = attacker
    dinitiative, dnumunits, dhp, ddmg, ddmgtype, dweak, dimmune, dteam = defender
    dealt = dmg*numunits
    if dweak.__contains__(dmgtype):
        dealt *= 2
    elif dimmune.__contains__(dmgtype):
        dealt = 0
    return dealt


def dealdamage(attacker, defender):
    dealt = dealtdamage(attacker, defender)
    initiative, numunits, hp, dmg, dmgtype, weak, immune, team = defender
    numunits -= dealt//hp
    # print('dmg dealt: '+str(dealt//hp)+' ( '+str(dealt)+' // '+str(hp)+' )')
    return initiative, numunits, hp, dmg, dmgtype, weak, immune, team


def findtarget(unit, possible):
    try:
        return max((x for x in possible if x[7] != unit[7] and dealtdamage(unit, x) != 0),
                   key=lambda x: (dealtdamage(unit, x), effectivepower(x), x[0]))
    except ValueError as e:
        return None


def isalive(unit):
    return unit[1] > 0


def p(unit):
    return '['+str(unit[7]) +', init: '+str(unit[0])+' with '+str(unit[1])+' at '+str(unit[2])+']'


def fight(f, boost):
    immune = f[0].split('\n')
    infection = f[1].split('\n')
    immune.pop(0)
    infection.pop(0)

    units = []
    for i in immune:
        units.append(togroup(i, 'IM', boost))
    for i in infection:
        units.append(togroup(i, 'IF', 0))

    attackpattern = {'just': 'not empty'}
    seen = set()
    while len(attackpattern) > 0:
        # print('round ', i)
        units.sort(key=effectivepower)
        units.reverse()
        ID = str(units)
        possible = deepcopy(units)
        attackpattern = dict()
        for attacker in units:
            target = findtarget(attacker, possible)
            if target is not None:
                attackpattern[attacker[0]] = target[0]
                possible.remove(target)
        # print(attackpattern)
        units.sort(key=initiative)
        units.reverse()
        # print('------------')
        for unit in units:
            # print('['+str(boost)+']'+p(unit))
            if isalive(unit):
                targetinitiative = attackpattern.get(unit[0], None)
                if targetinitiative is not None:
                    target = None
                    for potentialtarget in units:
                        if potentialtarget[0] == targetinitiative:
                            target = potentialtarget
                    units[units.index(target)] = dealdamage(unit, target)
                    # print(p(unit)+' attacked '+p(target))
        # print('------------')
        for unit in units:
            if not isalive(unit):
                units.remove(unit)
    sum = 0
    for unit in units:
        sum += unit[1]

    return units[0][7], sum


f = open(os.path.dirname(__file__) + '/../inputs/input24.txt').read().split('\n\n')
print('task 1:', fight(f, 0)[1])

boost = 0
while fight(f, boost)[0] != 'IM':
    boost += 1
print('task 2:', fight(f, boost)[1])
