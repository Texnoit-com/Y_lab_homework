'''Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:'''


def zeros(n: int) -> int:
    x: int = n // 5
    y: int = x
    while x > 0:
        x /= 5
        y += int(x)
    return y


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
