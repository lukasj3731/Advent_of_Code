def solve_captcha(captcha, offset):
    return sum([int(captcha[i]) for i in range(len(captcha))
                if captcha[i] == captcha[(i+offset) % len(captcha)]])


def solve01():
    captcha = open('inputs/day01.txt').read()
    print('Task 1:', solve_captcha(captcha, 1))
    print('Task 2:', solve_captcha(captcha, len(captcha)//2))
