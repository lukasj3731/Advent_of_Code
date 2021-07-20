from functools import reduce


def solve20():
    house_num = 1
    min_presents = int(open('inputs/day20.txt').read())
    min_presents_1 = min_presents / 10
    min_presents_2 = min_presents / 11
    task_1 = task_2 = None
    while not task_1 or not task_2:
        if get_presents(house_num) >= min_presents_1 and not task_1:
            task_1 = house_num
        if get_presents2(house_num) >= min_presents_2 and not task_2:
            task_2 = house_num
        house_num += 1
    return task_1, task_2


def get_presents(house_num):
    return sum(factors(house_num))


def get_presents2(house_num):
    fact = factors(house_num)
    max_fact = max(fact)
    return sum(factor if factor*50 >= max_fact else 0 for factor in fact)


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))

