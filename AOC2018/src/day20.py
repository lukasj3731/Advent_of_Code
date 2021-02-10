import os.path

f = open(os.path.dirname(__file__) + '/../inputs/input20.txt').read()[1:-1]
distances = dict()
px, py = x, y = 0, 0
stack = []
distances[(0, 0)] = 0
for c in f:
    if c == '(':
        stack.append((x, y))
    elif c == ')':
        x, y = stack.pop()
    elif c == '|':
        x, y = stack[-1]
    else:
        x = x + (c == 'N') - (c == 'S')
        y = y + (c == 'E') - (c == 'W')
        distances[(x, y)] = min(distances.get((x, y), 99999), distances[(px, py)]+1)
    px, py = x, y

print(max(distances.values()))
print(sum([(1000 <= dist) for dist in distances.values()]))
