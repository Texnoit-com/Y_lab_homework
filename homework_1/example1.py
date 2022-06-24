'''Написать метод domain_name, который вернет домен из url адреса'''


def domain_name(url: str) -> str:
    url = url.replace('http://', '', 1).\
        replace('https://', '', 1).\
        replace('www.', '', 1)
    return url.split('.')[0]


if __name__ == '__main__':
    assert domain_name('http://google.com') == 'google'
    assert domain_name('http://google.co.jp') == 'google'
    assert domain_name('www.xakep.ru') == 'xakep'
    assert domain_name('https://youtube.com') == 'youtube'
    assert domain_name('http://www.zombie-bites.com') == 'zombie-bites'
