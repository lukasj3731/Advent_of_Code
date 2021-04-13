
def solve10():
    inputs = [int(x) for x in open('inputs/day10.txt').read().split(',')]
    list = [x for x in range(256)]
    scramble_list(list, inputs, 1)
    print('Task 1:', list[0]*list[1])

    inputs = [ord(c) for c in open('inputs/day10.txt').read()]+[17, 31, 73, 47, 23]
    list = [x for x in range(256)]
    scramble_list(list, inputs, 64)
    print('Task 2:', condense(list))


def scramble_list(list, inputs, n):
    curr_pos = skip_size = 0
    for iter in range(n):
        for l in inputs:
            for i in range(l // 2):
                swap(list, curr_pos + i, curr_pos + l - i - 1)
            curr_pos += l + skip_size
            curr_pos %= len(list)
            skip_size += 1


def condense(list):
    hash = ''
    for block in range(16):
        xor = 0
        for elem in range(16):
            xor = xor ^ list[16 * block + elem]
        hash += "{:02x}".format(xor)
    return hash


def swap(list, a, b):
    a %= len(list)
    b %= len(list)
    tmp = list[a]
    list[a] = list[b]
    list[b] = tmp
