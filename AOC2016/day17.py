import hashlib


def possible_ways(passcode, path):
    hash = hashlib.md5(bytes(passcode+path, 'utf-8')).hexdigest()
    return hash[0] > 'a' and path.count('D') > path.count('U'), \
           hash[1] > 'a' and path.count('D') < path.count('U') + 3, \
           hash[2] > 'a' and path.count('R') > path.count('L'), \
           hash[3] > 'a' and path.count('R') < path.count('L') + 3


def solve17():
    passcode = open('inputs/day17.txt').read()
    longest_path = ''
    shortest_path = ''
    paths = ['']
    while paths:
        nxt = []
        for path in paths:
            if path.count('D')-3 == path.count('U') and path.count('R')-3 == path.count('L'):
                if shortest_path == '':
                    shortest_path = path
                longest_path = path
            else:
                ways = possible_ways(passcode, path)
                if ways[0]:
                    nxt.append(path + 'U')
                if ways[1]:
                    nxt.append(path + 'D')
                if ways[2]:
                    nxt.append(path + 'L')
                if ways[3]:
                    nxt.append(path + 'R')
        paths = nxt
    print('Task 1:', shortest_path)
    print('Task 2:', len(longest_path))
