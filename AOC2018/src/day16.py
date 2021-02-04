import os.path
import re
from copy import deepcopy


def doOp(op, input, instr):
    if op == 0:  # addr
        input[instr[3]] = input[instr[1]] + input[instr[2]]
        return input
    if op == 1:  # addi
        input[instr[3]] = input[instr[1]] + instr[2]
        return input
    if op == 2:  # mulr
        input[instr[3]] = input[instr[1]] * input[instr[2]]
        return input
    if op == 3:  # muli
        input[instr[3]] = input[instr[1]] * instr[2]
        return input
    if op == 4:  # banr
        input[instr[3]] = input[instr[1]] & input[instr[2]]
        return input
    if op == 5:  # bani
        input[instr[3]] = input[instr[1]] & instr[2]
        return input
    if op == 6:  # borr
        input[instr[3]] = input[instr[1]] | input[instr[2]]
        return input
    if op == 7:  # bori
        input[instr[3]] = input[instr[1]] | instr[2]
        return input
    if op == 8:  # setr
        input[instr[3]] = input[instr[1]]
        return input
    if op == 9:  # seti
        input[instr[3]] = instr[1]
        return input
    if op == 10:  # gtir
        input[instr[3]] = (instr[1] > input[instr[2]]) * 1
        return input
    if op == 11:  # gtri
        input[instr[3]] = (input[instr[1]] > instr[2]) * 1
        return input
    if op == 12:  # gtrr
        input[instr[3]] = (input[instr[1]] > input[instr[2]]) * 1
        return input
    if op == 13:  # eqir
        input[instr[3]] = (instr[1] == input[instr[2]]) * 1
        return input
    if op == 14:  # eqri
        input[instr[3]] = (input[instr[1]] == instr[2]) * 1
        return input
    if op == 15:  # eqrr
        input[instr[3]] = (input[instr[1]] == input[instr[2]]) * 1
        return input


f = open(os.path.dirname(__file__) + '/../inputs/input16.txt').read()
sum = 0
for l in f.split('\n\n\n')[0].split('\n\n'):
    comp = l.split('\n')
    input = [int(x) for x in re.findall('[0-9]+', comp[0])]
    instr = [int(x) for x in re.findall('[0-9]+', comp[1])]
    result = [int(x) for x in re.findall('[0-9]+', comp[2])]
    possible = 0
    for i in range(0, 16):
        possible += doOp(i, input.copy(), instr) == result
    sum += possible >= 3
print('task 1:', sum)

opCodes = []
for i in range(0, 16):
    possible = []
    for m in range(0, 16):
        possible.append(m)
    opCodes.append(possible)

for l in f.split('\n\n\n\n')[0].split('\n\n'):
    comp = l.split('\n')
    input = [int(x) for x in re.findall('[0-9]+', comp[0])]
    instr = [int(x) for x in re.findall('[0-9]+', comp[1])]
    result = [int(x) for x in re.findall('[0-9]+', comp[2])]
    possible = []
    for i in range(0, 16):
        if doOp(i, input.copy(), instr) == result:
            possible.append(i)
    opCodes[instr[0]] = [value for value in possible if value in opCodes[instr[0]]]

opcodesResolved = dict()
while any(len(code) >= 1 for code in opCodes):
    min = -1
    for i in range(len(opCodes)):
        if len(opCodes[i]) == 1:
            min = i
    correctCode = opCodes[min][0]
    opcodesResolved[min] = correctCode
    for i in range(len(opCodes)):
        if opCodes[i].__contains__(correctCode):
            opCodes[i].remove(correctCode)

register = [0, 0, 0, 0]
for operation in f.split('\n\n\n\n')[1].split('\n'):
    opCode = [int(x) for x in re.findall('[0-9]+', operation)]
    register = doOp(opcodesResolved[opCode[0]], register, opCode)
print('task 2:', register[0])

