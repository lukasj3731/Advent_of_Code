import os.path


f = open(os.path.dirname(__file__) + '/../inputs/input14.txt').read()
s = '37'
p0, p1 = 0, 1
while f not in s[-7:]:
    s += str(int(s[p0])+int(s[p1]))
    p0 = (p0 + int(s[p0]) + 1) % len(s)
    p1 = (p1 + int(s[p1]) + 1) % len(s)
print('task 1', s[int(f):int(f)+10])
print('task 2', len(s)-len(str(f)) - 1)




