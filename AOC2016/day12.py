def solve12():
    print('Task 1:', get_a_reg(0))
    print('Task 1:', get_a_reg(1))


def get_a_reg(value):
    variables = {'a': 0, 'b': 0, 'c': value, 'd': 0}
    index = 0
    instructions = [line.split(' ') for line in open('inputs/day12.txt').read().split('\n')]
    while index < len(instructions):
        if instructions[index][0] == 'cpy':
            variables[instructions[index][2]] = get_value(variables, instructions[index][1])
        elif instructions[index][0] == 'inc':
            variables[instructions[index][1]] += 1
        elif instructions[index][0] == 'dec':
            variables[instructions[index][1]] -= 1
        else:
            if get_value(variables, instructions[index][1]) != 0:
                index += get_value(variables, instructions[index][2]) - 1
        index += 1
    return variables['a']


def get_value(variables, val):
    if 'a' <= val <= 'd':
        return variables[val]
    else:
        return int(val)
