def solve18():
    row = open('inputs/day18.txt').read()
    print('Task 1:', count_safe_tiles(row, 40))
    print('Task 2:', count_safe_tiles(row, 400000))


def count_safe_tiles(row, iterations):
    sum = 0
    for i in range(iterations):
        sum += row.count('.')
        row = iterate(row)
    return sum


def iterate(line):
    line = line+'..'
    return ''.join(['^' if line[i-1] != line[i+1] else '.' for i in range(len(line)-2)])
