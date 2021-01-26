import os.path
import re


class Marble:
    def __init__(self, nxt, prev, val):
        if val != 0:
            self.nxt = nxt
            self.prev = prev
            self.val = val
        else:
            self.nxt = self
            self.prev = self
            self.val = 0


def highscore(playernum, marbles):
    curr = Marble(0, 0, 0)
    players = []
    for i in range(0, playernum):
        players.append(0)

    for i in range(1, marbles + 1):
        if i % 23:
            curr = curr.nxt
            curr.nxt = Marble(curr.nxt, curr, i)
            curr = curr.nxt
            curr.nxt.prev = curr
        else:
            for a in range(0, 7):
                curr = curr.prev
            players[i % playernum] += i + curr.val
            curr.prev.nxt = curr.nxt
            curr = curr.nxt
    return max(players)


f = open(os.path.dirname(__file__) + '/../inputs/input09.txt').read()
f = re.findall('[0-9]+', f)
print(highscore(int(f[0]), int(f[1])))
print(highscore(int(f[0]), 100*int(f[1])))

