import re


def solve06():
    method1 = {'toggle': lambda light: not light,
               'turn on': lambda light: True,
               'turn off': lambda light: False}
    method2 = {'toggle': lambda light: light + 2,
               'turn on': lambda light: light + 1,
               'turn off': lambda light: light - 1 if light > 0 else 0}
    lights1 = [[False for x in range(1000)] for y in range(1000)]
    lights2 = [[0 for x in range(1000)] for y in range(1000)]
    for instr, x1, y1, x2, y2 in re.findall('(toggle|turn on|turn off) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)',
                                            open('inputs/day06.txt').read()):
        for x in range(int(x1), int(x2)+1):
            for y in range(int(y1), int(y2)+1):
                lights1[x][y] = method1[instr](lights1[x][y])
                lights2[x][y] = method2[instr](lights2[x][y])
    return sum([light for row in lights1 for light in row]), sum([light for row in lights2 for light in row])
