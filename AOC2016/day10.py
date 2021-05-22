import re


def solve10():
    bots = dict()
    outputs = dict()
    rules = dict()
    for line in open('inputs/day10.txt').read().split('\n'):
        if line.__contains__('value'):
            numbers = [int(i) for i in re.findall('[0-9]+', line)]
            bots[numbers[1]] = bots.get(numbers[1], [])
            bots[numbers[1]].append(numbers[0])
        else:
            targets = re.findall('(bot|output) ([0-9]+)', line)
            rules[int(targets[0][1])] = [(targets[1][0], int(targets[1][1])), (targets[2][0], int(targets[2][1]))]
    print('Task 1: ', find_comparison(bots, outputs, rules, 61, 17))
    print('Task 2: ', find_comparison(bots, outputs, rules, -1, -1))


def find_comparison(bots, outputs, rules, c1, c2):
    while len([bot for bot in bots.keys() if len(bots[bot]) == 2]) > 0:
        bot = [bot for bot in bots.keys() if len(bots[bot]) == 2][0]
        min_val = min(bots[bot])
        max_val = max(bots[bot])
        if min_val == c2 and max_val == c1:
            return bot
        rule = rules[bot]
        if rule[0][0] == 'bot':
            bots[rule[0][1]] = bots.get(rule[0][1], [])
            bots[rule[0][1]].append(min_val)
        else:
            outputs[rule[0][1]] = min_val
        if rule[1][0] == 'bot':
            bots[rule[1][1]] = bots.get(rule[1][1], [])
            bots[rule[1][1]].append(max_val)
        else:
            outputs[rule[1][1]] = max_val
        bots[bot] = []
    return outputs[0]*outputs[1]*outputs[2]
