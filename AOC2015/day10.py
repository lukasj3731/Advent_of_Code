import re


def solve10():
    string = open('inputs//day10.txt').read()
    for i in range(40):
        new_string = ''
        for element in re.findall(r'((.)(\2*))', string):
            new_string += str(len(element[0])) + element[0][0]
        string = new_string
    t1 = len(string)
    for i in range(10):
        new_string = ''
        for element in re.findall(r'((.)(\2*))', string):
            new_string += str(len(element[0])) + element[0][0]
        string = new_string
    return t1, len(string)
