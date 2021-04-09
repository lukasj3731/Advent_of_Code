def solve08():
    instructions = open('inputs/day08.txt').read().replace('inc', '+=').replace('dec', '-=').split('\n')
    for instr in instructions:
        exec(instr.split(' ')[0]+' = 0')
    max_val_1 = max_val_2 = 0
    for instr in instructions:
        exec(instr + ' else 0')
        for variable in dir():
            if len(variable) <= 3:
                max_val_2 = max(max_val_2, eval(variable))
    for variable in dir():
        if len(variable) <= 3:
            max_val_1 = max(max_val_1, eval(variable))
    print('Task 1:', max_val_1)
    print('Task 2:', max_val_2)
