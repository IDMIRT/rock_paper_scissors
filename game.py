from random import choice
selection_element = ['камень','ножицы','бумага']
                  

def selection_processing(user_selection, comp_selection):
    """Процедура обработки выбора пользователя и игрока
    user_selection - выбор пользоваетля
    comp_selection - выбор компьютера
    возврат True - выиграл пользователь False - выиграл компьютер, None - ничья"""
    if user_selection == comp_selection:
        return None
    elif user_selection == 'камень' and comp_selection == 'ножницы':
        return True
    elif user_selection == 'ножницы' and comp_selection == 'камень':
        return False
    elif user_selection == 'ножницы' and comp_selection == 'бумага':
        return True
    elif user_selection == 'бумага' and comp_selection == 'ножницы':
        return False
    elif user_selection == 'бумага' and comp_selection == 'камень':
        return True
    elif user_selection == 'камень' and comp_selection == 'бумага':
        return False

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
        if you_selection.strip in ['0','1','2','3']:

            if you_selection == '0':
                print('Игра окончена')
                break
            elif you_selection in ['1','2','3']:
                comp_selection = choice(selection_element)
                result = selection_processing(selection_element[int(you_selection)-1], comp_selection)
                if result == True:
                    scores[gamer] += 1
                else:
                    scores['Компьютер'] += 1

        
        else:
            print(f'Неверный выбор значения {you_selection}')
       
