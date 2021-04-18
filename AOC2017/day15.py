import re


def generate(number, factor, mod, filter):
    number = (number * factor) % 2147483647
    return number if not filter or number % mod == 0 else generate(number, factor ,mod, filter)


def judge(n1, n2, filter, iterations):
    pairs = 0
    for i in range(iterations):
        n1 = generate(n1, 16807, 4, filter)
        n2 = generate(n2, 48271, 8, filter)
        pairs += n1 % 65536 == n2 % 65536
    return pairs


def solve15():
    numbers = re.findall('[0-9]+', open('inputs/day15.txt').read())
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    print('Task 1:', judge(n1, n2, False, 40000000))
    print('Task 2:', judge(n1, n2, True, 5000000))
