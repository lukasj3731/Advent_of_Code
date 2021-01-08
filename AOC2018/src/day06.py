import os.path


f = open(os.path.dirname(__file__) + '/../inputs/input06.txt').read().split('\n')
ymin, ymax = 1, 0
xmin, xmax = 1, 0

for line in f:
    ymax = max(ymax, int(line.split(', ')[0]))
    xmax = max(xmax, int(line.split(', ')[1]))

field = []

for i in range(ymin-1, ymax+1):
    new = []
    for j in range(xmin-1, xmax+1):
        new.append(-1)
    field.append(new)
f = open(os.path.dirname(__file__) + '/../inputs/input06.txt').read().split('\n')
for i in range(0, len(field)):
    for j in range(0, len(field[i])):
        minimum = 999999
        for line in f:
            dist = abs(i-int(line.split(', ')[0]))+ abs(j-int(line.split(', ')[1]))
            minimum = min(minimum, dist)

        nearest = -1
        for l in range(0, len(f)):
            line = f[l]
            dist = abs(i - int(line.split(', ')[0])) + abs(j - int(line.split(', ')[1]))
            if dist == minimum:
                if nearest == -1:
                    nearest = l
                else:
                    nearest = -2
        field[i][j] = nearest
rim = set()
for i in range(0, len(field)):
    rim.add(field[i][0])
    rim.add(field[i][len(field[i])-1])
for i in range(0, len(field[0])):
    rim.add(field[0][i])
    rim.add(field[len(field)-1][i])
count = dict()
for i in range(0, len(field)):
    for j in range (0, len(field[i])):
        count[field[i][j]] = count.get(field[i][j], 0) + 1
maximum = 0
for num in count:
    if num not in rim:
        maximum = max(maximum, count.get(num))
print("Task 1:", maximum)

for i in range(0, len(field)):
    for j in range(0, len(field[i])):
        dist = 0
        for line in f:
            dist += abs(i-int(line.split(', ')[0]))+ abs(j-int(line.split(', ')[1]))
        field[i][j] = dist
safeFields = 0
for i in range(0, len(field)):
    for j in range(0, len(field[i])):
        if field[i][j] < 10000:
            safeFields += 1
print("Task 2:", safeFields)

