import re


def total_weight(name, list):
    line = ''
    for item in list:
        if item.split(' -> ')[0].__contains__(name):
            line = item
    weight = int(re.findall('[0-9]+', line)[0])
    if line.__contains__(' -> '):
        children = line.split(' -> ')[1].split(', ')
        child_weights = [total_weight(child, list) for child in children]
        weights = dict()
        for w in child_weights:
            weights[w] = weights.get(w, 0) + 1
        if len(weights) > 1:
            wrong = right =-1
            for w in weights:
                if weights[w] == 1:
                    wrong = w
                else:
                    right = w
            print('Task 2:', actual_weight(children[child_weights.index(wrong)], list)+(right-wrong))
            child_weights[child_weights.index(wrong)] = right
        weight += sum(child_weights)
    return weight


def actual_weight(name, list):
    line = ''
    for item in list:
        if item.split(' -> ')[0].__contains__(name):
            line = item
    weight = int(re.findall('[0-9]+', line)[0])
    return weight


def find_bottom(list):
    not_bottom = re.findall('-> [a-z, ]+', list)
    for item in not_bottom:
        elements = item[3:].split(', ')
        for element in elements:
            list = list.replace(element, '')
    return re.search('[a-z]+', list)[0]


def solve07():
    list = open('inputs/day07.txt').read()
    print('Task 1:', find_bottom(list))
    lines = list.split('\n')
    total_weight(find_bottom(list), lines)
