import regex
import json


def solve12():
    file = open('inputs/day12.txt').read()
    return sum([int(x) for x in regex.findall('(-?[0-9]+)', file)]), sum_not_red(json.loads(file))


def sum_not_red(element):
    if isinstance(element, int):
        return element
    if isinstance(element, list):
        return sum(sum_not_red(e) for e in element)
    if isinstance(element, dict):
        if 'red' in element.values():
            return 0
        else:
            return sum(sum_not_red(e) for e in element.values())
    return 0
