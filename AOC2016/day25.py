import re
import math


def solve25():
    i = 0
    while not gen_output(i):
        i += 1
    print('Task 1:', i)
    print('Task 2: Merry Christmas!')


def gen_output(starting_value):
    variables = {'a': starting_value, 'b': 0, 'c': 0, 'd': 0}
    index = 0
    instructions = [line.split(' ') for line in open('inputs/day25.txt').read().split('\n')]
    output = []
    while index < len(instructions) and len(output) < 50 and output_valid(output):
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
        elif instructions[index][0] == 'jnz':
            if get_value(variables, instructions[index][1]) != 0:
                index += get_value(variables, instructions[index][2]) - 1
        else:
            output.append(get_value(variables, instructions[index][1]))
        index += 1
    if output_valid(output):
        return True
    else:
        return False


def output_valid(output):
    for i in range(len(output)):
        if output[i] != i % 2:
            return False
    return True


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
