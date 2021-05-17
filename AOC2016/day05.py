import hashlib


def solve05():
    seed = open('inputs/day05.txt').read()
    i = 0
    ret1 = ''
    ret2 = dict()
    while len(ret2) < 8:
        md5 = hash_md5(seed + str(i))
        if md5[:5] == '00000':
            ret1 += md5[5]
            if ret2.get(md5[5], '.') == '.' and '0' <= md5[5] <= '7':
                ret2[md5[5]] = md5[6]
        i += 1
    print('Task 1:', ret1[:8])
    print('Task 2: ', end='')
    for i in range(8):
        print(ret2[str(i)], end='')


def hash_md5(input):
    return hashlib.md5(bytes(input, 'utf-8')).hexdigest()
