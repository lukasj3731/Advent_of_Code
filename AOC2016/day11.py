import re


def solve11():
    file = open('inputs/day11.txt').read().split('\n')
    floors = []
    seen = set()
    for i in range(4):
        floor = re.findall('([a-z]+)\-[a-z]+ (microchip)', file[3-i]) + re.findall('([a-z]+) (generator)', file[3 - i])
        floors.append(floor)
    state = to_string(floors, 3)
    curr = [state]
    iterations = 0
    while True:
        nxt = []
        for curr_state in curr:
            if curr_state not in seen:
                if is_solved(curr_state):
                    print('Task 1:', iterations)
                    print('Task 2:', iterations+24)
                    return
                nxt = nxt + next_possible(curr_state)
                seen.add(curr_state)
        curr = nxt
        iterations += 1


def is_solved(state):
    components = state.split(';')
    if len(components[2]) == len(components[3]) == len(components[4]) == 0:
        return True
    return False


def to_string(floors, elevator):
    return str(elevator)+';'+';'.join([','.join([item[0]+'-'+item[1] for item in sorted(floor)]) for floor in floors])


def to_obj(state):
    elevator = int(state[0])
    floors = [[item.split('-') for item in floor.split(',')] if len(floor) > 0 else [] for floor in state.split(';')[1:]]
    return floors, elevator


def next_possible(state):
    floors, elevator = to_obj(state)
    possible = []
    for item in floors[elevator]:
        possible.append([item])
        for item_two in floors[elevator]:
            if item_two != item:
                possible.append([item, item_two])
    nxt = []
    for items in possible:
        for i in [-1, 1]:
            if elevator + i > 3 or elevator + i < 0:
                continue
            else:
                for item in items:
                    floors[elevator].remove(item)
                    floors[elevator + i].append(item)
                    state = to_string(floors, elevator + i)
                if is_valid(state):
                    nxt.append(state)
                for item in items:
                    floors[elevator + i].remove(item)
                    floors[elevator].append(item)
    return nxt


def is_valid(state):
    for line in state.split(';')[1:]:
        for item in line.split(','):
            if item.__contains__('microchip'):
                if line.__contains__('generator') and not line.__contains__(item.split('-')[0]+'-generator'):
                    return False
    return True
