def phrase_valid(phrase, mode):
    words = phrase.split(' ')
    if mode == 2:
        words = [''.join(sorted(word)) for word in words]   # alphabetically sorting words for part 2
    return len(words) == len(set(words))


def solve04():
    phrases = open('inputs/day04.txt').read().split('\n')
    sum0 = sum1 = 0
    for phrase in phrases:
        sum0 += phrase_valid(phrase, 1)
        sum1 += phrase_valid(phrase, 2)
    print('Task 1:', sum0)
    print('Task 2:', sum1)
