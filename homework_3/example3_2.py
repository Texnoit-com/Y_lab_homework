'''Надо написать декоратор для повторного выполнения декорируемой функции
через некоторое время. Использует наивный экспоненциальный рост времени
повтора (factor) до граничного времени ожидания (border_sleep_time).'''


from functools import wraps
from time import sleep


def repeater(call_count=1, start_sleep_time=0.5,
             factor=2, border_sleep_time=15):
    '''Повторение выполнения кода'''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            for counter in range(call_count):
                value = func(*args, **kwargs)
                sleep_time = start_sleep_time * factor ** counter
                if sleep_time >= border_sleep_time:
                    sleep_time = border_sleep_time
                print(f'Запуск номер {counter+1}. Ожидание:'
                      f' {sleep_time} секунд. Результат '
                      f'декорируемой функций = {value}')
                sleep(sleep_time)
            print('Конец работы')
        return wrapper
    return decorator


@repeater(5, 2, 2, 20)
def user_sqrt(number: int):
    return number * 2


if __name__ == '__main__':
    user_sqrt(3)
