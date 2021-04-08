def execute(instructions, mode):
    pos = 0
    step = 0
    while True:
        if not 0 <= pos < len(instructions):
            return step
        jmp = instructions[pos]
        if mode == 2 and instructions[pos] >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos += jmp
        step += 1


def solve05():
    instructions = [int(x) for x in open('inputs/day05.txt').read().split('\n')]
    print('Task 1:', execute(instructions.copy(), 1))
    print('Task 2:', execute(instructions, 2))
