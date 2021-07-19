import re


def solve19():
    file = open('inputs/day19.txt').read().split('\n\n')
    rules_text = file[0].split('\n')
    rules = dict()
    rules_b = dict()
    for line in rules_text:
        parts = line.split(' => ')
        arr = rules.get(parts[0], [])
        arr.append(parts[1])
        rules[parts[0]] = arr
        rules_b[parts[1]] = parts[0]
    molecule = file[1]
    operations = 0
    while molecule != 'e':
        for value_from in rules_b.keys():
            if value_from in molecule:
                molecule = replacenth(molecule ,value_from, rules_b[value_from], 0)
                operations += 1
    return len(iterate(file[1], rules)), operations


def iterate(molecule, rules):
    possible = set()
    for value_from in rules.keys():
        for i in range(molecule.count(value_from)):
            for value_to in rules[value_from]:
                str = replacenth(molecule, value_from, value_to, i)
                possible.add(str)
    return possible


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    return before + after
