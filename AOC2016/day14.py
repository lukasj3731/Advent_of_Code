import hashlib
import re


def solve14():
    salt = open('inputs/day14.txt').read()
    print('Task 1:', find_64(lambda inp: hashlib.md5(bytes(inp, 'utf-8')).hexdigest(), salt))
    def keystretching(input):
        hashed = hashlib.md5(bytes(input, 'utf-8')).hexdigest()
        for i in range(2016):
            hashed = hashlib.md5(bytes(hashed, 'utf-8')).hexdigest()
        return hashed
    print('Task 2:', find_64(keystretching, salt))


def find_64(hash_func, salt):
    found_threes = dict()
    found_fives = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': []}
    ret = []
    i = 0
    while len(ret) < 64:
        hashed = hash_func(salt + str(i))
        three = re.findall(r'(.)\1\1', hashed)
        five = re.findall(r'(.)\1\1\1\1', hashed)
        if three:
            found_threes[i] = three[0]
        if five:
            found_fives[five[0]].append(i)
        if i - 1000 in found_threes:
            current_case = found_threes[i - 1000]
            if [item for item in found_fives[current_case] if i - 1000 < item <= i]:
                ret.append(i - 1000)
        i += 1
    return ret[63]
