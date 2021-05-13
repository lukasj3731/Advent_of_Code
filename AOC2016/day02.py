def move(pos, dir, numbers):
    ret = (pos[0]+dir[0], pos[1]+dir[1])
    return ret if ret in numbers else pos


def crack_code(instructions, numbers):
    dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    ret = ''
    pos = list(numbers.keys())[list(numbers.values()).index('5')]
    for instr in instructions:
        for c in instr:
            pos = move(pos, dir[c], numbers)
        ret += numbers[pos]
    return ret


def solve02():
    instructions = open('inputs/day02.txt').read().split('\n')
    keypad = {(-1, -1): '1', (-1, 0): '2', (-1, 1): '3', (0, -1): '4', (0, 0): '5', (0, 1): '6', (1, -1): '7', (1, 0): '8', (1, 1): '9'}
    print('Task 1:', crack_code(instructions, keypad))
    keypad = {(-2, 0): '1', (-1, -1): '2', (-1, 0): '3', (-1, 1): '4', (0, -2): '5',  (0, -1): '6', (0, 0): '7', (0, 1): '8', (0, 2): '9', (1, -1): 'A', (1, 0): 'B', (1, 1): 'C', (2, 0): 'D'}
    print('Task 2:', crack_code(instructions, keypad))
