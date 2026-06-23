from random import choice
import json
import time

selection_element = ['камень','ножницы','бумага']

selection_choice = {'камень':{'ножницы':True,'бумага':False},
                    'ножницы':{'бумага':True,'камень':False},
                    'бумага':{'камень':True,'ножницы':False}}  


class ScoreBoard:
    """Класс для сохранения результатов игры
    gamer - игрок
    board - сохраненые результаты"""

    def __init__(self, gamer):
        self.file_scores = 'scores.json' 
        self.gamer = gamer
        self.board = {self.gamer:0, 'Компьютер':0}
    
    def show_score(self):
        return f'Результат игры {self.gamer} - {self.board[self.gamer]} компьютер - {self.board["Компьютер"]}'  

    def add_point(self, winner):
        self.board[winner] += 1 

    def save_score(self):
        with open(self.file_scores,'w',encoding='utf-8') as file:
            json.dump(self.board,file,ensure_ascii=False)
    
        

def game():
    """Логика игры с выбором и сохранением результата"""

    print('Игра "Камень, ножницы, бумага"\n' \
          '               Правила игры\n'
          'выбираете один из элементов Камень,ножницы или бумагу\n' \
          'Ножницы сильнее бумаги но слабее камня, бумага сильнее камня но слабее ножниц\n' \
          'по результам выигравшей стороне засчитывается очко')
    
    gamer = input('Введите ваше имя: ')
    if gamer.strip() == '':
        gamer = "Аноним"

    scores = ScoreBoard(gamer)

    while True:
        print(scores.show_score())
       
        print('Введите цифру выбора: \n' \
        '1 - камень \n' \
        '2 - ножницы\n' \
        '3 - бумага\n' \
        '0 - окончание игры')
        you_selection = input('Ваш выбор: ') 

        if you_selection.strip() in ['0','1','2','3']:

            if you_selection == '0':
                print('Игра окончена')
                scores.save_score()
                break
            elif you_selection in ['1','2','3']:
                key_comp_selection = choice(selection_element)
                key_you_selection = selection_element[int(you_selection)-1]

                if key_you_selection == key_comp_selection:
                    result = None
                else:                 
                    result = selection_choice[key_you_selection][key_comp_selection]

                time.sleep(0.5)    
                if result == True:
                    scores.add_point(gamer)
                    print(f'Выиграл {gamer}')
                elif result == False:
                    scores.add_point('Компьютер')
                    print('Выиграл компьютер')
                elif result == None:
                    print('Ничья')
            
        else:
            print(f'Неверный выбор значения {you_selection}')
       
        print()

game()