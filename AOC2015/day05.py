import re


def solve05():
    sum1 = sum2 = 0
    for string in open('inputs/day05.txt').read().split('\n'):
        if len(re.findall(r'[aeiou]', string)) >= 3 \
                and re.search(r'.*(.)\1', string) \
                and len(re.findall('(ab|cd|pq|xy)', string)) == 0:
            sum1 += 1
        if re.match(r'.*(.)(.).*\1\2', string) and re.match(r'.*(.).\1', string):
            sum2 += 1
    return sum1, sum2
