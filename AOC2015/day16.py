import re


def solve16():
    sues = open('inputs/day16.txt').read().split('\n')
    return find_sue(sues, compare_1), find_sue(sues, compare_2)


def find_sue(sue_list, compare):
    conditions = {'children': 3,
                  'cats': 7,
                  'samoyeds': 2,
                  'pomeranians': 3,
                  'akitas': 0,
                  'vizslas': 0,
                  'goldfish': 5,
                  'trees': 3,
                  'cars': 2,
                  'perfumes': 1}
    for sue in sue_list:
        possible = True
        for condition in re.findall('([a-z]+): ([0-9]+)', sue):
            if not compare(condition[0], conditions[condition[0]], int(condition[1])):
                possible = False
        if possible:
            return sue.split(':')[0][4:]
    return '', ''


def compare_1(condition, should, value):
    return should == value


def compare_2(condition, should, value):
    if condition in ['cats', 'trees']:
        return should < value
    elif condition in ['pomeranians', 'goldfish']:
        return should > value
    else:
        return should == value
