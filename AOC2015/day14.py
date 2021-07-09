import re


def solve14():
    duration = 2503
    all_reindeer = [[int(x) for x in re.findall('[0-9]+', line)] for line in open('inputs/day14.txt').read().split('\n')]
    scores = dict()
    for seconds in range(1, duration+1):
        best_reindeer = []
        highest_score = -1
        for i in range(len(all_reindeer)):
            d = distance(all_reindeer[i], seconds)
            if d == highest_score:
                best_reindeer.append(i)
            elif d > highest_score:
                highest_score = d
                best_reindeer = [i]
        for leader in best_reindeer:
            scores[leader] = scores.get(leader, 0) + 1
    return max([distance(reindeer, duration) for reindeer in all_reindeer]), max(scores.values())


def distance(reindeer, duration):
    return (duration//(reindeer[1]+reindeer[2]))*reindeer[1]*reindeer[0] + \
           min(reindeer[1]*reindeer[0], (duration % (reindeer[1]+reindeer[2]))*reindeer[0])
