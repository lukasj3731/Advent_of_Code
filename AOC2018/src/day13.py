import os.path


class cart:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.counter = 0

    def __str__(self):
        return str(self.y) + ',' + str(self.x)

    def move(self, tracks):
        self.y += self.c == '>'
        self.y -= self.c == '<'
        self.x += self.c == 'v'
        self.x -= self.c == '^'
        if ('^v'.__contains__(self.c) and tracks[self.x][self.y] == '/') or ('<>'.__contains__(self.c) and tracks[self.x][self.y] == '\\'):
            self.rotateC()
        elif '/\\'.__contains__(tracks[self.x][self.y]):
            self.rotateCC()
        if tracks[self.x][self.y] == '+':
            if self.counter % 3 == 0:
                self.rotateCC()
            if self.counter % 3 == 2:
                self.rotateC()
            self.counter += 1

    def rotateC(self):
        self.c = '<^>v'[('<^>v'.index(self.c)+1) % 4]

    def rotateCC(self):
        self.c = '<^>v'[('<^>v'.index(self.c)-1) % 4]

    def __lt__(self, other):
        return self.diff(other) < 0

    def __le__(self, other):
        return self.diff(other) <= 0

    def __eq__(self, other):
        return self.diff(other) == 0

    def __ne__(self, other):
        return self.diff(other) != 0

    def __gt__(self, other):
        return self.diff(other) > 0

    def __ge__(self, other):
        return self.diff(other) >= 0

    def diff(self, other):
        if self.x == other.x:
            return self.y - other.y
        else:
            return self.x - other.x


tracks = []
f = open(os.path.dirname(__file__) + '/../inputs/input13.txt').read().split('\n')
for line in f:
    tracks.append([char for char in line])
carts = []
for i in range(0, len(tracks)):
    for j in range(0, len(tracks[i])):
        if '><v^'.__contains__(tracks[i][j]):
            carts.append(cart(i, j, tracks[i][j]))
            if '><'.__contains__(tracks[i][j]):
                tracks[i][j] = '-'
            else:
                tracks[i][j] = '|'

noCollision = True

while noCollision:
    parking = []
    carts.sort()
    for i in range(0, len(carts)):
        cart = carts.pop(0)
        cart.move(tracks)
        if any(c.diff(cart) == 0 for c in carts + parking):
            print(cart)
            noCollision = False
        parking.append(cart)
    carts = parking

