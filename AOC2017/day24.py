import re

max_val = -1

def solve24():
    components_list = open('inputs/day24.txt').read().split('\n')
    components = [(int(c.split('/')[0]), int(c.split('/')[1])) for c in components_list]
    build('0', components)
    print(max_val)


def build(chain, components):
    last = int(chain.split('/')[-1])
    for i in range(len(components)):
        component = components[i]
        if component.__contains__(last):
            if component[1] == last:
                component = (component[1], component[0])
            build(chain+'--'+to_component(component), components[:i]+components[i+1:])
    update_max(chain)


def to_component(c):
    return str(c[0])+'/'+str(c[1])


def update_max(chain):
    global max_val
    val = sum([int(v) for v in re.findall('[0-9]+', chain)])
    max_val = max(max_val, val)
