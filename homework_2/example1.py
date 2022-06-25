'''Надо написать класс CyclicIterator. Итератор должен итерироваться по
итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда
достигнет последнего элемента, начинать сначала.'''

from dataclasses import dataclass


@dataclass
class CyclicIterator:
    num: list
    index: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.num):
            result = self.num[self.index]
            self.index += 1
        else:
            self.index = 0
            result = self.num[self.index]
        return result


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(100))
    for i in cyclic_iterator:
        print(i)
