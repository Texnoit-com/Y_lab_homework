'''Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса.
Модуль ipaddress входит в стандартный пакет python'''
from ipaddress import IPv4Address


def int32_to_ip(int32: int) -> str:
    return str(IPv4Address(int32))


if __name__ == '__main__':
    assert int32_to_ip(2154959208) == '128.114.17.104'
    assert int32_to_ip(0) == '0.0.0.0'
    assert int32_to_ip(2149583361) == '128.32.10.1'
