'''Написать метод count_find_num, который принимает на вход список простых
множителей (primesl) и целое число, предел (limit), после чего попробуйте
сгенерировать по порядку все числа. Меньшие значения предела, которые имеют все
и только простые множители простых чисел primesl'''

from math import prod


def count_find_num(primesl: list, limit: int) -> list:
    valid_factors: int = prod(primesl)
    all_factors: set = set()
    all_factors.add(valid_factors)
    if valid_factors > limit:
        return []
    old_values = {valid_factors}
    while valid_factors <= limit:
        new_values: set = set()
        for index in old_values:
            for i in primesl:
                element: int = index * i
                new_values.add(element)
                if element <= limit:
                    all_factors.add(element)
        valid_factors = min(new_values)
        old_values = {index for index in new_values if index < limit}
    return [len(all_factors), max(all_factors)]


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
