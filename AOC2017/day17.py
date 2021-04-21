def solve17():
    steps = int(open('inputs/day17.txt').read())
    spinlock = [0]
    index = 0
    for i in range(1, 2017 + 1):
        index = (index + steps) % i + 1
        spinlock.insert(index, i)
    print('Task 1:', spinlock[spinlock.index(2017)+1])
    index = val = 0
    for i in range(1, 50000000 + 1):
        index = (index + steps) % i + 1
        if index == 1:
            val = i
    print('Task 2:', val)
