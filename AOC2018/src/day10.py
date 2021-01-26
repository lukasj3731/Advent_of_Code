import os.path
import re


class Star:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self. dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def getPos(self):
        return self.x, self.y


def starsaligned(stars):
    miny = minx = 99999
    maxy = maxx = -99999
    for star in stars:
        x, y = star.getPos()
        miny = min(miny, y)
        maxy = max(maxy, y)
        minx = min(minx, x)
        maxx = max(maxx, x)
    #print(abs(miny-maxy), abs(minx-maxx))
    return abs(miny-maxy) < 10

f = open(os.path.dirname(__file__) + '/../inputs/input10.txt').read().split('\n')
stars = []
for line in f:
    c = re.findall('(-?[0-9]+)', line)
    stars.append(Star(int(c[0]), int(c[1]), int(c[2]), int(c[3])))

seconds = 0

while not starsaligned(stars):
    for star in stars:
        star.move()
    seconds += 1

miny = minx = 99999
maxy = maxx = -99999

for star in stars:
    x, y = star.getPos()
    miny = min(miny, y)
    maxy = max(maxy, y)
    minx = min(minx, x)
    maxx = max(maxx, x)

sky = dict()
for star in stars:
    sky[str(star.x)+','+str(star.y)] = '#'
    #print(str(star.x)+','+str(star.y))

print('task 1:')

for i in range(miny, maxy+1):
    for j in range(minx, maxx+1):
        print(sky.get((str(j)+','+str(i)), ' '), end='')
        #print(str(i)+','+str(j))
    print()

print('task 2:', seconds)

