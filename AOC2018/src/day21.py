import os.path


def doOp(input, instr):
    op = instr[0]
    if op == 0:  # addr
        input[instr[3]] = input[instr[1]] + input[instr[2]]
    if op == 1:  # addi
        input[instr[3]] = input[instr[1]] + instr[2]
    if op == 2:  # mulr
        input[instr[3]] = input[instr[1]] * input[instr[2]]
    if op == 3:  # muli
        input[instr[3]] = input[instr[1]] * instr[2]
    if op == 4:  # banr
        input[instr[3]] = input[instr[1]] & input[instr[2]]
    if op == 5:  # bani
        input[instr[3]] = input[instr[1]] & instr[2]
    if op == 6:  # borr
        input[instr[3]] = input[instr[1]] | input[instr[2]]
    if op == 7:  # bori
        input[instr[3]] = input[instr[1]] | instr[2]
    if op == 8:  # setr
        input[instr[3]] = input[instr[1]]
    if op == 9:  # seti
        input[instr[3]] = instr[1]
    if op == 10:  # gtir
        input[instr[3]] = (instr[1] > input[instr[2]]) * 1
    if op == 11:  # gtri
        input[instr[3]] = (input[instr[1]] > instr[2]) * 1
    if op == 12:  # gtrr
        input[instr[3]] = (input[instr[1]] > input[instr[2]]) * 1
    if op == 13:  # eqir
        input[instr[3]] = (instr[1] == input[instr[2]]) * 1
    if op == 14:  # eqri
        input[instr[3]] = (input[instr[1]] == instr[2]) * 1
    if op == 15:  # eqrr
        input[instr[3]] = (input[instr[1]] == input[instr[2]]) * 1


f = open(os.path.dirname(__file__) + '/../inputs/input21.txt').read()
for i in range(0, 16):
    op = 'addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr'.split(' ')[i]
    f = f.replace(op, str(i))
f = f.split('\n')
ip = int(f.pop(0).split(' ')[1])
opcodes = []
for line in f:
    opcodes.append([int(x) for x in line.split(' ')])
register = [0, 0, 0, 0, 0, 0]

register = [0, 0, 0, 0, 0, 0]
while register[ip] < len(opcodes):
    opcode = opcodes[register[ip]]
    doOp(register, opcode)
    register[ip] += 1
    if register[ip] == 28:
        break;
print('task 1:', register[opcodes[28][1]])
print('warning: task 2 takes a while')
register = [0, 0, 0, 0, 0, 0]
seen = set()
prev = -1

while True:
    opcode = opcodes[register[ip]]
    doOp(register, opcode)
    register[ip] += 1
    if register[ip] == 28:
        val = register[opcodes[28][1]]
        if seen.__contains__(val):
            break
        else:
            seen.add(val)
            prev = val
print('task 2:', prev)
