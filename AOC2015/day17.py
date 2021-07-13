from itertools import chain, combinations


def solve17():
    valid = 0
    min_len = 999999
    num_with_min_len = 0
    for item in powerset([int(x) for x in open('inputs/day17.txt').read().split('\n')]):
        if sum(item) == 150:
            valid += 1
            length = len(item)
            if length == min_len:
                num_with_min_len += 1
            elif length < min_len:
                min_len = length
                num_with_min_len = 1
    return valid, num_with_min_len


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
