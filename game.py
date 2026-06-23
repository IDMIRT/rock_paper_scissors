from random import choice
import json
import os

selection_element = ['камень','ножницы','бумага']

selection_choice = {'камень':{'ножницы':True,'бумага':False},
                    'ножницы':{'бумага':True,'камень':False},
                    'бумага':{'камень':True,'ножницы':False}}  

       


def game():

    print('Игра "Камень, ножницы, бумага"\n' \
          '               Правила игры\n'
          'выбираете один из элементов Камень,ножницы или бумагу\n' \
          'Ножницы сильнее бумаги но слабее камня, бумага сильнее камня но слабее ножниц\n' \
          'по результам выигравшей стороне засчитывается очко')
    
    gamer = input('Введите ваше имя: ')
    if gamer.strip == '':
        gamer = 'Аноним'

    scores = {gamer:0, 'Компьютер':0}

    while True:
        print(f'Результат игры {gamer} - {scores[gamer]} компьютер - {scores["Компьютер"]}')
        print('Введите цифру выбора: \n' \
        '1 - камень \n' \
        '2 - ножницы\n' \
        '3 - бумага\n' \
        '0 - окончание игры')
        you_selection = input('Ваш выбор: ') 

        if you_selection.strip() in ['0','1','2','3']:

            if you_selection == '0':
                print('Игра окончена')
                break
            elif you_selection in ['1','2','3']:
                key_comp_selection = choice(selection_element)
                key_you_selection = selection_element[int(you_selection)-1]

                if key_you_selection == key_comp_selection:
                    result = None
                else:                 
                    result = selection_choice[key_you_selection][key_comp_selection]
                    
                if result == True:
                    scores[gamer] += 1
                    print(f'Выиграл {gamer}')
                elif result == False:
                    scores['Компьютер'] += 1
                    print('Выиграл компьютер')
                elif result == None:
                    print('Ничья')
        
        else:
            print(f'Неверный выбор значения {you_selection}')
       

game()