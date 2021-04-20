def solve16():
    programs = 'abcdefghijklmnop'
    instructions = open('inputs/day16.txt').read().split(',')
    seen = dict()
    i = 1
    while True:
        for instr in instructions:
            programs = do_op(programs, instr)
        if programs in seen.keys():
            break
        else:
            seen[programs] = i
            i += 1
    loop = i - seen[programs]
    iterations = 1000000000 % loop
    programs = 'abcdefghijklmnop'
    for i in range(iterations + loop):
        for instr in instructions:
            programs = do_op(programs, instr)
        if i == 0:
            print('Task 1:', programs)
    print('Task 2:', programs)


def do_op(programs, instr):
    if instr[0] == 's':
        value = int(instr[1:])
        return programs[len(programs)-value:] + programs[:len(programs)-value]
    else:
        characters = [programs[int(x)] for x in instr[1:].split('/')] if instr[0] == 'x' else instr[1:].split('/')
        programs = programs.replace(characters[0], '_')
        programs = programs.replace(characters[1], characters[0])
        programs = programs.replace('_', characters[1])
        return programs
