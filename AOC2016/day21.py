import re
import itertools


def scramble(instructions, password):
    password = [letter for letter in password]
    for instruction in instructions:
        if instruction.__contains__('swap position'):
            numbers = [int(x) for x in re.findall('[0-9]+', instruction)]
            tmp = password[numbers[0]]
            password[numbers[0]] = password[numbers[1]]
            password[numbers[1]] = tmp
        elif instruction.__contains__('swap letter'):
            numbers = [password.index(instruction[12]), password.index(instruction[26])]
            tmp = password[numbers[0]]
            password[numbers[0]] = password[numbers[1]]
            password[numbers[1]] = tmp
        elif instruction.__contains__('rotate based'):
            number = password.index(instruction[35])
            number = -1 - number if number < 4 else -2 - number
            number %= len(password)
            password = password[number:] + password[:number]
        elif instruction.__contains__('rotate '):
            number = int(re.findall('[0-9]+', instruction)[0])
            if instruction.__contains__('right'):
                number *= -1
            password = password[number:]+password[:number]
        elif instruction.__contains__('reverse positions'):
            numbers = [int(x) for x in re.findall('[0-9]+', instruction)]
            password[numbers[0]:numbers[1]+1] = password[numbers[0]:numbers[1]+1][::-1]
        else:
            numbers = [int(x) for x in re.findall('[0-9]+', instruction)]
            password.insert(numbers[1], password.pop(numbers[0]))
    return ''.join(password)


def solve21():
    print('hi')
    instructions = open('inputs/day21.txt').read().split('\n')
    print('Task 1:', scramble(instructions, 'abcdefgh'))
    for password in list(itertools.permutations('abcdefgh')):
        if scramble(instructions, ''.join(password)) == 'fbgdceah':
            print('Task 2:', ''.join(password))
            return
