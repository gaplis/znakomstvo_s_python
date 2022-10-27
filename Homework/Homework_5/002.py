# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint, choice


def check_take(amount, amount_of_take, player):
    while True:
        if player == 'Бот':
            num = randint(1, amount_of_take)
        else:
            num = int(input(f'Введите количество конфет от 1 до {amount_of_take}: '))
        if amount_of_take < num:
            print('Неверное количество конфет')
        elif num > amount:
            print('Нельзя взять конфет больше, чем в банке')
        else:
            return num


def process(amount, amount_of_take, player_one, player_two, turn, current_player):
    print(f'В банке с конфетами: {amount}')
    while amount > 0:
        player_take = check_take(amount, amount_of_take, current_player)
        print(f'Игрок {current_player} взял {player_take}')
        if current_player == player_one:
            current_player = player_two
            turn = 2
        else:
            current_player = player_one
            turn = 1
        amount -= player_take
        print(f'В банке осталось конфет: {amount}')
        print()
    return turn


def play(amount, amount_of_take, players):
    player_one = input('Имя первого игрока: ')
    if players == 2:
        player_two = input('Имя второго игрока: ')
    else:
        player_two = 'Бот'
    current_player = player_one
    coin = choice(['0', '1'])
    if coin == '0':
        print(f'Ходит {player_one}')
        current_player = player_one
        turn = 1
    else:
        print(f'Ходит {player_two}')
        current_player = player_two
        turn = 2
    if process(amount, amount_of_take, player_one, player_two, turn, current_player) == 2:
        print(f'Победил {player_one}')
    else:
        print(f'Победил {player_two}')

amount = 2021
amount_of_take = 28
player_or_bot = int(input('Выберете режим игры:\n'
                 '1. Бот\n'
                 '2. Два игрока\n'))
play(amount, amount_of_take, player_or_bot)