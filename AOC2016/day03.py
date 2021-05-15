import re


def solve03():
    wall = [[int(x) for x in re.findall('[0-9]+', triplet)] for triplet in open('inputs/day03.txt').read().split('\n')]
    print('Task 1:', sum([max(n)*2 < sum(n) for n in wall]))
    wall = [item for sublist in [list(i) for i in zip(*wall)] for item in sublist]
    print('Task 2:', sum([max(wall[3*i:3*i+3])*2 < sum(wall[3*i:3*i+3]) for i in range(len(wall)//3)]))
