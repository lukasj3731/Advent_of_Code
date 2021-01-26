import os.path


def powerlevel(x, y, serial):
    rackID = x + 10
    lvl = rackID * y
    lvl += serial
    lvl *= rackID
    lvl = (lvl//100) % 10
    return lvl - 5

f = int(open(os.path.dirname(__file__) + '/../inputs/input11.txt').read())

grid = dict()
table = []
for row in range(1, 301):
    tmp = []
    for col in range(1, 301):
        tmp.append(0)
    table.append(tmp)

for i in range(1, 301):
    for j in range(1, 301):
        grid[str(i)+','+str(j)] = powerlevel(i, j, f) \
                                  + grid.get(str(i-1)+','+str(j), 0) + grid.get(str(i)+','+str(j-1), 0) \
                                  - grid.get(str(i-1)+','+str(j-1), 0)

max = 0
pos = ''
for i in range(1, 298):
    for j in range(1, 298):
        sum = grid[str(i+3)+','+str(j+3)] - grid[str(i+3)+','+str(j)] - grid[str(i)+','+str(j+3)] + grid[str(i)+','+str(j)]
        if sum > max:
            max = sum
            pos = str(i+1)+','+str(j+1)

print('task 1:', pos)

max = 0
pos = ''
for s in range(1, 301):
    for i in range(1, 300 - s + 1):
        for j in range(1, 300 - s + 1):
            sum = grid[str(i+s)+','+str(j+s)] - grid[str(i+s)+','+str(j)] - grid[str(i)+','+str(j+s)] + grid[str(i)+','+str(j)]
            if sum > max:
                max = sum
                pos = pos = str(i+1)+','+str(j+1)+','+str(s)

print('task 2:', pos)

