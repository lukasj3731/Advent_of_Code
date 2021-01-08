import os.path
import re

f = open(os.path.dirname(__file__) + '/../inputs/input07.txt').read().split('\n')

Map = dict()
for c in range(65, 91):
    Map[chr(c)] = ''

for line in f:
    match = re.findall('( [A-Z] )', line)
    Map[match[0].replace(' ', '')] += match[1].replace(' ', '')
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
print(output)
print(Map)
print(f)

