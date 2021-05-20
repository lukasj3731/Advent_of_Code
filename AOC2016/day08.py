import re


def solve08():
    screen = []
    for i in range(6):
        line = []
        for j in range(50):
            line.append(' ')
        screen.append(line)
    for instr in open('inputs/day08.txt').read().split('\n'):
        screen = do_instr(instr, screen)
    s = '\n'.join([''.join(i) for i in screen])
    print('Task 1:', s.count('#'))
    print('Task 2:', '\n'+s)


def do_instr(instr, screen):
    if instr.__contains__('rect'):
        size = [int(i) for i in re.findall('[0-9]+', instr)]
        for x in range(size[1]):
            for y in range(size[0]):
                screen[x][y] = '#'
    elif instr.__contains__('row'):
        values = [int(i) for i in re.findall('[0-9]+', instr)]
        screen[values[0]] = rotate(screen[values[0]], -values[1])
    else:
        values = [int(i) for i in re.findall('[0-9]+', instr)]
        screen = [list(i) for i in zip(*screen)]
        screen[values[0]] = rotate(screen[values[0]], -values[1])
        screen = [list(i) for i in zip(*screen)]
    return screen


def rotate(l, n):
    return l[n:] + l[:n]
