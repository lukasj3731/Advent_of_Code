def solve01():
    file = open('inputs/day01.txt').read()
    index = floor = 0
    while floor >= 0:
        floor += 1 if file[index] == '(' else -1
        index += 1
    return file.count('(')-file.count(')'), index
