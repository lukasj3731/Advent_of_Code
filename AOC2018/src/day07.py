import os.path
import re

f = open(os.path.dirname(__file__) + '/../inputs/input07.txt').read().split('\n')

Map = dict()
for c in range(65, 91):
    Map[chr(c)] = ''

for line in f:
    match = re.findall('( [A-Z] )', line)
    Map[match[1].replace(' ', '')] += match[0].replace(' ', '')
output = ''
for i in range(0, 26):
    char = ''
    for c in range(65, 91):
        if char == '' and len(Map[chr(c)])==0:
            char = chr(c)
    output += char
    Map[char] = '.'
    for c in range(65, 91):
        Map[chr(c)] = Map[chr(c)].replace(char, '')
print('Task 1:', output)

Map = dict()
workersNum = 5
offset = 60
workers = []
for c in range(ord('A'), ord('Z')+1):
    Map[chr(c)] = ''
for line in f:
    match = re.findall('( [A-Z] )', line)
    Map[match[1].replace(' ', '')] += match[0].replace(' ', '')

for i in range(0, workersNum):
    workers.append('.')

print(Map)

done = False
while not done:
    done = True
    for i in range(0, len(workers)):
        completed = True
        toCompletion = 999
        for c in range(ord('A'), ord('Z')+1):
            if 0 < workers[i].count(chr(c)) < int(c)-64+offset:
                completed = False
        if not completed:
            workers[i] += workers[i][len(workers[i])-1]
        else:
            char = '.'
            for c in range(ord('A'), ord('Z')+1):
                if char == '.' and len(Map[chr(c)]) == 0:
                    char = chr(c)
            workers[i] += char
            Map[char] = '.'

        done = done and workers[i][len(workers[i]) - 1] == '.'

    for i in range(0, len(workers)):
        if workers[i].count(workers[i][len(workers[i])-1]) == ord(workers[i][len(workers[i])-1])-64+offset:
            if workers[i][len(workers[i])-1] != '.':
                for c in range(ord('A'), ord('Z')+1):
                    Map[chr(c)] = Map[chr(c)].replace(workers[i][len(workers[i])-1], '')

for i in range(0, len(workers)):
    print(workers[i])
print(len(workers[0])-2)

