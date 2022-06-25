'''Надо написать класс CyclicIterator. Итератор должен итерироваться по 
итерируемому объекту (list, tuple, set, range, Range2, и т. д.), и когда 
достигнет последнего элемента, начинать сначала.'''

from dataclasses import dataclass


@dataclass
class CyclicIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
