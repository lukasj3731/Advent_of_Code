def flip(input):
    return ''.join(['1' if char == '0' else '0' for char in input[::-1]])


def checksum(data):
    ret = ''
    for i in range(0,len(data)-1,2):
        ret += '1' if data[i] == data[i+1] else '0'
    return ret


def get_checksum(data, disc_size):
    while len(data) < disc_size:
        data = data+'0'+flip(data)
    data = data[:disc_size]
    while len(data) % 2 == 0:
        data = checksum(data)
    return data


def solve16():
    data = open('inputs/day16.txt').read()
    print('Task 1:', get_checksum(data, 272))
    print('Task 2:', get_checksum(data, 35651584))
