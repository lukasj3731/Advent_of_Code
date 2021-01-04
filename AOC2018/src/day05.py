import os.path


def collapse(f):
    oldf = f
    run = True
    while run:
        for char in range(65, 91):
            f = f.replace(chr(char) + chr(char + 32), '')
            f = f.replace(chr(char + 32) + chr(char), '')
        run = oldf != f
        oldf = f
    return f


file = open(os.path.dirname(__file__) + '/../inputs/input05.txt').read()
print('Task 1:', len(collapse(file)))
minimum = len(collapse(file))
for char in range(65, 91):
    f = file.replace(chr(char), '')
    f = f.replace(chr(char+32), '')
    minimum = min(minimum, len(collapse(f)))
print('Task 2:', minimum)

