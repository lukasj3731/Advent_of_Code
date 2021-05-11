import re


def solve25():
    file = open('inputs/day25.txt').read().split('\n\n')
    print(file)
    begin_state = file[0].split(' ')[3][0]
    iterations = int(re.findall('[0-9]+', file[0])[0])
    nxt = dict()
    tape = dict()
    for state_rules in file[1:]:
        state = state_rules.split(' ')[2][0]
        for current_val_rules in state_rules.split('If the')[1:]:
            lines = current_val_rules.split('\n')
            current_val = int(re.findall('[0-9]+', lines[0])[0])
            write = int(re.findall('[0-9]+', lines[1])[0])
            to = 1 if re.findall('left|right', lines[2])[0] == 'right' else -1
            next_state = re.findall('[A-Z]', lines[3])[-1]
            nxt[(state, current_val)] = (write, to, next_state)
    pos = 0
    curr_state = begin_state
    for num_iteration in range(iterations):
        curr_val = tape.get(pos, 0)
        nxt_val, dir, nxt_state = nxt[(curr_state, curr_val)]
        tape[pos] = nxt_val
        pos += dir
        curr_state = nxt_state
    print('Task 1:', sum(tape.values()))
    print('Task 2: Merry Christmas!')
