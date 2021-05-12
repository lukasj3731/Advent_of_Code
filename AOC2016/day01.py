turn = {((0, 1),  'R'): (1, 0),  ((0, 1),  'L'): (-1, 0),
        ((1, 0),  'R'): (0, -1), ((1, 0),  'L'):  (0, 1),
        ((0, -1), 'R'): (-1, 0), ((0, -1), 'L'):  (1, 0),
        ((-1, 0), 'R'): (0, 1),  ((-1, 0), 'L'): (0, -1)}


def solve01():
    pos_x = pos_y = 0
    seen = set()
    direction = (0, 1)
    task2 = None
    for instruction in open('inputs/day01.txt').read().split(', '):
        direction = turn[(direction, instruction[0])]
        for i in range(int(instruction[1:])):
            if seen.__contains__((pos_x, pos_y)):
                if not task2:
                    task2 = abs(pos_x)+abs(pos_y)
            else:
                seen.add((pos_x, pos_y))
            pos_x += direction[0]
            pos_y += direction[1]
    print('Task 1:', abs(pos_x) + abs(pos_y))
    print('Task 2:', task2)
