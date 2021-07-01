import re


def solve07():
    rules = dict()
    variables = dict()
    for line in open('inputs/day07.txt').read().split('\n'):
        components = line.split(' -> ')
        rules[components[1]] = components[0]
    val_a = eval(rules, variables, 'a')
    rules['b'] = str(val_a)
    variables = dict()
    return val_a, eval(rules, variables, 'a')


def eval(rules, variables, expression):
    operator = re.findall('(OR|AND|NOT|RSHIFT|LSHIFT)', expression)
    if operator:
        if operator[0] == 'OR':
            components = expression.split(' OR ')
            return eval(rules, variables, components[0]) | eval(rules, variables, components[1])
        elif operator[0] == 'AND':
            components = expression.split(' AND ')
            return eval(rules, variables, components[0]) & eval(rules, variables, components[1])
        elif operator[0] == 'NOT':
            components = expression.split('NOT ')
            return ~eval(rules, variables, components[1])
        elif operator[0] == 'LSHIFT':
            components = expression.split(' LSHIFT ')
            return eval(rules, variables, components[0]) << eval(rules, variables, components[1])
        elif operator[0] == 'RSHIFT':
            components = expression.split(' RSHIFT ')
            return eval(rules, variables, components[0]) >> eval(rules, variables, components[1])
    else:
        try:
            return int(expression)
        except:
            pass
        try:
            return variables[expression]
        except:
            pass
        val = eval(rules, variables, rules[expression])
        variables[expression] = val
        return val
