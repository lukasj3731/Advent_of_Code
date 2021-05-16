import re


def room_valid(room):
    parts = room.split('-')
    return int(re.findall('[0-9]+', parts[-1])[0]) if parts[-1].split('[')[1][:-1] == chcksm(''.join(parts[:-1])) else 0


def chcksm(name):
    occurences = dict()
    for i in range(ord('a'), ord('z')+1):
        occurences[name.count(chr(i))] = occurences.get(name.count(chr(i)), '')+chr(i)
    return ''.join([occurences.get(i, '') for i in range(max(occurences.keys()), -1, -1)])[:5]


def decrypt(room, number):
    return ''.join([chr((ord(c)-ord('a')+number) % 26 + ord('a')) for c in room if 'a' <= c <= 'z'])


def solve04():
    rooms = open('inputs/day04.txt').read().split('\n')
    print('Task 1:', sum([room_valid(r) for r in rooms]))
    decrypted_rooms = [(decrypt(room, room_valid(room)), room_valid(room)) for room in rooms if room_valid(room) > 0]
    print('Task 2:', [room[1] for room in decrypted_rooms if room[0].__contains__('northpoleobjects')][0])
