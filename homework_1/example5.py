'''Написать метод count_find_num, который принимает на вход список простых
множителей (primesl) и целое число, предел (limit), после чего попробуйте
сгенерировать по порядку все числа. Меньшие значения предела, которые имеют все
и только простые множители простых чисел primesl'''

from math import prod


def count_find_num(primesl: list, limit: int) -> list:
    valid_factors: list = []
    all_factors: list = []
    for index in range(2, limit+1):
        factors: list = []
        divisor: int = 2
        while divisor <= index:
            if index % divisor == 0:
                factors.append(divisor)
                index = index / divisor
            else:
                divisor += 1
        all_factors.append(factors)

    for factor in all_factors:
        if set(primesl) == set(factor):
            valid_factors.append(factor)

    if valid_factors:
        iterations = len(valid_factors)
        max_number = max([prod(factor) for factor in valid_factors])
        return [iterations, max_number]
    else:
        return []


if __name__ == "__main__":
    primesl = [2, 3]
    limit = 200
    assert count_find_num(primesl, limit) == [13, 192]

    primesl = [2, 5]
    limit = 200
    assert count_find_num(primesl, limit) == [8, 200]

    primesl = [2, 3, 5]
    limit = 500
    assert count_find_num(primesl, limit) == [12, 480]

    primesl = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesl, limit) == [19, 960]

    primesl = [2, 3, 47]
    limit = 200
    assert count_find_num(primesl, limit) == []
