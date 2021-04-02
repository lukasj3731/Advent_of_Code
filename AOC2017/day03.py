def hamming_dist(n):    # used pen and paper to figure this one out
    a = 1
    while (a+2)*(a+2) < n:
        a += 2
    return int(a + 1 - ((a + 1) / 2) + abs((n - a * a) % (a + 1) - (a + 1) / 2)) if n > 1 else 0


def fillGrid(number):
    square = dict()
    square[(0, 0)] = 1
    pos = (1, 0)
    dir = (0, -1)
    n = 0
    while n < number:
        if square.__contains__(sum_t(pos, rotate(dir))):
            n = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    n += square.get((pos[0]+i, pos[1]+j), 0)
            square[pos] = n
            pos = sum_t(pos, dir)
        else:
            dir = rotate(dir)
    return n


def rotate(dir):
    x, y = dir
    return y, -x


def sum_t(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def solve03():
    number = int(open('inputs/day03.txt').read())
    print('task1:', hamming_dist(number))
    print('task2:', fillGrid(number))
