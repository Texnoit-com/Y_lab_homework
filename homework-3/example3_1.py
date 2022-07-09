'''Напишите функцию-декоратор, которая сохранит (закэширует) значение 
декорируемой функции multiplier (Чистая функция). Если декорируемая 
функция будет вызвана повторно с теми же параметрами — декоратор должен 
вернуть сохранённый результат, не выполняя функцию.'''

from functools import wraps


def cached(func):
    cache: dict = dict()

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not cache.get(args):
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper


@cached
def multiplier(number: int):
    '''Функция с декоратором, который
    кэширует результаты вызова .'''
    return number * 2


if __name__ == "__main__":
    print(multiplier(2))
    print(multiplier(2))
