import os.path
from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adj(self):
        return [Point(self.x + 1, self.y), Point(self.x - 1, self.y), Point(self.x, self.y + 1), Point(self.x, self.y - 1)]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def __hash__(self):
        return self.x*1000*self.y

class Player:
    def __init__(self, posx, posy, type, strength):
        self.pos = Point(posx, posy)
        self.type = type
        self.health = 200
        self.strength = 3 if type == 'G' else strength

    def __str__(self):
        return self.type + '[' + str(self.health) + '] @ ' + str(self.pos.x) + ',' + str(self.pos.y)

    def step(self, c):
        #print('1')
        cave = deepcopy(c)
        for i in range(0, len(cave)):   #friends are no target
            for j in range(0, len(cave[0])):
                if cave[i][j] == self.type:
                    cave[i][j] = '#'
        #print('2')
        #printCave(cave)

        inrange = []    #get in range enemies
        for i in range(0, len(cave)):
            for j in range(0, len(cave[0])):
                if 'GE'.__contains__(cave[i][j]):
                    inrange += Point(i, j).adj()
                    cave[i][j] = '#'
        for pt in inrange:
            if cave[pt.x][pt.y] == '.':     #and mark with '?'
                cave[pt.x][pt.y] = '?'

        #print('3')

        nextPoints = [self.pos] #get points with min distance
        seen = set()
        notdone = True
        nearest = []
        while notdone:
            tmp = []
            for pt in nextPoints:
                for adjp in pt.adj():
                    if not seen.__contains__(adjp) and cave[adjp.x][adjp.y] != '#':
                        tmp.append(adjp)
                        seen.add(adjp)
            for pt in tmp:
                if cave[pt.x][pt.y] == '?':
                    nearest.append(pt)
            nextPoints = tmp
            notdone = len(nearest) == 0 and len(tmp) != 0

        for i in range(0, len(cave)):
            for j in range(0, len(cave[0])):
                if cave[i][j] == '?':
                    cave[i][j] = '.'
        for pt in nearest:
            cave[pt.x][pt.y] = '@'

        #print('4')

        if len(nearest) == 0:
            return self.pos
        else:
            min = nearest[0]    #get min by reading order
            for pt in nearest:
                if pt.x < min.x or (pt.x == min.x and pt.y < min.y):
                    min = pt

            for i in range(0, len(cave)):
                for j in range(0, len(cave[0])):
                    if cave[i][j] == '@':
                        cave[i][j] = '.'
            cave[min.x][min.y] = '+'

            #print('5')

            seen = set()
            nextPoints = [min]
            notdone = True
            tmp = [min]
            while notdone:  #find path to take to that directionn
                for pt in nextPoints:
                    for adjp in pt.adj():
                        if not seen.__contains__(adjp) and cave[adjp.x][adjp.y] != '#':
                            tmp.append(adjp)
                            seen.add(adjp)
                adj = []
                for pt in self.pos.adj():
                    if tmp.__contains__(pt):
                        adj.append(pt)
                nextPoints = tmp
                notdone = len(adj) == 0 and len(tmp) != 0
                tmp = []
            min = adj[0]
            for pt in adj:  #get first step by reading order
                if pt.x < min.x or (pt.x == min.x and pt.y < min.y):
                    min = pt
            return min

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
        if self.pos.x == other.pos.x:
            return + self.pos.y - other.pos.y
        else:
            return + self.pos.x - other.pos.x


def printCave(cave):
    for i in range(0, len(cave)):
        for j in range(0, len(cave[0])):
            print(cave[i][j], end='')
        print()
    print()

def mainFun(strength):
    f = open(os.path.dirname(__file__) + '/../inputs/input15.txt').read().split()
    emptycave = []
    players = []
    for line in f:
        emptycave.append([char for char in line])
    for i in range(0, len(emptycave)):
        for j in range(0, len(emptycave[0])):
            if 'EG'.__contains__(emptycave[i][j]):
                players.append(Player(i, j, emptycave[i][j], strength))
                emptycave[i][j] = '.'
    round = 0
    allDed = False
    while not allDed:
        cave = deepcopy(emptycave)
        for player in players:
            cave[player.pos.x][player.pos.y] = player.type

        players.sort()

        playernum = 0
        while playernum < len(players):

            alive = ''
            for player in players:
                alive += player.type
            if not (alive.__contains__('E') and alive.__contains__('G')):
                sum = 0
                for pl in players:
                    sum += pl.health
                return(round, players)

            player = players[playernum]
            playernum += 1
            cave = deepcopy(emptycave)
            for p in players:
                cave[p.pos.x][p.pos.y] = p.type

            if not any(not (cave[player.pos.x][player.pos.y] + '#.').__contains__(cave[p.x][p.y]) for p in Point(player.pos.x, player.pos.y).adj()):
                player.pos = player.step(cave)
            adjPos = player.pos.adj()
            adjEnemies = []
            for enemy in players:
                if enemy.type != player.type and adjPos.__contains__(enemy.pos):
                    adjEnemies.append(enemy)
            if len(adjEnemies) > 0:
                minPlayer = adjEnemies[0]
                for enemy in adjEnemies:
                    if enemy.health < minPlayer.health:
                        minPlayer = enemy
                    if enemy.health == minPlayer.health and enemy.pos.x < minPlayer.pos.x:
                        minPlayer = enemy
                    if enemy.health == minPlayer.health and enemy.pos.x == minPlayer.pos.x and enemy.pos.y < minPlayer.pos.y:
                        minPlayer = enemy
                minPlayer.health -= player.strength
                if minPlayer.health <= 0:
                    if players.index(minPlayer) < playernum:
                        playernum -= 1
                    players.remove(minPlayer)
        round += 1


roundNum, players = mainFun(3)
sum = 0
for player in players:
    sum += player.health
print('task 1:', roundNum*sum)

NumberofElves = open(os.path.dirname(__file__) + '/../inputs/input15.txt').read().count('E')
elveStren = 3
elvesLost = True
while elvesLost:
    round, players = mainFun(elveStren)
    if players[0].type == 'E' and len(players) == NumberofElves:
        sum = 0
        for player in players:
            sum += player.health
        print('task 2:', sum * round)
        elvesLost = False
    elveStren += 1