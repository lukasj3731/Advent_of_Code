def solve19():
    number = int(open('inputs/day19.txt').read())
    print('Task 1:', int(bin(number)[3:]+bin(number)[2], 2))
    i = 1
    while i*3 < number:
        i *= 3
    print('Task 2:', number-i)
