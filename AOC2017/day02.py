def solve02():
    matrix = open('inputs/day02.txt').read().split('\n')
    checksum1 = checksum2 = 0
    for line in matrix:
        numbers = [int(x) for x in line.split('\t')]
        checksum1 += max(numbers)-min(numbers)
        checksum2 += int(division_line(numbers))
    print('Task 1:', checksum1)
    print('Task 2:', checksum2)


def division_line(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if max(numbers[i], numbers[j]) % min(numbers[i], numbers[j]) == 0:
                return max(numbers[i], numbers[j]) / min(numbers[i], numbers[j])
