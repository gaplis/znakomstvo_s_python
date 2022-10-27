# Создайте программу для игры в "Крестики-нолики".

from random import choice


def check_x_o(lst):
    if lst[0][0] == 'x' and lst[1][0] == 'x' and lst[2][0] == 'x' \
        or lst[0][1] == 'x' and lst[1][1] == 'x' and lst[2][1] == 'x' \
        or lst[0][2] == 'x' and lst[1][2] == 'x' and lst[2][2] == 'x' \
        or lst[0][0] == 'x' and lst[0][1] == 'x' and lst[0][2] == 'x' \
        or lst[1][0] == 'x' and lst[1][1] == 'x' and lst[1][2] == 'x' \
        or lst[2][0] == 'x' and lst[2][1] == 'x' and lst[2][2] == 'x' \
        or lst[0][0] == 'x' and lst[1][1] == 'x' and lst[2][2] == 'x' \
        or lst[0][2] == 'x' and lst[1][1] == 'x' and lst[2][0] == 'x':
        return True
    elif lst[0][0] == 'o' and lst[1][0] == 'o' and lst[2][0] == 'o' \
        or lst[0][1] == 'o' and lst[1][1] == 'o' and lst[2][1] == 'o' \
        or lst[0][2] == 'o' and lst[1][2] == 'o' and lst[2][2] == 'o' \
        or lst[0][0] == 'o' and lst[0][1] == 'o' and lst[0][2] == 'o' \
        or lst[1][0] == 'o' and lst[1][1] == 'o' and lst[1][2] == 'o' \
        or lst[2][0] == 'o' and lst[2][1] == 'o' and lst[2][2] == 'o' \
        or lst[0][0] == 'o' and lst[1][1] == 'o' and lst[2][2] == 'o' \
        or lst[0][2] == 'o' and lst[1][1] == 'o' and lst[2][0] == 'o':
        return True   
    else: return False

def process(player_one, player_two, turn, current_player, lst):
    res = False
    while res == False:
        strok = int(input(f'Ходит {current_player}. Введите строку: ')) - 1
        stolb = int(input(f'Введите столбец: ')) - 1
        if strok >= 0 and strok <= 2 and stolb >= 0 and stolb <= 2:
            if current_player == player_one:
                if lst[strok][stolb] != 'x' and lst[strok][stolb] != 'o':
                    lst[strok][stolb] = 'x'
                    current_player = player_two
                    turn = 2
                else: print('Неверно, попробуйте ещё')
            else:
                if lst[strok][stolb] != 'x' and lst[strok][stolb] != 'o':
                    lst[strok][stolb] = 'o'
                    current_player = player_one
                    turn = 1
                else: print('Неверно, попробуйте ещё')
        else: print('Неверно, попробуйте ещё')
        print(*x_o, sep='\n')
        res = check_x_o(lst)
    return turn
    
def play(lst):
    player_one = input('Имя первого игрока: ')
    player_two = input('Имя второго игрока: ')
    current_player = player_one
    coin = choice(['0', '1'])
    if coin == '0':
        print(f'Первый ходит {player_one}')
        current_player = player_one
        turn = 1
    else:
        print(f'Первый ходит {player_two}')
        current_player = player_two
        turn = 2
    if process(player_one, player_two, turn, current_player, lst) == 2:
        print(f'Победил {player_one}')
    else:
        print(f'Победил {player_two}')


x_o = [['*' for _ in range(3)] for _ in range(3)]

print(*x_o, sep='\n')

play(x_o)