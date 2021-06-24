def solve02():
    wrapping_paper = ribbon = 0
    for line in open('inputs/day02.txt').read().split('\n'):
        dim = [int(number) for number in line.split('x')]
        dim.sort()
        wrapping_paper += 3*dim[0]*dim[1]+2*dim[1]*dim[2]+2*dim[0]*dim[2]
        ribbon += dim[0]*2+dim[1]*2+dim[0]*dim[1]*dim[2]
    return wrapping_paper, ribbon
