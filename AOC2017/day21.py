def solve21():
    file = open('inputs/day21.txt').read().split('\n')
    rules = dict()
    for rule in file:
        components = rule.split(' => ')
        previous = components[0]
        next = components[1]
        for i in range(4):
            rules[previous] = next
            previous = rotate(previous)
        previous = flip(previous)
        for i in range(4):
            rules[previous] = next
            previous = rotate(previous)
    arr = '.#./..#/###'
    for iterations in range(18):
        step = 2 if len(arr.split('/')) % 2 == 0 else 3
        iter = len(arr.split('/')) // step
        complete = ''
        split_arr = arr.split('/')
        for i in range(iter):
            rows = ''
            for j in range(iter):
                rows = horizontal_fuse(rows, rules[get_subarray(split_arr, i, j, step)])
            complete = vertical_fuse(complete, rows)
        arr = complete
        if iterations == 5 - 1:
            print('Task 1:', complete.count('#'))
        if iterations == 18 - 1:
            print('Task 2:', complete.count('#'))


def rotate(pattern):
    ret = ''
    for line in zip(*pattern.split('/')[::-1]):
        ret += '/'
        for item in line:
            ret += item
    return ret[1:]


def flip(pattern):
    ret = ''
    for line in pattern.split('/'):
        ret += '/'+line[::-1]
    return ret[1:]


def get_subarray(arr, posx, posy, step):
    ret = ''
    for i in range(step*posx, step*posx+step):
        ret += '/'
        for j in range(step*posy, step*posy+step):
            ret += arr[i][j]
    return ret[1:]


def horizontal_fuse(arr1, arr2):
    if arr1 == '':
        return arr2
    lines1 = arr1.split('/')
    lines2 = arr2.split('/')
    ret = ''
    for i in range(len(lines1)):
        ret += '/'
        ret += lines1[i]+lines2[i]
    return ret[1:]


def vertical_fuse(arr1, arr2):
    if arr1 == '':
        return arr2
    return arr1+'/'+arr2
