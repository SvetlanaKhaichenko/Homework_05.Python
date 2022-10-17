"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
from random import randint


konf = 100
sum_player_1 = 0
sum_player_2 = 0

while konf >= 1:
    player_1 = int(
        input('Сколько конфет возьмет первый игрок? не более 28 шт: '))
    if player_1 <= 28 and player_1 > 0:
        if player_1 < konf:
            konf = konf - player_1
            sum_player_1 += player_1
        elif player_1 == konf:
            sum_player_1 += player_1 + sum_player_2
            break
        elif player_1 > konf:
            print(
                f'Осталось {konf} конфет, вы можете забрать их и конфеты оппонента.')
            sum_player_1 += konf + sum_player_2
            break
    else:
        print('Вы ввели ошибочное число конфет')
        player_1 = int(
            input('Сколько конфет возьмет первый игрок? не более 28 шт.: '))

    player_2 = konf % 28+1
    if player_2 == 0:
        if konf != 28:
            player_2 = 27
            sum_player_2 += player_2
        elif konf - player_2 <= 28:
            player_2 = (konf - 28)+1
        else:
            player_2 = 28
            sum_player_2 += player_2
    elif player_2 == konf:
        sum_player_2 += player_2 + sum_player_1
        print(f'Второй игрок взял: {player_2} конфет.')
        break
    print(f'Второй игрок взял: {player_2} конфет.')
    konf = konf - player_2
    sum_player_2 += player_2


if sum_player_1 > sum_player_2:
    print('Первый игрок сделал ход последним и забирает все конфеты второго игрока.')
else:
    print('Второй игрок сделал ход последним и забирает все конфеты первого игрока.')
