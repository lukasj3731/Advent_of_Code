from hashlib import md5


def solve04():
    salt = open('inputs/day04.txt').read()
    index = 0
    h1 = h2 = False
    while not h1 or not h2:
        hash = md5((salt+str(index)).encode('utf-8')).hexdigest()
        if hash[0:5] == '00000':
            if not h1:
                h1 = index
            if hash[5] == '0' and not h2:
                h2 = index
        index += 1
    return h1, h2
