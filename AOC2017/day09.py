import re


def solve09():
    stream = open('inputs/day09.txt').read()
    cleaned = remove_garbage(stream)
    print('Task 1:', count_score(re.sub('(<|>|!.)', '', cleaned)))
    print('Task 2:', len(stream)-len(cleaned))


def count_score(stream):
    points = level = 0
    for i in range(len(stream)):
        if stream[i] == '{':
            level += 1
            points += level
        if stream[i] == '}':
            level -= 1
    return points


def remove_garbage(stream):
    i = 0
    while i < len(stream):
        i += 1
        if stream[i-1] == '<':
            while stream[i] != '>':
                if stream[i] == '!':
                    i += 2
                else:
                    stream = stream[:i] + stream[(i + 1):]
    return stream
