import itertools
import re


def solve13():
    scores = dict()
    all_names = set()
    for ranking in open('inputs/day13.txt').read().split('\n'):
        names = re.findall('([A-Z][a-z]+)', ranking)
        score = int(re.findall('([0-9]+)', ranking)[0])
        sign = -1 if ranking.__contains__('lose') else 1
        all_names.add(names[0])
        all_names.add(names[1])
        scores[names[0], names[1]] = score * sign

    score1 = find_max_score(all_names, scores)

    for name in all_names:
        scores['lukasj3731', name] = 0
        scores[name, 'lukasj3731'] = 0
    all_names.add('lukasj3731')

    return score1, find_max_score(all_names, scores)


def find_max_score(names, scores):
    max_score = 0
    for permutation in list(itertools.permutations(names)):
        score = 0
        for i in range(len(permutation)):
            score += scores[permutation[i], permutation[i - 1]]
            score += scores[permutation[i], permutation[(i + 1) % len(permutation)]]
        max_score = max(max_score, score)
    return max_score