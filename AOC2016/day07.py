import re


def aba_in_bab(abas, babs):
    for aba in abas:
        for bab in babs:
            if aba[0] == bab[1] and bab[0] == aba[1]:
                return True
    return False


def solve07():
    t1 = t2 = 0
    for ip in open('inputs/day07.txt').read().split('\n'):
        parts = ip.replace('[', ']').split(']')
        if re.search(r'(?!(\w)\1\1\1)(\w)(\w)\3\2', ' '.join(parts[::2])) \
                and not re.search(r'(?!(\w)\1\1\1)(\w)(\w)\3\2', ' '.join(parts[1::2])):
            t1 += 1
        if aba_in_bab([e[0] for e in re.findall(r'(?=((.)(?!\2).\2))', ' '.join(parts[::2]))],
                      [e[0] for e in re.findall(r'(?=((.)(?!\2).\2))', ' '.join(parts[1::2]))]):
            t2 += 1
    print('Task 1:', t1)
    print('Task 2:', t2)
