import itertools
import re


def solve09():
    file = open('inputs/day09.txt').read()
    cities = set()
    paths = dict()
    for city in re.findall('[A-Za-z]{3,}', file):
        cities.add(city)
    for dist in re.findall('([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)', file):
        paths[dist[0], dist[1]] = int(dist[2])
        paths[dist[1], dist[0]] = int(dist[2])
    min_path = 999999
    max_path = 0
    for iteration in list(itertools.permutations(list(cities))):
        dist = sum([paths[(iteration[i], iteration[i+1])] for i in range(len(iteration)-1)])
        min_path = min(min_path, dist)
        max_path = max(max_path, dist)
    return min_path, max_path
