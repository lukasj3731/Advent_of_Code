operators = {'set': '=', 'mul': '*=', 'sub': '-=', }
multiplications = index = a = b = c = d = e = f = g = h = 0


def get_instr(asm_code):
    components = asm_code.split(' ')
    if components[0] == 'jnz':
        return 'index += '+components[2]+' if '+components[1]+' != 0 else 1'
    else:
        return components[1] + operators[components[0]]+components[2] + '\nindex += 1' \
               + ('\nmultiplications += 1' if components[0] == 'mul' else '')


def solve23():
    instructions = [get_instr(asm_code) for asm_code in open('inputs/day23.txt').read().split('\n')]
    while index < len(instructions):
        exec(instructions[index], globals())
    print(multiplications)

    b = 99 * 100 + 100000   # thx to https://www.reddit.com/user/jonathan_paulson/ for the following, cause there is
    c = b + 17000           # nothing i hate more than decompiling assembly code
    ans = 0

    def is_composite(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return True
            i += 1
        return False

    while True:
        if is_composite(b):
            ans += 1
        if b == c:
            break
        b += 17
    print(ans)
