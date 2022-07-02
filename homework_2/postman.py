'''Разработать программу для вычисления кратчайшего пути для почтальона.'''

from dataclasses import dataclass
from itertools import combinations, permutations

POINTS = {
    'Почтовое отделение': (0, 2),
    'Ул. Грибоедова, 104/25': (2, 5),
    'Ул. Бейкер стрит, 221б': (5, 2),
    'Ул. Большая Садовая, 302-бис': (6, 6),
    'Вечнозелёная Аллея, 742': (8, 3)
    }


@dataclass
class Postman():
    points: dict

    def get_shortest_path(self) -> str:
        '''Расчет самого короткого пути'''
        length_route: float = None
        section_segment: tuple = None
        lenght_section: list = None
        segments: dict = self.get_segments()
        sequences: list = self.get_route()

        for segment in sequences:
            path_len: float = 0
            intermediate: list = []
            for i in range(len(segment) - 1):
                path_len += segments[(segment[i], segment[i+1])]
                intermediate.append(path_len)
            if length_route is None or length_route > path_len:
                length_route = path_len
                section_segment = segment
                lenght_section = intermediate

        return self._get_result_string(section_segment,
                                       lenght_section,
                                       length_route)

    def get_segments(self) -> dict:
        '''Формирование словаря с расстояниями до пунктов'''
        segments: list = list(combinations(self.points.keys(), 2))
        length: dict = {}
        for start, finish in segments:
            count = ((self.points[finish][0] - self.points[start][0]) ** 2 +
                     (self.points[finish][1] - self.points[start][1]) ** 2) ** 0.5
            length[(start, finish)] = count
            length[(finish, start)] = count
        return length

    def get_route(self) -> list:
        '''Формирование маршрутов через точки от почтового отделения
        с возвращением на почтовое отделение'''
        route: list = list(self.points.keys())
        route.remove('Почтовое отделение')
        start_route = 'Почтовое отделение'
        return [(start_route,) + segment + (start_route,)
                for segment in permutations(route, len(route))]

    def _get_result_string(self, section_segment,
                           lenght_section, length_route) -> str:
        '''Создание форматированного ответа'''
        result: str = str(self.points[section_segment[0]])
        section_segment = section_segment[1:]

        for point_num, intermediate in zip(section_segment, lenght_section):
            result += f' -> {str(self.points[point_num])}[{intermediate}]'

        result += f' = {str(length_route)}'
        return result


if __name__ == '__main__':
    postman = Postman(POINTS)
    print(postman.get_shortest_path())
