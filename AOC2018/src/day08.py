import os.path


def recSum(numbers):
    sum = 0
    children = numbers.pop(0)
    meta = numbers.pop(0)
    for i in range(0, children):
        sum += recSum(numbers)
    for i in range(0, meta):
        sum += numbers.pop(0)
    return sum


def recSum2(numbers):
    sum = 0
    childCount = numbers.pop(0)
    meta = numbers.pop(0)
    if childCount == 0:
        for i in range(0, meta):
            sum += numbers.pop(0)
    else:
        children = []
        for i in range(0, childCount):
            children.append(recSum2(numbers))
        for i in range(0, meta):
            tmp = numbers.pop(0)
            if tmp-1 < len(children):
                sum += children[tmp-1]
    return sum


queue = []
f = open(os.path.dirname(__file__) + '/../inputs/input08.txt').read().split(' ')
for n in f:
    queue.append(int(n))
print('task 1:', recSum(queue.copy()))
print('task 2:', recSum2(queue))

