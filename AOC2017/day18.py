def solve18():
    variables = dict()
    output = [0]
    for i in range(26):
        variables[chr(i + ord('a'))] = 0
    index = 0
    instructions = open('inputs/day18.txt').read().split('\n')
    while index is not None:
        index = step(instructions, variables, output, output, index, 1)
    variables1 = dict()
    variables2 = dict()
    output1 = []
    output2 = []
    for i in range(26):
        variables1[chr(i + ord('a'))] = 0
        variables2[chr(i + ord('a'))] = 0
    variables2['p'] = 1
    index1 = index2 = counter = 0
    while not (instructions[index1][:3] == 'rcv' == instructions[index2][:3] and len(output1) == 0 == len(output2)):
        if instructions[index2][:3] == 'snd':
            counter += 1
        index1 = step(instructions, variables1, output1, output2, index1, 2)
        index2 = step(instructions, variables2, output2, output1, index2, 2)
    print('Task 2:', counter)


def get_value(operation, variables):
    return [variables[x] if 'a' <= x <= 'z' else int(x) for x in operation.split(' ')[1:]]


def step(instructions, variables, output, input, index, task):
    if index >= len(instructions):
        return
    operation = instructions[index]
    if operation[:3] == 'snd':
        if task == 1:
            output[0] = get_value(operation, variables)[0]
        else:
            output.append(get_value(operation, variables)[0])
    elif operation[:3] == 'set':
        variables[operation.split(' ')[1]] = get_value(operation, variables)[1]
    elif operation[:3] == 'add':
        variables[operation.split(' ')[1]] += get_value(operation, variables)[1]
    elif operation[:3] == 'mul':
        variables[operation.split(' ')[1]] *= get_value(operation, variables)[1]
    elif operation[:3] == 'mod':
        variables[operation.split(' ')[1]] %= get_value(operation, variables)[1]
    elif operation[:3] == 'rcv':
        if task == 1:
            if get_value(operation, variables)[0] != 0:
                print('Task 1:', input[0])
                return
        else:
            if len(input) > 0:
                variables[operation.split(' ')[1]] = input.pop(0)
            else:
                return index
    elif operation[:3] == 'jgz':
        values = get_value(operation, variables)
        if values[0] > 0:
            index += values[1] - 1
    index += 1
    return index
