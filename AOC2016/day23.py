import re
import math


def solve23():
    variables = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    index = 0
    instructions = [line.split(' ') for line in open('inputs/day23.txt').read().split('\n')]
    while index < len(instructions):
        if instructions[index][0] == 'tgl':
            val = get_value(variables, instructions[index][1])
            if index+val < len(instructions):
                instructions[index+val][0] = switch(instructions[index+val])
        elif instructions[index][0] == 'cpy':
            variables[instructions[index][2]] = get_value(variables, instructions[index][1])
        elif instructions[index][0] == 'inc':
            variables[instructions[index][1]] += 1
        elif instructions[index][0] == 'dec':
            variables[instructions[index][1]] -= 1
        else:
            if get_value(variables, instructions[index][1]) != 0:
                index += get_value(variables, instructions[index][2]) - 1
        index += 1
    print('Task 1:', variables['a'])
    numbers = [int(x) for x in re.findall('[0-9]+', open('inputs/day23.txt').read())]
    numbers.sort()
    print('Task 2:', numbers[-1] * numbers[-2] + math.factorial(12))


def get_value(variables, val):
    if 'a' <= val <= 'd':
        return variables[val]
    else:
        return int(val)


def switch(instr):
    if len(instr) == 2:
        return 'dec' if instr[0] == 'inc' else 'inc'
    else:
        return 'cpy' if instr[0] == 'jnz' else 'jnz'
