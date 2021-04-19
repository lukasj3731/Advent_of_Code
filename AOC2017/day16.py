def solve16():
    programs = 'abcdefghijklmnop'
    instructions = open('inputs/day16.txt').read().split(',')
    for instr in instructions:
        programs = do_op(programs, instr)
    print('Task 1:',programs)


def do_op(programs, instr):
    if instr[0] == 's':
        value = int(instr[1:])
        programs = programs[len(programs)-value:] + programs[:len(programs)-value]
    elif instr[0] == 'x':
        characters = [programs[int(x)] for x in instr[1:].split('/')]
        programs = programs.replace(characters[0], '_')
        programs = programs.replace(characters[1], characters[0])
        programs = programs.replace('_', characters[1])
    elif instr[0] == 'p':
        characters = instr[1:].split('/')
        programs = programs.replace(characters[0], '_')
        programs = programs.replace(characters[1], characters[0])
        programs = programs.replace('_', characters[1])
    return programs
