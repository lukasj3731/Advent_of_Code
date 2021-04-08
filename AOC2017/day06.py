def redistribute(banks):
    max_blocks = max(banks)
    index = min([x for x in range(len(banks)) if banks[x] == max_blocks])
    banks[index] = 0
    index = (index + 1) % len(banks)
    while max_blocks > 0:
        banks[index] += 1
        index = (index + 1) % len(banks)
        max_blocks -= 1


def num_till_repetitions(banks):
    seen = set()
    counter = 0
    while not seen.__contains__(str(banks)):
        seen.add(str(banks))
        redistribute(banks)
        counter += 1
    return counter


def solve06():
    banks = [int(x) for x in open('inputs/day06.txt').read().split('\t')]
    print('Task 1:', num_till_repetitions(banks))
    print('Task 2:', num_till_repetitions(banks))    # this works differently for the second task, since banks is still changed from the first run
