'''Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.'''


from itertools import combinations


def bananas(s: str) -> set:
    result: set = set()
    for combin in combinations(range(len(s)), len(s) - 6):
        list_word: list = list(s)
        for i in combin:
            list_word[i] = '-'
        variant = ''.join(list_word)

        if variant.replace('-', '') == 'banana':
            result.add(variant)
    return result


if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                    "b-a--nana", "-banan--a", "b-ana--na",
                                    "b---anana", "-bana--na", "-ba--nana",
                                    "b-anan--a", "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
