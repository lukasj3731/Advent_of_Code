import re


def is_open(time, disc):
    return (time+disc[0]+disc[2]) % disc[1] == 0


def opening_time(discs):
    time = 0
    while not all([is_open(time, disc) for disc in discs]):
        time += 1
    return time


def solve15():
    discs = []
    for elem in open('inputs/day15.txt').read().split('\n'):
        numbers = [int(n) for n in re.findall('[0-9]+', elem)]
        discs.append((numbers[0], numbers[1], numbers[3]))
    print('Task 1:', opening_time(discs))
    discs.append((7, 11, 0))
    print('Task 2:', opening_time(discs))
