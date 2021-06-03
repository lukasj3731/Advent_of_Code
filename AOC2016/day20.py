import re


def solve20():
    tuples = []
    free = []
    for line in open('inputs/day20.txt').read().split('\n'):
        numbers = [int(n) for n in re.findall('[0-9]+', line)]
        tuples.append(numbers)
    tuples.sort()
    curr_max = 0
    for i in range(len(tuples)):
        if tuples[i][0] > curr_max + 1:
            free.append([curr_max+1, tuples[i][0]-1])
        curr_max = max(tuples[i][1], curr_max)
    if curr_max < 4294967295:
        free.append([curr_max+1, 4294967295])
    print('Task 1:', free[0][0])
    print('Task 2:', sum([n[1]-n[0]+1 for n in free]))
