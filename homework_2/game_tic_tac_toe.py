'''Игра «Обратные крестики-нолики» на поле 10 x 10 с правилом «Пять в ряд»'''


GAME_MODES = ('A', 'a', 'B', 'b')
USER_MARKER = 'X'
PLAY_BOARD = ['.' for x in range(100)]
BEST_SCORE = 1000


def field_rendering(board: list) -> None:
    '''Поле для игры'''
    print('     1 2 3 4 5 6 7 8 9 10')
    print('   -----------------------')

    for i in range(10):
        num_str = str(i + 1)
        if i < 9:
            num_str += ' '
        line = [board[i*10+j] for j in range(10)]
        print(num_str, '|', *line, '|')

    print('   -----------------------')


def game_role(row: list, marker: str) -> bool:
    '''Функция проверки проигрыша'''
    for i in range(len(row)-4):
        if row[i:i+5].count(marker) == 5:
            return True
    return False


def combinations_rule(board: list, marker: str) -> bool:
    '''Проверка комбинаций пройгрыша'''
    for i in range(10):
        if game_role(board[i*10:i*10+10], marker) or \
           game_role(board[i::10], marker) or \
           game_role(board[i:100-i*10:11], marker) or \
           game_role(board[i*10:100-i:11], marker) or \
           game_role(board[i*10+9:90+i+1:9], marker) or \
           game_role(board[i:i*10+1:9], marker):
            return True
    return False


def empty_fields(board: list) -> str:
    '''Формирвоание пустого поля'''
    return [x for x, val in enumerate(board) if val == '.']


def calculation_move(board: list,
                     marker: str,
                     cell: int,
                     is_max: bool,
                     score: int) -> int:
    '''Возвращает оценку расчета хода'''
    bot_marker: str = 'O' if marker == 'X' else 'X'
    if cell == 2:
        return 0
    if combinations_rule(board, marker):
        return -40
    elif combinations_rule(board, bot_marker):
        return 40
    elif len(empty_fields(board)) == 0:
        return 1

    if is_max:
        best_score = -score
        for i in empty_fields(board):
            board[i] = marker
            score = calculation_move(board, marker, cell + 1, False, score)
            board[i] = '.'
            best_score = max(best_score, score)
    else:
        best_score = score
        for i in empty_fields(board):
            board[i] = bot_marker
            score = calculation_move(board, marker, cell + 1, True, score)
            board[i] = '.'
            best_score = min(best_score, score)
    return best_score


def move_bot(board: list, mark: str) -> int:
    '''Просматривает пустые индексы и находит лучшию позицию'''
    move: int = None
    best_score: int = -BEST_SCORE
    for i in empty_fields(board):
        board[i] = mark
        score = calculation_move(board, mark, 0, False, BEST_SCORE)
        board[i] = '.'
        if score > best_score:
            best_score = score
            move = i
    print('----------Ход компьютера----------')
    return move


def user_choice(board: list) -> str:
    '''Проверка ввода игрока'''
    while True:
        user_cord = input('Введите координаты хода (столбец строка): ').split()
        try:
            x: int = int(user_cord[0])
            y: int = int(user_cord[1])
        except ValueError:
            print('--! Вы должны вводить числа !--')
            continue
        except IndexError:
            print('--! Вы ввели неправильно. Пример ввода: 1 1 !--')
            continue
        if 0 < x < 11 and 0 < y < 11:
            pos = (x - 1) * 10 + y - 1
            if board[pos] == '.':
                return pos
            print('--! Ячейка занята. Введите координаты другой ячейки !--')
        else:
            print('--! Координаты должны быть в диапазоне от 1 до 10 !--')


def game_status(board: list) -> bool:
    '''Состояние раунда игры'''
    if combinations_rule(board, 'X'):
        print('Победа O')
    elif combinations_rule(board, 'O'):
        print('Победа X')
    elif not combinations_rule(board, 'X') and not combinations_rule(board, 'O') and '.' not in board:
        print('Ход')
    else:
        return True
    return False


def game_mode() -> str:
    '''Выбор режима игры'''
    while True:
        print('Выберите режим игры: "A" - компьютер-игрок '
              '"B" компьютер-компьютер "Exit" закончить игру.')
        input_command = input('Режим игры: ')
        if input_command in ('Exit', 'exit'):
            return 'Exit'
        if input_command in GAME_MODES[:2]:
            return input_command
        print('--! Введите правильный режим !--')


def game_process(board_orig: list, curr_mark_orig: str) -> None:
    '''Главная функция игры'''
    while True:
        board: list = board_orig[:]
        curr_mark: str = curr_mark_orig
        command: str = game_mode()
        if command == 'Exit':
            break
        field_rendering(board)
        while game_status(board):
            if command in ('A', 'a') and curr_mark == 'X':
                player_position = user_choice(board)
            else:
                player_position = move_bot(board, curr_mark)
            board[player_position] = curr_mark
            curr_mark = 'O' if curr_mark == 'X' else 'X'
            field_rendering(board)


if __name__ == '__main__':
    game_process(PLAY_BOARD, USER_MARKER)
