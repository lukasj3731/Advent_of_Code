import os

f = open(os.path.dirname(__file__) + '/../inputs/input25.txt').read().split('\n')
points = [[int(n) for n in point.split(',')] for point in f]
constellations = 0

while len(points) > 0:
    curr = [points.pop()]
    constellations += 1
    for p1 in curr:
        for p2 in reversed(points):
            if sum([abs(p1[i]-p2[i]) for i in range(4)]) <= 3:
                curr.append(p2)
                points.remove(p2)

print('task 1:', constellations)
print('task 2: Merry Christmas!')
