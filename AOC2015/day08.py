def solve08():
    strings = open('inputs/day08.txt').read()
    return sum([len(strg)-len(bytes(strg, "utf-8").decode("unicode_escape"))+2 for strg in strings.split('\n')]), \
           strings.count('"')+strings.count('\\')+(strings.count('\n')+1)*2
