"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
"""
from random import randint


konf = 100
sum_player_1 = 0
sum_player_2 = 0

while konf >= 1:
    player_1 = int(input('Сколько конфет возьмет первый игрок? не более 28 шт: '))
    if player_1 <= 28 and player_1 > 0:
        if player_1<konf:
            konf = konf - player_1
            sum_player_1 += player_1
        elif player_1 == konf:
            sum_player_1 += player_1
            break
        elif player_1 > konf:
            print(f'Осталось {konf} конфет, вы можете забрать их и конфеты оппонента.')
            sum_player_1 += konf + sum_player_2
            break
    else:
        print('Вы ввели ошибочное число конфет')
        player_1 = int(input('Сколько конфет возьмет первый игрок? не более 28 шт.: '))
   
    player_2 = randint(1,28)
    print(f'Второй игрок взял: {player_2} конфет.')
    if player_2<konf:
        konf = konf - player_2
        sum_player_2 += player_2
    elif player_2 == konf:
        sum_player_2 += player_2
        break
    elif player_2 > konf:
        print(f'Осталось {konf} конфет, вы можете забрать их и конфеты оппонента.')
        sum_player_2 += konf + sum_player_2
        break   
    else:
        print('Вы ввели ошибочное число конфет')
        player_2 = int(input('Сколько конфет возьмет второй игрок? не более 28 шт.: '))
    
   
if sum_player_1 > sum_player_2:
    print('Первый игрок сделал ход последним и забирает все конфеты второго игрока.')
else:
    print('Второй игрок сделал ход последним и забирает все конфеты первого игрока.')