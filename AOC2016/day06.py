from collections import Counter


def solve06():
    letters = dict()
    for line in open('inputs/day06.txt'):
        for i in range(len(line)):
            letters[i] = letters.get(i, '')+line[i]
    print('Task 1:', ''.join([Counter(letters[i]).most_common(1)[0][0] for i in range(len(letters))]), end='')
    print('Task 2:', ''.join([Counter(letters[i]).most_common()[-1][0] for i in range(len(letters))]), end='')
