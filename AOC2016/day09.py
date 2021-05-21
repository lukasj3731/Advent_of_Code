import re, string


def solve09():
    word = open('inputs/day09.txt').read()
    print('Task 1:', len(decompress(word, False)))
    print('Task 2:', len(decompress(word, True)))


def decompress(word, rec):
    pos = 0
    ret = ''
    while pos < len(word):
        if word[pos] != '(':
            ret += word[pos]
            pos += 1
        else:
            index = word.find(')', pos)
            values = [int(i) for i in re.findall('[0-9]+', word[pos + 1:index])]
            pos = index + 1
            if rec:
                ret += decompress(word[pos:pos + values[0]], True) * values[1]
            else:
                ret += word[pos:pos + values[0]] * values[1]
            pos += values[0]
    return ret
