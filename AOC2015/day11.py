def solve11():
    password = [letter for letter in open('inputs/day11.txt').read()]
    passwords = ['', '']
    for i in range(2):
        inc(password)
        while not valid(password):
            inc(password)
        passwords[i] = ''.join(password)
    return passwords[0], passwords[1]


def inc(password):
    length = len(password) - 1
    while password[length] == 'z' and length >= 0:
        password[length] = 'a'
        length -= 1
    if length == -1:
        password.insert(0, 'a')
    else:
        password[length] = chr(ord(password[length]) + 1)


def valid(password):
    if 'i' in password or 'l' in password or 'o' in password:
        return False
    double_letters = 0
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            double_letters += 1
            i += 2
        else:
            i += 1
    if double_letters < 2:
        return False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            double_letters = True
    if not double_letters:
        return False
    ascending_letters = False
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 == ord(password[i+2])-2:
            ascending_letters = True
    return ascending_letters
